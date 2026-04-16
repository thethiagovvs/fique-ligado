import streamlit as st


def page_phishing() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;font-weight:800;text-align:center;color:#fff;margin:8px 0 12px;">🎣 PHISHING</p>', unsafe_allow_html=True)

    nome = st.session_state.get("user_name", "Usuário")

    st.markdown(f"""
<div class="card">

  <p class="body-text" style="text-align:center;">
    <strong><em>Phishing</em></strong> é um tipo de golpe em que criminosos enviam
    e-mails ou mensagens fingindo ser empresas confiáveis para roubar seus dados.
    Quando utilizam informações reais, como seu nome, o golpe é chamado de
    <strong><em>spear phishing</em></strong>.
  </p>

  <p class="section-title">Exemplo real:</p>
  <div class="email-demo">
    <div class="email-field"><span>De:</span> seguranca@banco-seguro.com</div>
    <div class="email-field"><span>Assunto:</span> Conta bloqueada</div>
    <div class="email-body">
      Prezado(a) <strong>{nome}</strong>,<br>
      Identificamos atividade suspeita. Confirme seus dados
      acessando o link abaixo:
    </div>
    <div class="email-link">www.linkfalso.com.biz</div>
  </div>

  <p class="body-text" style="text-align:center;">
    Acessar esse link pode resultar em <strong>roubo de dados</strong>
    e até prejuízos financeiros.
  </p>

  <div class="spacer"></div>

  <p class="section-title">🔍 Como identificar:</p>
  <ul class="clean-list">
    <li>Verifique o <strong>domínio</strong> do e-mail</li>
    <li>Desconfie de mensagens com <strong>urgência</strong> excessiva</li>
    <li>Nunca clique em links suspeitos</li>
    <li>Acesse sites digitando o endereço manualmente</li>
  </ul>

</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_phish", use_container_width=True):
        st.session_state.page = "senhas"
        st.rerun()
