import streamlit as st
from pages.utils import logo_html

CARDS = [
    ("🔑 Senhas Fortes", """
Sabia que a maioria das pessoas usa senhas que um programa consegue quebrar em segundos?

- **FRACA** (`123456`): Quebrada **instantaneamente**.
- **DADOS PESSOAIS** (`maria1990`): Quebrada em **segundos**. Robôs cruzam informações das suas redes sociais para adivinhar esse tipo de senha.
- **FORTE** (`Gosto#De#Pizza!26`): Demoraria **34 mil anos** para ser decifrada.

Parece uma senha boba, né? Mas esse exemplo é poderoso. O uso de caracteres especiais (`#`, `!`), letras maiúsculas, minúsculas e números em uma frase longa torna o trabalho dos invasores matematicamente impossível.
"""),
    ("☠️ Downloads e Programas Piratas", """
Baixar um programa "de graça" pode sair muito caro.

Arquivos piratas são uma das formas mais comuns de instalar vírus no seu dispositivo — programas que roubam senhas, monitoram tudo que você digita ou bloqueiam seus arquivos pedindo dinheiro para devolver.

**O que fazer:**
- Prefira versões gratuitas de programas conhecidos
- Baixe sempre pelo site oficial
- Desconfie de sites com muitos botões de "Download" — geralmente são armadilhas
"""),
    ("🔗 Links Inseguros", """
Um simples clique em um link errado pode comprometer todas as suas senhas e dados bancários — e você nem vai perceber na hora.

Criminosos criam links que parecem legítimos mas levam a sites falsos. Fique atento:

- `bancobradesco.com` virou `banc0bradesco.com` *(zero no lugar do "o")*
- O link usa encurtador (`bit.ly`) e você não sabe para onde vai
- A mensagem veio por WhatsApp ou SMS com urgência

**Regra de ouro:** na dúvida, não clique. Abra o navegador e acesse o site digitando o endereço você mesmo.
"""),
    ("📶 Wi-Fi Público", """
Redes abertas de shoppings, aeroportos e cafés são convenientes, mas qualquer pessoa conectada na mesma rede pode tentar bisbilhotar o que você está fazendo.

**Evite fazer isso em Wi-Fi público:**
- Acessar aplicativos de banco
- Digitar senhas
- Fazer compras online

**Dica prática:** use os dados móveis do celular para qualquer coisa que envolva dinheiro ou senha. É mais seguro e rápido.
"""),
    ("🤖 Clonagem de Voz com IA", """
Com apenas alguns segundos de áudio, uma IA consegue imitar a voz de qualquer pessoa. Criminosos já usam isso para ligar para familiares fingindo ser você em uma emergência — preso, acidentado — e pedir transferências urgentes.

**Como se proteger:**
- Crie uma **palavra-código** com sua família para confirmar identidade em emergências
- Sempre ligue de volta para o número salvo da pessoa antes de qualquer transferência
- Desconfie quando o pedido vier com urgência e "não conta pra ninguém"
"""),
    ("🛒 Compras em E-commerce", """
Anúncios de produtos com descontos absurdos nas redes sociais são uma das armadilhas mais comuns na internet. Aquele tênis de R$ 800 por R$ 99 pode nunca chegar — ou pior, seus dados do cartão ficam com os criminosos.

**Regra principal:** nunca compre diretamente por um anúncio. Se viu um produto interessante, feche o anúncio, abra o aplicativo ou site oficial da loja e busque o item lá.

**Sinais de alerta:**
- Site desconhecido com preço muito abaixo do mercado
- Só aceita Pix para "pessoa física"
- Avaliações inexistentes ou todas com 5 estrelas e textos genéricos

**Dica:** pesquise o nome da loja seguido de "é confiável" ou "reclamação" antes de qualquer compra.
"""),
    ("📸 Exposição nas Redes Sociais", """
Expor demais sobre sua rotina, hábitos e localização nas redes sociais pode ser um prato cheio para criminosos.

Postar onde você está em tempo real, os lugares que frequenta — academia, bares, restaurantes — ou mostrar que está viajando avisa a todos que sua casa está vazia. Isso pode abrir caminho para roubos, invasões e até sequestros.

Além disso, informações pessoais expostas publicamente são usadas por criminosos para criar golpes mais convincentes direcionados a você.

**Boas práticas:**
- Evite marcar sua localização em tempo real
- Prefira postar fotos de viagens depois que voltar
- Revise quem pode ver suas publicações nas configurações de privacidade
"""),
    ("🆘 O que fazer quando for vítima de um golpe?", """
Ser vítima não é motivo de vergonha. O mais importante é agir rápido.

**1. Bloqueie imediatamente**
Cancele cartões pelo app do banco e troque suas senhas.

**2. Registre o Boletim de Ocorrência**
Faça pela Delegacia Virtual do seu estado, sem sair de casa. Guarde prints e comprovantes.

**3. Notifique o banco**
Informe sobre transações não autorizadas — há prazo para contestação e chance de reaver o dinheiro.

**4. Procure ajuda**
- **safernet.org.br** — denúncias de crimes digitais
- **Procon** do seu estado para golpes de consumo
"""),
    ("⭐ VirusTotal — Verifique antes de clicar", """
O **VirusTotal** é uma ferramenta gratuita que verifica se um link, arquivo ou site é perigoso antes de você abrir.

É simples: acesse **virustotal.com**, cole o link suspeito e em segundos ele mostra se é seguro ou não, consultando dezenas de sistemas de segurança ao mesmo tempo.

**Quando usar:**
- Recebeu um link por WhatsApp e não tem certeza se é seguro
- Quer baixar um arquivo e não sabe se tem vírus
- Desconfia de um site antes de inserir seus dados

É gratuito, não precisa de cadastro e funciona pelo celular.
"""),
]


