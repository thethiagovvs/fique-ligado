import streamlit as st
import requests
from urllib.parse import unquote
from datetime import datetime
import streamlit.components.v1 as components
from pages.utils import DEFAULTS, logo_html

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwpnrMS3XP3YUVQkcK8C56ml7rdc-oUTUMKk5aLtWvVwKPrXLUN0k-gZar7KALVjMW2/exec"

DOIS_FA_LABEL = {
    "nao":                 "Nao conhece",
    "sim_conheco_nao_uso": "Conhece mas nao usa",
    "sim_utilizo":         "Utiliza",
}

# (emoji, titulo, label_webhook, msg1, msg2, mostrar_botao_dicas)
VARIANTES = {
    "expert": (
        "🎉", "PARABÉNS,", "EXPERT",
        "Você é um verdadeiro <strong>expert</strong> em segurança digital! "
        "Acertou todos os golpes e já utiliza a Autenticação de Dois Fatores.",
        "Continue assim e compartilhe com <strong>amigos</strong> e "
        "<strong>familiares</strong>. Juntos tornamos a internet mais segura!",
        False
    ),
    "bom": (
        "👍", "MANDOU BEM,", "BOM",
        "Você tem <strong>ótima</strong> capacidade de identificar golpes por e-mail.",
        "Que tal ativar a <strong>Autenticação de Dois Fatores</strong>? "
        "Com ela você bloqueia <strong>99,9%</strong> dos ataques.",
        True
    ),
    "atencao": (
        "💡", "BOM TRABALHO,", "ATENCAO",
        "Você já utiliza a Autenticação de Dois Fatores, o que é <strong>excelente!</strong>",
        "Ainda dá para melhorar na identificação de e-mails falsos. "
        "Revise as dicas sobre remetentes suspeitos e links enganosos.",
        True
    ),
    "estudar": (
        "📚", "HORA DE ESTUDAR,", "ESTUDAR",
        "Você identificou alguns golpes, mas ainda pode <strong>melhorar</strong>.",
        "Revise <strong>Phishing</strong> e <strong>Engenharia Social</strong>, "
        "ative o <strong>2FA</strong> e pratique identificar e-mails suspeitos.",
        True
    ),
    "cuidado": (
        "⚠️", "CUIDADO,", "CUIDADO",
        "Você está <strong>vulnerável</strong> aos golpes digitais.",
        "Revise todo o conteúdo, ative a <strong>Autenticação de Dois Fatores</strong> "
        "urgentemente e nunca clique em links suspeitos.",
        True
    ),
}


def _variante(score: int, two_fa: str) -> str:
    if score >= 5 and two_fa == "sim_utilizo":  return "expert"
    if score >= 4 and two_fa != "sim_utilizo":  return "bom"
    if score >= 3 and two_fa == "sim_utilizo":  return "atencao"
    if score >= 3 and two_fa != "sim_utilizo":  return "estudar"
    return "cuidado"


def _geo_por_ip(ip: str) -> tuple:
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        d = r.json()
        return d.get("city", "Desconhecida"), d.get("region", "Desconhecido")
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
    emoji, titulo, label, msg1, msg2, mostrar_dicas = VARIANTES[key]

    # ── Geolocalização via IP real do usuário ─────────────────────────────────
    user_ip = unquote(st.query_params.get("user_ip", ""))
    if user_ip:
        st.query_params.clear()
        if not st.session_state.get("geo_cidade"):
            cidade, estado = _geo_por_ip(user_ip)
            st.session_state.geo_cidade = cidade
            st.session_state.geo_estado = estado

    cidade = st.session_state.get("geo_cidade", "")
    estado = st.session_state.get("geo_estado", "")

    if not cidade:
        components.html("""
<script>
fetch('https://api.ipify.org?format=json')
  .then(r => r.json())
  .then(data => {
    var url = new URL(window.parent.location.href);
    url.searchParams.set('user_ip', data.ip);
    window.parent.location.href = url.toString();
  })
  .catch(() => {
    fetch('https://api64.ipify.org?format=json')
      .then(r => r.json())
      .then(data => {
        var url = new URL(window.parent.location.href);
        url.searchParams.set('user_ip', data.ip);
        window.parent.location.href = url.toString();
      })
      .catch(() => {
        var url = new URL(window.parent.location.href);
        url.searchParams.set('user_ip', 'unknown');
        window.parent.location.href = url.toString();
      });
  });
</script>
""", height=0)
        cidade = "..."
        estado = "..."

    if cidade and cidade != "...":
        _enviar(score, two_fa, label, nome, cidade, estado)

    # ── CSS extra: botão VER DICAS ────────────────────────────────────────────
    st.markdown("""
<style>
div[data-testid="stButton"][st-key="btn_dicas"] > button {
    background: #1565c0 !important;
}
div[data-testid="stButton"][st-key="btn_dicas"] > button:hover {
    background: #0d47a1 !important;
}
</style>
""", unsafe_allow_html=True)

    st.markdown(logo_html(), unsafe_allow_html=True)

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
""", unsafe_allow_html=True)

    if mostrar_dicas:
        if st.button("📚 VER DICAS DE SEGURANÇA", key="btn_dicas", use_container_width=True):
            st.session_state.page = "dicas"
            st.rerun()

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
