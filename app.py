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
from pages.dicas      import page_dicas

st.set_page_config(
    page_title="Fique Ligado",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(BASE_CSS, unsafe_allow_html=True)

# Âncora invisível no topo — o JS faz scroll até ela a cada rerun
st.markdown('<div id="topo-pagina"></div>', unsafe_allow_html=True)

components.html("""
<script>
  function irAoTopo() {
    try {
      var ancora = window.parent.document.getElementById('topo-pagina');
      if (ancora) {
        ancora.scrollIntoView({ behavior: 'instant', block: 'start' });
        return;
      }
    } catch(e) {}
    try { window.parent.scrollTo(0, 0); } catch(e) {}
    try { window.scrollTo(0, 0); } catch(e) {}
  }
  irAoTopo();
  setTimeout(irAoTopo, 100);
  setTimeout(irAoTopo, 300);
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
elif p == "dicas":      page_dicas()
elif p == "finalizado":
    st.balloons()
    st.stop()
