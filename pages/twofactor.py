import streamlit as st


def page_twofactor() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;">🔐 AUTENTICAÇÃO DE DOIS FATORES</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card" style="padding:22px 20px 20px;margin-bottom:12px;">
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:14px;">
    O <strong>Autenticação em Dois Fatores (ou 2FA)</strong> adiciona uma camada
    extra de segurança às suas contas. Além da senha, ele exige uma segunda
    verificação para confirmar sua identidade. Assim, mesmo que alguém descubra
    sua senha, não conseguirá acessar sua conta sozinho.
  </p>

  <div class="box-blue" style="margin-bottom:14px;">
    <p style="font-weight:700;text-align:center;margin:0 0 8px;font-size:15px;">Como funciona</p>
    <p style="margin:4px 0;font-size:14px;">1. Você digita sua senha no site ou aplicativo</p>
    <p style="margin:4px 0;font-size:14px;">2. Um <strong>código único</strong> é enviado para seu celular, e-mail ou aplicativo autenticador</p>
    <p style="margin:4px 0;font-size:14px;">3. Você retorna à plataforma e informa o código para concluir o acesso</p>
  </div>

  <p class="body-text" style="text-align:center;margin-bottom:20px;">
    Esse segundo passo confirma que é realmente você tentando entrar,
    dificultando acessos indevidos e bloqueando a maioria dos ataques automatizados.
  </p>

  <p style="font-size:15px;font-weight:700;color:#1a237e;text-align:center;margin:0 0 12px;">
    Você já conhece a Autenticação de Dois Fatores?
  </p>
</div>
""", unsafe_allow_html=True)

    if st.button("❌  Não", key="btn_nao", use_container_width=True):
        st.session_state.two_factor_knowledge = "nao"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("❕  Sim, mas não utilizo", key="btn_conheco", use_container_width=True):
        st.session_state.two_factor_knowledge = "sim_conheco_nao_uso"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("✅  Sim, e utilizo", key="btn_uso", use_container_width=True):
        st.session_state.two_factor_knowledge = "sim_utilizo"
        st.session_state.page = "qrcode"
        st.rerun()
