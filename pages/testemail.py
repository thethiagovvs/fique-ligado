import streamlit as st
from pages.qrcode import iniciar_quiz
from pages.utils import logo_html


def page_testemail() -> None:
    st.markdown(logo_html(), unsafe_allow_html=True)

    st.markdown("""
<div class="card card-logo">

  <div style="text-align:center;">
    <div style="font-size:3rem;margin-bottom:8px;">✉️</div>
    <p style="font-size:22px;font-weight:800;color:#1a237e;margin:0 0 14px;letter-spacing:.5px;">
      TESTE DE E-MAILS
    </p>
    <p class="body-text">
      Você verá <strong>5 e-mails</strong> com dificuldade crescente.
      Para cada um, indique se é legítimo ou golpe:
    </p>
  </div>

  <div class="spacer"></div>

  <!-- Botões de referência visual -->
  <div style="display:flex;justify-content:center;gap:16px;margin:16px 0 0;">
    <div style="text-align:center;">
      <div style="background:#43a047;color:#fff;font-weight:700;font-size:14px;
        border-radius:8px;padding:10px 22px;">✅ VERDADEIRO</div>
      <p style="font-size:13px;color:#555;margin:5px 0 0;">(legítimo)</p>
    </div>
    <div style="align-self:center;color:#888;font-size:13px;">ou</div>
    <div style="text-align:center;">
      <div style="background:#e53935;color:#fff;font-weight:700;font-size:14px;
        border-radius:8px;padding:10px 22px;">❌ FALSO</div>
      <p style="font-size:13px;color:#555;margin:5px 0 0;">(golpe)</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

    if st.button("INICIAR", key="btn_testemail", use_container_width=True):
        iniciar_quiz()
        st.session_state.page = "quiz"
        st.rerun()
