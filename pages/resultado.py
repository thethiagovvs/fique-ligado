import streamlit as st
import requests
from datetime import datetime
from pages.utils import DEFAULTS, logo_html

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

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
        "Para <strong>mais dicas</strong>, pegue um panfleto e comece sua jornada em segurança digital!"
    ),
    "estudar": (
        "📚", "HORA DE ESTUDAR,", "ESTUDAR",
        "Você identificou alguns golpes, mas ainda pode <strong>melhorar</strong>.",
        "Revise <strong>Phishing</strong> e <strong>Engenharia Social</strong>, "
        "ative o <strong>2FA</strong> e pratique identificar e-mails suspeitos.",
        "Para <strong>mais dicas</strong>, pegue um panfleto e comece sua jornada em segurança digital!"
    ),
    "cuidado": (
        "⚠️", "CUIDADO,", "CUIDADO",
        "Você está <strong>vulnerável</strong> aos golpes digitais.",
        "Revise todo o conteúdo, ative a <strong>Autenticação de Dois Fatores</strong> "
        "urgentemente e nunca clique em links suspeitos.",
        "Para <strong>mais dicas</strong>, pegue um panfleto e comece sua jornada em segurança digital!"
    ),
}


def _variante(score: int, two_fa: str) -> str:
    if score >= 5 and two_fa == "sim_utilizo":  return "expert"
    if score >= 4 and two_fa != "sim_utilizo":  return "bom"
    if score >= 3 and two_fa == "sim_utilizo":  return "atencao"
    if score >= 3 and two_fa != "sim_utilizo":  return "estudar"
    return "cuidado"


def _enviar(score, two_fa, label, nome_completo):
    if st.session_state.get("resultado_enviado", False):
        return
    primeiro = nome_completo.strip().split()[0].capitalize() if nome_completo.strip() else "Anonimo"
    try:
        geo    = requests.get("https://ipapi.co/json/", timeout=4).json()
        cidade = geo.get("city", "Desconhecida")
        estado = geo.get("region_code", "Desconhecido")
    except Exception:
        cidade = estado = "Desconhecido"
    try:
        requests.post(WEBHOOK_URL, json={
            "nome": primeiro,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "cidade": cidade, "estado": estado,
            "score": f"{score}/5",
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

    _enviar(score, two_fa, label, nome)

    st.markdown(logo_html(), unsafe_allow_html=True)

    nota_html = f'<p style="font-size:13px;color:#dce8ff;text-align:center;margin:6px 0 8px;line-height:1.5;">{nota}</p>' if nota else ""

    st.markdown(f"""
<div class="card card-logo" style="text-align:center;">
  <div style="font-size:3rem;margin-bottom:6px;">{emoji}</div>
  <p style="font-size:22px;font-weight:900;color:#1a237e;margin:0 0 6px;letter-spacing:.5px;">
    {titulo}
  </p>
  <p style="font-size:35px;font-weight:700;color:#1a73e8;margin:0 0 14px;">
    {nome}
  </p>
  <p class="body-text">{msg1}</p>
  <p class="body-text">{msg2}</p>

  <p style="font-size:15px;font-weight:700;color:#1a237e;margin:14px 0 4px;">SEU PLACAR</p>
  <p style="font-size:2.2rem;font-weight:900;color:#1a73e8;margin:0 0 8px;">
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
            for k, v in DEFAULTS.items():
                st.session_state[k] = v
            st.rerun()
    with col2:
        if st.button("FINALIZAR", key="btn_finalizar", use_container_width=True):
            st.session_state.page = "finalizado"
            st.rerun()
