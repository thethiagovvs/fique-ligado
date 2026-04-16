import streamlit as st


def page_twofactor() -> None:
    st.markdown("""
<p class="page-title" style="font-size:clamp(16px,4.5vw,22px);">
  🔐 AUTENTICAÇÃO DE DOIS FATORES
</p>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

  <p class="body-text" style="text-align:center;">
    A <strong>Autenticação de Dois Fatores</strong> adiciona uma segunda
    verificação além da senha. Essa confirmação extra pode ser feita por
    meio de um código enviado por SMS, e-mail ou gerado em um aplicativo.
  </p>

  <div class="box-blue">
    <p style="font-weight:700;text-align:center;margin:0 0 8px;font-size:15px;">Como funciona</p>
    <p style="margin:4px 0;font-size:14px;">1. Você digita sua senha normalmente</p>
    <p style="margin:4px 0;font-size:14px;">2. Um <strong>código único</strong> é enviado ao seu celular ou app</p>
    <p style="margin:4px 0;font-size:14px;">3. Você informa o código para concluir o acesso</p>
  </div>

  <p class="body-text" style="text-align:center;margin-top:8px;">
    Mesmo que alguém descubra sua senha, não conseguirá acessar sua conta
    sem essa segunda etapa, o que bloqueia a <strong>maioria</strong> dos ataques automatizados
    dos ataques automatizados, mesmo com senha comprometida.
  </p>

  <p style="font-size:15px;font-weight:700;color:#1a237e;text-align:center;margin:14px 0 4px;">
    Você já conhecia a Autenticação de Dois Fatores?
  </p>

</div>
""", unsafe_allow_html=True)

    if st.button("❌  Não", key="btn_nao", use_container_width=True):
        st.session_state.two_factor_knowledge = "nao"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("⚠️  Sim, mas não utilizo", key="btn_conheco", use_container_width=True):
        st.session_state.two_factor_knowledge = "sim_conheco_nao_uso"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("✅  Sim, e utilizo", key="btn_uso", use_container_width=True):
        st.session_state.two_factor_knowledge = "sim_utilizo"
        st.session_state.page = "qrcode"
        st.rerun()
