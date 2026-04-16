import streamlit as st


def page_senhas() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;">🔑 ENTROPIA DE SENHAS</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="card card-content">
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:14px;">
    A senha é a <strong>principal</strong> proteção das suas contas.
    Quanto mais longa e imprevisível ela for, mais <strong>difícil</strong>
    será para um criminoso descobrir.
  </p>

  <div class="box-blue" style="margin-bottom:12px;">
    <div class="stat-row">
      <div class="stat-badge">66%</div>
      <div class="stat-text">
        Cerca de <strong>66% dos brasileiros</strong> utilizam a mesma senha
        em diferentes serviços online. É como usar a mesma chave para todas
        as portas da sua casa: se alguém tiver acesso a uma delas, poderá
        acessar todas.
      </div>
    </div>
  </div>

  <div class="box-blue" style="margin-bottom:14px;">
    <div class="stat-row">
      <div class="stat-badge">80%</div>
      <div class="stat-text">
        Cerca de <strong>80% das senhas criadas</strong> no Brasil são
        consideradas fracas e fáceis de adivinhar, muitas delas baseadas
        em dados pessoais como nome, data de nascimento ou nome de pets.
      </div>
    </div>
  </div>

  <p class="section-title">💡 Dicas para criar uma senha forte:</p>
  <ul class="clean-list">
    <li>Use senhas com <strong>12 a 16 caracteres</strong></li>
    <li>Combine letras <strong>maiúsculas</strong> e <strong>minúsculas</strong></li>
    <li>Inclua <strong>números</strong> e <strong>caracteres especiais</strong></li>
    <li><strong>Não</strong> use informações pessoais</li>
    <li><strong>Não</strong> reutilize a mesma senha</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_senhas", use_container_width=True):
        st.session_state.page = "twofactor"
        st.rerun()
