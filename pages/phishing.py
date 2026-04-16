import streamlit as st


def page_phishing() -> None:
    st.markdown('<p class="page-title" style="font-size:22px;">🎣 PHISHING</p>', unsafe_allow_html=True)

    nome = st.session_state.get("user_name", "Usuário")

    st.markdown(f"""
<div class="card card-content">
  <p class="body-text" style="text-align:center;font-size:15px;margin-bottom:14px;">
    <strong><em>Phishing</em></strong> é uma técnica de golpe em que criminosos enviam
    e-mails ou mensagens fingindo ser empresas confiáveis. Em alguns casos,
    os criminosos já possuem informações suas, isso é conhecido como
    <strong><em>spear phishing</em></strong>, quando o golpe é
    <strong>personalizado</strong> com dados reais para parecer mais convincente.
  </p>

  <p class="section-title" style="margin-top:10px;">Exemplo real:</p>
  <div class="email-demo">
    <div class="email-field"><span>De:</span> seguranca@banco-seguro.com</div>
    <div class="email-field"><span>Assunto:</span> Conta bloqueada</div>
    <div class="email-body">
      Prezado(a) <strong>{nome}</strong>,<br>
      Identificamos uma atividade suspeita em sua conta. Para evitar
      o bloqueio, confirme seus dados imediatamente acessando o link abaixo:
    </div>
    <div class="email-link">http://www.linkfalso.com.biz</div>
  </div>

  <p class="body-text" style="text-align:center;margin-top:10px;">
    O simples fato de acessar esse link pode colocar você em risco. Seus dados
    podem ser roubados, sua conta pode ser comprometida e até prejuízos
    financeiros podem acontecer.
  </p>

  <p class="section-title">🔍 Como identificar phishing:</p>
  <ul class="clean-list">
    <li>Verifique o <strong>domínio</strong> do e-mail</li>
    <li>Desconfie de mensagens com <strong>urgência</strong> excessiva</li>
    <li>Evite clicar em <strong>links suspeitos</strong></li>
    <li>Acesse o site digitando o endereço <strong>manualmente</strong></li>
  </ul>
</div>
""", unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_phish", use_container_width=True):
        st.session_state.page = "senhas"
        st.rerun()
