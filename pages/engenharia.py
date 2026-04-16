import streamlit as st


def page_engenharia() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;">🎭 ENGENHARIA SOCIAL</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card card-content">
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:14px;">
    <strong>Engenharia social</strong> é a prática de manipular pessoas
    para obter informações confidenciais.
  </p>

  <div class="box-blue" style="margin-bottom:14px;">
    <strong>Os criminosos utilizam diferentes abordagens, como:</strong><br>
    Ligações telefônicas · Mensagens via WhatsApp ou SMS · E-mails fraudulentos · Redes sociais
    <br><br>
    <strong>E costumam se passar por:</strong><br>
    Bancos · Entregadores · Parentes · Empresas
  </div>

  <p class="section-title">🛡️ Como se proteger:</p>
  <ul class="clean-list" style="margin-bottom:14px;">
    <li>Evite tomar decisões com <strong>pressa</strong> ou <strong>sob pressão</strong></li>
    <li>Desconfie de mensagens que exigem <strong>ação imediata</strong></li>
    <li>Verifique a identidade de quem entrou em contato</li>
    <li>Evite clicar em <strong>links suspeitos</strong></li>
    <li>Desconfie de ofertas <strong>muito vantajosas</strong></li>
    <li><strong>Nunca</strong> compartilhe códigos de verificação</li>
  </ul>

  <div class="box-blue" style="text-align:center;">
    <strong>Cenário Atual:</strong><br>
    Cerca de <strong>72%</strong> dos brasileiros receberam tentativas de golpe via WhatsApp.<br>
    Prejuízo médio: <strong>R$ 1.100</strong> por vítima.<br>
    <span class="small-text">Fonte: Mobile Time/Opinion Box (2024) e Fórum Brasileiro de Segurança Pública</span>
  </div>
</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_eng", use_container_width=True):
        st.session_state.page = "phishing"
        st.rerun()
