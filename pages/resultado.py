import streamlit as st
import requests
from urllib.parse import unquote
from datetime import datetime
from pages.utils import DEFAULTS, logo_html
import streamlit.components.v1 as components

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwpnrMS3XP3YUVQkcK8C56ml7rdc-oUTUMKk5aLtWvVwKPrXLUN0k-gZar7KALVjMW2/exec"

DOIS_FA_LABEL = {
    "nao":                 "Nao conhece",
    "sim_conheco_nao_uso": "Conhece mas nao usa",
    "sim_utilizo":         "Utiliza",
}

VARIANTES = {
    "expert": (
        "🎉", "PARABÉNS,", "EXPERT",
        "Você é um verdadeiro <strong>expert</strong> em segurança digital! "
        "Acertou todos os golpes e já utiliza a Autenticação de Dois Fatores.",
        "Continue assim e compartilhe com <strong>amigos</strong> e "
        "<strong>familiares</strong>. Juntos tornamos a internet mais segura!",
        ""
    ),
    "bom": (
        "👍", "MANDOU BEM,", "BOM",
        "Você tem <strong>ótima</strong> capacidade de identificar golpes por e-mail.",
        "Que tal ativar a <strong>Autenticação de Dois Fatores</strong>? "
        "Com ela você bloqueia <strong>99,9%</strong> dos ataques.",
        ""
    ),
    "atencao": (
        "💡", "BOM TRABALHO,", "ATENCAO",
        "Você já utiliza a Autenticação de Dois Fatores, o que é <strong>excelente!</strong>",
        "Ainda dá para melhorar na identificação de e-mails falsos. "
        "Revise as dicas sobre remetentes suspeitos e links enganosos.",
        "Para <strong>mais dicas</strong>, pegue um panfleto!"
    ),
    "estudar": (
        "📚", "HORA DE ESTUDAR,", "ESTUDAR",
        "Você identificou alguns golpes, mas ainda pode <strong>melhorar</strong>.",
        "Revise <strong>Phishing</strong> e <strong>Engenharia Social</strong>, "
        "ative o <strong>2FA</strong> e pratique identificar e-mails suspeitos.",
        "Para <strong>mais dicas</strong>, pegue um panfleto!"
    ),
    "cuidado": (
        "⚠️", "CUIDADO,", "CUIDADO",
        "Você está <strong>vulnerável</strong> aos golpes digitais.",
        "Revise todo o conteúdo, ative a <strong>Autenticação de Dois Fatores</strong> "
        "urgentemente e nunca clique em links suspeitos.",
        "Para <strong>mais dicas</strong>, pegue um panfleto!"
    ),
}


def _variante(score: int, two_fa: str) -> str:
    if score >= 5 and two_fa == "sim_utilizo":  return "expert"
    if score >= 4 and two_fa != "sim_utilizo":  return "bom"
    if score >= 3 and two_fa == "sim_utilizo":  return "atencao"
    if score >= 3 and two_fa != "sim_utilizo":  return "estudar"
    return "cuidado"


def _geo_por_ip(ip: str) -> tuple:
    """Consulta ipapi.co com o IP real do usuário."""
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        d = r.json()
        cidade = d.get("city", "Desconhecida")
        estado = d.get("region", d.get("region_code", "Desconhecido"))
        return cidade, estado
    except Exception:
        return "Desconhecida", "Desconhecido"


def _enviar(score, two_fa, label, nome_completo, cidade, estado):
    if st.session_state.get("resultado_enviado", False):
        return
    primeiro = nome_completo.strip().split()[0].capitalize() if nome_completo.strip() else "Anonimo"
    try:
        requests.post(WEBHOOK_URL, json={
            "nome":      primeiro,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "cidade":    cidade,
            "estado":    estado,
            "score":     f"{score}/5",
            "dois_fa":   DOIS_FA_LABEL.get(two_fa, two_fa),
            "resultado": label,
        }, timeout=6)
        st.session_state.resultado_enviado = True
    except Exception:
        pass


