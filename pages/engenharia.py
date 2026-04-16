import streamlit as st


def page_engenharia() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;font-weight:800;text-align:center;color:#fff;margin:8px 0 12px;">🎭 ENGENHARIA SOCIAL</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">

  <p class="body-text" style="text-align:center;">
    <strong>Engenharia social</strong> é a prática de manipular pessoas
    para obter informações confidenciais.
  </p>

  <div class="box-blue">
    <strong>Criminosos se passam por:</strong><br>
    <div style="text-align:center;margin-top:6px;">Bancos · Entregadores · Parentes · Empresas</div>
    <br>
    <strong>Usando:</strong> ligações, WhatsApp, SMS e e-mails falsos
  </div>

  <p class="section-title">🛡️ Como se proteger:</p>
  <ul class="clean-list">
    <li>Desconfie de <strong>pressão</strong> ou <strong>urgência</strong></li>
    <li>Verifique a identidade de quem entrou em contato</li>
    <li>Nunca compartilhe <strong>códigos de verificação</strong></li>
    <li>Evite clicar em links recebidos por mensagem</li>
  </ul>

  <div class="spacer"></div>

  <div class="box-blue" style="text-align:center;">
    Cerca de <strong>72%</strong> dos brasileiros já receberam tentativas de golpe via WhatsApp.<br>
    O prejuízo médio por vítima é de aproximadamente <strong>R$ 1.100</strong>.<br>
    <span class="small-text">Fonte: Mobile Time/Opinion Box (2024)</span>
  </div>

</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_eng", use_container_width=True):
        st.session_state.page = "phishing"
        st.rerun()