def page_dicas() -> None:
    if "dica_aberta" not in st.session_state:
        st.session_state.dica_aberta = None

    st.markdown(logo_html(), unsafe_allow_html=True)

    st.markdown("""
<div class="card card-logo" style="min-height:0;padding:20px 20px 16px;">
  <p style="font-size:22px;font-weight:800;color:#1a237e;text-align:center;margin:0 0 6px;">
    📚 SAIBA MAIS
  </p>
  <p class="body-text" style="text-align:center;margin:0;">
    Aprofunde seus conhecimentos em segurança digital.
  </p>
</div>

<style>
/* Botão-cabeçalho do accordion */
div[data-testid="stButton"][st-key^="acc_"] > button {
    background: #1a237e !important;
    color: #fff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    border-radius: 10px !important;
    height: auto !important;
    padding: 12px 16px !important;
    text-align: left !important;
    justify-content: space-between !important;
    white-space: normal !important;
    line-height: 1.4 !important;
}
div[data-testid="stButton"][st-key^="acc_"] > button:hover {
    background: #283593 !important;
}
/* Card de conteúdo aberto */
.acc-body {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-top: none;
    border-radius: 0 0 10px 10px;
    padding: 14px 16px;
    margin-top: -12px;
    margin-bottom: 8px;
    font-size: 15px;
    color: #333;
    line-height: 1.75;
}
/* Botão retornar ao resultado */
div[data-testid="stButton"][st-key="btn_volta_dicas"] > button {
    background: #1976d2 !important;
}
div[data-testid="stButton"][st-key="btn_volta_dicas"] > button:hover {
    background: #1565c0 !important;
}
div[data-testid="stButton"][st-key^="acc_"] {
    margin-bottom: 8px !important;
}
div[data-testid="stButton"][st-key^="acc_"][data-open="true"] {
    margin-bottom: 0 !important;
}
</style>
""", unsafe_allow_html=True)

    for i, (titulo, conteudo) in enumerate(CARDS):
        aberto = st.session_state.dica_aberta == i
        seta = "▲" if aberto else "▼"
        if st.button(f"{titulo}  {seta}", key=f"acc_{i}", use_container_width=True):
            st.session_state.dica_aberta = None if aberto else i
            st.rerun()
        if aberto:
            import re

            CODE = r'<code style="background:#f1f3f4;padding:1px 5px;border-radius:4px;font-size:15px;font-family:monospace;">\1</code>'

            def inline(txt):
                txt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', txt)
                txt = re.sub(r'\*(.+?)\*',     r'<em>\1</em>',          txt)
                txt = re.sub(r'`(.+?)`',        CODE,                    txt)
                return txt

            # Divide em blocos separados por linhas em branco
            blocos = re.split(r'\n{2,}', conteudo.strip())
            partes = []
            for bloco in blocos:
                linhas = bloco.strip().splitlines()
                # Bloco de lista
                if all(l.strip().startswith('- ') for l in linhas if l.strip()):
                    itens = ''.join(
                        f'<li style="margin-bottom:3px;">{inline(l.strip()[2:])}</li>'
                        for l in linhas if l.strip()
                    )
                    partes.append(
                        f'<ul style="padding-left:18px;margin:6px 0 0;">{itens}</ul>'
                    )
                # Bloco misto (começa com texto, pode ter lista depois)
                elif any(l.strip().startswith('- ') for l in linhas):
                    html_bloco = ''
                    dentro = False
                    for l in linhas:
                        if l.strip().startswith('- '):
                            if not dentro:
                                html_bloco += '<ul style="padding-left:18px;margin:4px 0 0;">'
                                dentro = True
                            html_bloco += f'<li style="margin-bottom:3px;">{inline(l.strip()[2:])}</li>'
                        else:
                            if dentro:
                                html_bloco += '</ul>'
                                dentro = False
                            if l.strip():
                                html_bloco += f'<p style="margin:0 0 4px;">{inline(l.strip())}</p>'
                    if dentro:
                        html_bloco += '</ul>'
                    partes.append(html_bloco)
                # Bloco de parágrafo simples
                else:
                    texto = ' '.join(l.strip() for l in linhas if l.strip())
                    partes.append(
                        f'<p style="margin:0 0 4px;">{inline(texto)}</p>'
                    )

            html = ''.join(partes)
            st.markdown(
                f'<div class="acc-body">{html}</div>',
                unsafe_allow_html=True
            )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if st.button("RETORNAR AO RESULTADO", key="btn_volta_dicas", use_container_width=True):
        st.session_state.page = "resultado"
        st.rerun()
