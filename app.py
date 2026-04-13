import streamlit as st
from urllib.parse import unquote

from pages.utils      import DEFAULTS
from pages.welcome    import page_welcome
from pages.engenharia import page_engenharia
from pages.phishing   import page_phishing
from pages.senhas     import page_senhas
from pages.twofactor  import page_twofactor
from pages.qrcode     import page_qrcode
from pages.testemail  import page_testemail
from pages.quiz       import page_quiz, handle_quiz_answer
from pages.resultado  import page_resultado

st.set_page_config(
    page_title="FIQUE LIGADO",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<meta name="viewport" content="width=450, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
    .stApp { background-color: #1a73e8 !important; }
    .block-container {
        max-width: 450px !important;
        padding: 0 !important;
        margin: 0 auto !important;
    }
    header, footer, #MainMenu { display: none !important; }
    [data-testid="stVerticalBlock"] { position: relative !important; }
    div[data-testid="stButton"],
    div[data-testid="stTextInput"] { margin: 0 !important; padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# COMUNICAÇÃO VIA QUERY_PARAMS
action = unquote(st.query_params.get("action", ""))
if action:
    st.query_params.clear()

    if action.startswith("go_engenharia:"):
        # Extrai nome|cidade|estado se disponível
        partes = action.split(":", 1)[1].split("|")
        st.session_state.user_name   = partes[0]
        st.session_state.user_cidade = partes[1] if len(partes) > 1 else "Desconhecida"
        st.session_state.user_estado = partes[2] if len(partes) > 2 else "Desconhecido"
        st.session_state.page = "engenharia"
        st.rerun()
    elif action == "go_phishing":
        st.session_state.page = "phishing"
        st.rerun()
    elif action == "go_senhas":
        st.session_state.page = "senhas"
        st.rerun()
    elif action == "go_twofactor":
        st.session_state.page = "twofactor"
        st.rerun()
    elif action == "go_qrcode":
        st.session_state.page = "qrcode"
        st.rerun()
    elif action == "go_testemail":
        st.session_state.page = "testemail"
        st.rerun()
    elif action == "go_quiz":
        from pages.qrcode import iniciar_quiz
        iniciar_quiz()
        st.session_state.page = "quiz"
        st.rerun()
    elif action.startswith("2fa:"):
        val_map = {"nao": "nao", "conheco_nao_uso": "sim_conheco_nao_uso", "sim_utilizo": "sim_utilizo"}
        st.session_state.two_factor_knowledge = val_map.get(action.split(":", 1)[1], "nao")
        st.session_state.page = "qrcode"
        st.rerun()
    elif action.startswith("quiz:"):
        handle_quiz_answer(action.split(":", 1)[1] == "verdadeiro")
        st.rerun()
    elif action == "popup_continue":
        st.session_state.show_popup        = False
        st.session_state.popup_explanation = ""
        st.session_state.quiz_index       += 1
        st.rerun()
    elif action == "quiz_success_continue":
        st.session_state.show_success_popup = False
        st.session_state.quiz_index        += 1
        st.rerun()
    elif action == "result:refazer":
        for k, v in DEFAULTS.items():
            st.session_state[k] = v
        st.rerun()
    elif action == "result:finalizar":
        st.session_state.page = "finalizado"
        st.rerun()

# ROTEAMENTO
p = st.session_state.page

if   p == "welcome":    page_welcome()
elif p == "engenharia": page_engenharia()
elif p == "phishing":   page_phishing()
elif p == "senhas":     page_senhas()
elif p == "twofactor":  page_twofactor()
elif p == "qrcode":     page_qrcode()
elif p == "testemail":  page_testemail()
elif p == "quiz":       page_quiz()
elif p == "resultado":  page_resultado()
elif p == "finalizado":
    st.balloons()
    st.stop()
