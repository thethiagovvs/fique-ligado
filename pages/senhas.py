import streamlit as st


def page_senhas() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;font-weight:800;text-align:center;color:#fff;margin:8px 0 12px;">🛡️ ENTROPIA DE SENHAS</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">

  <p class="body-text" style="text-align:center;">
    A senha é sua <strong>principal proteção</strong>. Quanto mais longa
    e imprevisível, mais difícil para um criminoso descobrir.
  </p>

  <div class="spacer"></div>

  <div class="box-blue">
    <div class="stat-row">
      <div class="stat-badge">66%</div>
      <div class="stat-text">
        dos brasileiros usam <strong>a mesma senha</strong> em vários serviços.
        Se uma vazar, todas ficam expostas.
      </div>
    </div>
  </div>

  <div class="box-blue">
    <div class="stat-row">
      <div class="stat-badge">80%</div>
      <div class="stat-text">
        das senhas criadas no Brasil são <strong>fracas</strong>,
        baseadas em nome, data de nascimento ou pet.
      </div>
    </div>
  </div>

  <div class="spacer"></div>

  <p class="section-title">💡 Dicas para uma senha forte:</p>
  <ul class="clean-list">
    <li>Use <strong>12 a 16 caracteres</strong></li>
    <li>Combine letras, <strong>números</strong> e caracteres especiais</li>
    <li><strong>Não</strong> use informações pessoais</li>
    <li><strong>Não</strong> reutilize a mesma senha</li>
  </ul>

  <div class="spacer"></div>

</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_senhas", use_container_width=True):
        st.session_state.page = "twofactor"
        st.rerun()
