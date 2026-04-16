import streamlit as st
from pages.qrcode import iniciar_quiz
from pages.utils import logo_html


def page_testemail() -> None:
    st.markdown(logo_html(), unsafe_allow_html=True)

    st.markdown("""
<div class="card card-logo" style="text-align:center;">
  <div style="font-size:3rem;margin-bottom:8px;">✉️</div>
  <p style="font-size:22px;font-weight:800;color:#1a237e;margin:0 0 14px;letter-spacing:.5px;">
    TESTE DE E-MAILS
  </p>
  <p class="body-text" style="font-size:15px;margin-bottom:20px;">
    Você verá <strong>5 e-mails</strong> com dificuldade crescente.
    Para cada um, indique se é legítimo ou golpe usando os botões abaixo:
  </p>

  <div style="display:flex;justify-content:center;gap:16px;margin:0 0 20px;flex-wrap:wrap;">
    <div style="background:#43a047;color:#fff;font-weight:700;font-size:15px;
      border-radius:8px;padding:12px 24px;text-align:center;min-width:130px;">
      ✅ VERDADEIRO
    </div>
    <div style="background:#e53935;color:#fff;font-weight:700;font-size:15px;
      border-radius:8px;padding:12px 24px;text-align:center;min-width:130px;">
      ❌ FALSO
    </div>
  </div>

  <div style="background:#e8f0fe;border-radius:10px;padding:14px 16px;margin-bottom:14px;">
    <p style="font-size:14px;color:#1a237e;margin:0;line-height:1.6;">
      <strong>Verdadeiro</strong> significa que o e-mail é legítimo.<br>
      <strong>Falso</strong> significa que é um golpe de phishing.
    </p>
  </div>

  <p class="body-text" style="font-size:13px;color:#888;margin:0;">
    Ao final, você receberá um resultado personalizado com base no seu desempenho.
  </p>
</div>
""", unsafe_allow_html=True)

    if st.button("INICIAR", key="btn_testemail", use_container_width=True):
        iniciar_quiz()
        st.session_state.page = "quiz"
        st.rerun()
