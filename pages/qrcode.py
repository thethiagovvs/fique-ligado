import random
import streamlit as st
from quiz_data import QUIZ_ITEMS


def iniciar_quiz():
    grupos = {}
    for item in QUIZ_ITEMS:
        g = item.get('grupo', 1)
        grupos.setdefault(g, []).append(item)
    items = [random.choice(grupos[g]) for g in sorted(grupos.keys())]
    st.session_state.quiz_items         = items
    st.session_state.quiz_index         = 0
    st.session_state.quiz_score         = 0
    st.session_state.quiz_answers       = []
    st.session_state.show_popup         = False
    st.session_state.popup_explanation  = ""
    st.session_state.show_success_popup = False


def page_qrcode() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;font-weight:800;text-align:center;color:#fff;margin:8px 0 12px;">📷 QR CODE</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">

  <p class="body-text" style="text-align:center;">
    Você chegou até aqui por meio de um <strong>QR Code</strong>, não é mesmo?
  </p>

  <div class="spacer"></div>

  <div class="box-yellow">
    <p style="font-weight:700;text-align:center;margin:0 0 8px;font-size:15px;">⚠️ ATENÇÃO</p>
    <p style="margin:0;font-size:14px;line-height:1.65;">
      Embora esta aplicação seja <strong>segura</strong>, nem todo QR Code é confiável.
      Em locais públicos, alguns podem ser alterados para aplicar <strong>golpes</strong>, como:
      sites falsos, páginas de pagamento fraudulentas ou download de arquivos maliciosos.
    </p>
  </div>

  <div class="spacer"></div>

  <p class="section-title">🤳 Como se proteger:</p>
  <ul class="clean-list">
    <li>Evite escanear QR Codes de origem desconhecida</li>
    <li>Verifique o link exibido antes de prosseguir</li>
    <li>Desconfie de promessas como <em>"Wi-Fi grátis"</em></li>
    <li>Nunca informe dados pessoais ou bancários sem certeza</li>
  </ul>

  <div class="spacer"></div>

</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_qr", use_container_width=True):
        st.session_state.page = "testemail"
        st.rerun()