def page_resultado() -> None:
    score  = st.session_state.quiz_score
    two_fa = st.session_state.two_factor_knowledge
    nome   = st.session_state.user_name
    key    = _variante(score, two_fa)
    emoji, titulo, label, msg1, msg2, nota = VARIANTES[key]

    # ── Passo 1: captura o IP real do usuário via JS ──────────────────────────
    # O JS pede o IP ao ipify (sem permissão necessária) e redireciona com ?user_ip=
    user_ip = unquote(st.query_params.get("user_ip", ""))

    if user_ip:
        # Chegou de volta com o IP — faz a consulta geo no servidor e salva
        st.query_params.clear()
        if not st.session_state.get("geo_cidade"):
            cidade, estado = _geo_por_ip(user_ip)
            st.session_state.geo_cidade = cidade
            st.session_state.geo_estado = estado

    cidade = st.session_state.get("geo_cidade", "")
    estado = st.session_state.get("geo_estado", "")

    # Se ainda não temos o IP, injeta JS silencioso para buscá-lo
    if not cidade:
        components.html("""
<!DOCTYPE html><html><head></head><body>
<script>
fetch('https://api.ipify.org?format=json')
  .then(function(r){ return r.json(); })
  .then(function(data){
    var url = new URL(window.parent.location.href);
    url.searchParams.set('user_ip', data.ip);
    window.parent.location.href = url.toString();
  })
  .catch(function(){
    // ipify falhou — tenta api64 como fallback
    fetch('https://api64.ipify.org?format=json')
      .then(function(r){ return r.json(); })
      .then(function(data){
        var url = new URL(window.parent.location.href);
        url.searchParams.set('user_ip', data.ip);
        window.parent.location.href = url.toString();
      })
      .catch(function(){
        // Sem IP disponível — segue sem localização
        var url = new URL(window.parent.location.href);
        url.searchParams.set('user_ip', 'unknown');
        window.parent.location.href = url.toString();
      });
  });
</script>
</body></html>
""", height=0)
        # Exibe a página enquanto aguarda o redirecionamento
        cidade = "..."
        estado = "..."

    # Envia para o webhook assim que tiver localização real
    if cidade and cidade != "...":
        _enviar(score, two_fa, label, nome, cidade, estado)

    # ── Renderiza a página de resultado ──────────────────────────────────────
    st.markdown(logo_html(), unsafe_allow_html=True)

    nota_html = (
        f'<p style="font-size:13px;color:#dce8ff;text-align:center;'
        f'margin:4px 0 8px;line-height:1.5;">{nota}</p>'
    ) if nota else ""

    st.markdown(f"""
<div class="card card-logo" style="text-align:center;">

  <div style="font-size:3rem;margin-bottom:6px;">{emoji}</div>

  <p style="font-size:22px;font-weight:900;color:#1a237e;margin:0 0 4px;letter-spacing:.5px;">
    {titulo}
  </p>
  <p style="font-size:35px;font-weight:900;color:#1a73e8;margin:0 0 14px;">
    {nome}
  </p>

  <p class="body-text">{msg1}</p>
  <p class="body-text">{msg2}</p>

  <div class="spacer"></div>

  <p style="font-size:15px;font-weight:700;color:#1a237e;margin:14px 0 4px;">SEU PLACAR</p>
  <p style="font-size:2.4rem;font-weight:900;color:#1a73e8;margin:0 0 8px;">
    {score}/5
  </p>
  <p style="font-size:13px;color:#888;margin:0;">Agradecemos sua participação!</p>

</div>
{nota_html}
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("REFAZER", key="btn_refazer", use_container_width=True):
            st.session_state.resultado_enviado = False
            st.session_state.pop("geo_cidade", None)
            st.session_state.pop("geo_estado", None)
            for k, v in DEFAULTS.items():
                st.session_state[k] = v
            st.rerun()
    with col2:
        if st.button("FINALIZAR", key="btn_finalizar", use_container_width=True):
            st.session_state.page = "finalizado"
            st.rerun()
