import streamlit as st
from pages.utils      import DEFAULTS, BASE_CSS
from pages.welcome    import page_welcome
from pages.engenharia import page_engenharia
from pages.phishing   import page_phishing
from pages.senhas     import page_senhas
from pages.twofactor  import page_twofactor
from pages.qrcode     import page_qrcode
from pages.testemail  import page_testemail
from pages.quiz       import page_quiz
from pages.resultado  import page_resultado

st.set_page_config(
    page_title="Fique Ligado",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(BASE_CSS, unsafe_allow_html=True)

# Rola para o topo após o conteúdo renderizar
st.markdown("""
<script>
  setTimeout(function(){
    window.scrollTo({top:0,behavior:'instant'});
    window.parent.scrollTo({top:0,behavior:'instant'});
  }, 50);
</script>
""", unsafe_allow_html=True)

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

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
