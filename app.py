import streamlit as st
import streamlit.components.v1 as components
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

# Scroll para o topo — atinge window, parent e o container interno do Streamlit
components.html("""
<script>
  function scrollTop() {
    try { window.scrollTo(0, 0); } catch(e) {}
    try { window.parent.scrollTo(0, 0); } catch(e) {}
    try {
      var p = window.parent.document;
      var targets = [
        p.querySelector('[data-testid="stAppViewBlockContainer"]'),
        p.querySelector('[data-testid="stAppViewContainer"]'),
        p.querySelector('.main'),
        p.querySelector('.block-container'),
        p.documentElement,
        p.body
      ];
      targets.forEach(function(el) {
        if (el) { el.scrollTop = 0; el.scrollTo && el.scrollTo(0, 0); }
      });
    } catch(e) {}
  }
  scrollTop();
  setTimeout(scrollTop, 80);
  setTimeout(scrollTop, 200);
</script>
""", height=0)

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
