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
    st.markdown('<p class="page-title" style="font-size:22px;">📷 QR CODE</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card card-content">
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:14px;">
    Você chegou até aqui por meio de um <strong>QR Code</strong>, não é mesmo?
  </p>

  <div class="box-yellow" style="margin-bottom:14px;">
    <p style="font-weight:700;text-align:center;margin:0 0 8px;font-size:15px;">⚠️ ATENÇÃO</p>
    <p style="margin:0;font-size:14px;line-height:1.6;">
      Embora esta aplicação seja <strong>segura</strong> e tenha um
      <strong>propósito educativo</strong>, nem todo QR Code é confiável.
      Em locais públicos, alguns podem ser alterados ou criados para aplicar
      <strong>golpes</strong>. Ao escanear um código, você pode ser direcionado
      para sites falsos, páginas de pagamento fraudulentas ou até iniciar o
      download de arquivos maliciosos.
    </p>
  </div>

  <p class="section-title">🤳 Como se proteger:</p>
  <ul class="clean-list" style="margin-bottom:14px;">
    <li>Evite escanear QR Codes de origem <strong>desconhecida ou suspeita</strong></li>
    <li>Verifique o <strong>link exibido</strong> antes de prosseguir</li>
    <li>Desconfie de QR Codes que oferecem benefícios exagerados, como <em>"Wi-Fi grátis"</em></li>
    <li>Nunca informe <strong>dados pessoais ou bancários</strong> sem certeza da segurança</li>
  </ul>

  <p class="body-text" style="text-align:center;font-size:13px;color:#888;">
    Esta aplicação é segura. Continue para o teste prático!
  </p>
</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_qr", use_container_width=True):
        st.session_state.page = "testemail"
        st.rerun()
