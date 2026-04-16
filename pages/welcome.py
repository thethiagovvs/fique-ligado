import streamlit as st
from pages.utils import logo_html


def page_welcome() -> None:
    if "input_error" not in st.session_state:
        st.session_state.input_error = False

    st.markdown(logo_html(), unsafe_allow_html=True)

    st.markdown("""
<div class="card card-logo">

  <h2 style="text-align:center;font-size:22px;font-weight:800;color:#1a237e;margin:0 0 16px;">
    Olá! Seja bem-vindo(a).
  </h2>

  <p class="body-text" style="text-align:center;">
    Esta é uma ferramenta educativa desenvolvida por um estudante de
    <strong>Segurança da Informação</strong>, com o objetivo de orientar sobre
    os principais riscos digitais e oferecer testes práticos que ajudam você
    a se preparar para os desafios do dia a dia.
  </p>

  <div class="box-blue" style="text-align:center;margin:14px 0;">
    <br>
    Sua participação é <strong>voluntária</strong>.<br>
    Os resultados podem ser usados em relatório acadêmico.
    <br><br>
  </div>

  <div class="spacer"></div>

  <p class="body-text" style="margin-bottom:6px;text-align:center;">
    Antes de começarmos, como podemos te chamar?
  </p>

</div>
""", unsafe_allow_html=True)

    if st.session_state.input_error:
        st.markdown('<p style="color:#e53935;font-size:13px;text-align:center;margin:2px 0 4px;">⚠️ Digite seu nome para continuar.</p>', unsafe_allow_html=True)
        st.markdown('<style>div[data-testid="stTextInput"] input{border-color:#e53935 !important;}</style>', unsafe_allow_html=True)

    name = st.text_input("nome", key="welcome_name", label_visibility="collapsed",
                         placeholder="Digite seu nome", on_change=_clear_error)

    if st.button("CONTINUAR", key="btn_welcome", use_container_width=True):
        limpo = ''.join(c for c in (name or '') if not c.isdigit()).strip()
        if len(limpo) >= 2:
            st.session_state.user_name   = name.strip()
            st.session_state.input_error = False
            st.session_state.page        = "engenharia"
            st.rerun()
        else:
            st.session_state.input_error = True
            st.rerun()


def _clear_error():
    st.session_state.input_error = False
