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
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:16px;">
    Esta é uma ferramenta educativa desenvolvida por um
    estudante de <strong>Segurança da Informação</strong>, com o objetivo
    de orientar sobre os principais riscos digitais e oferecer
    <strong>testes práticos</strong> que ajudam você a se preparar para os
    desafios do dia a dia.
  </p>
  <p style="font-size:14px;color:#1565c0;text-align:center;line-height:1.7;margin:0 0 24px;">
    Seu aprendizado é totalmente <strong>voluntário</strong>, e seus
    resultados poderão ser utilizados para relatório de
    atividade acadêmica.
  </p>
  <p class="body-text" style="font-size:15px;margin-bottom:8px;">
    Antes de começarmos, como podemos te chamar?
  </p>
</div>
""", unsafe_allow_html=True)

    if st.session_state.input_error:
        st.markdown('<p style="color:#e53935;font-size:13px;text-align:center;margin:2px 0 4px;">⚠️ Digite seu nome para continuar.</p>', unsafe_allow_html=True)

    name = st.text_input("nome", key="welcome_name", label_visibility="collapsed",
                         placeholder="Digite seu nome", on_change=_clear_error)

    if st.session_state.input_error:
        st.markdown('<style>div[data-testid="stTextInput"] input{border-color:#e53935 !important;}</style>', unsafe_allow_html=True)

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
