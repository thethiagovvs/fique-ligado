"""
Banco de emails para o quiz — organizado por grupos de dificuldade crescente.

Grupo 1 — Spam genérico          (3 itens, todos FALSOS)
Grupo 2 — Urgência / imediatismo  (4 itens, 2 FALSOS + 2 VERDADEIROS)
Grupo 3 — Personalizado com nome  (4 itens, 2 FALSOS + 2 VERDADEIROS)
Grupo 4 — Sofisticado             (4 itens, 2 FALSOS + 2 VERDADEIROS)
Grupo 5 — Engenharia visual       (3 itens, todos FALSOS)
"""

QUIZ_ITEMS = [

    # ═══════════════════════════════════════════════════════════════════
    # GRUPO 1 — SPAM GENÉRICO  |  todos FALSOS
    # Erros leves de português, telefones suspeitos, IDs de transação
    # ═══════════════════════════════════════════════════════════════════
    {
        'grupo': 1,
        'titulo': 'Confirmação de Renovação — Webroot SafeCore',
        'remetente': 'billing@webroot-membros.com',
        'avatar_text': 'W',
        'avatar_color': '#00BCD4',
        'data': 'Hoje 09:41',
        'corpo': 'Prezado Cliente,\n\nSua assinatura foi renovada com exito. O valor de R$ 487,90 sera debitado automaticamente.\n\nCaso não reconheça esta compra, entre em contato: { 0800 942-3371 }\n\nID Transação: 1045-379-5439\nDuração: 60 Meses\n\nWebroot LLC. Todos direitos reservados.',
        'link': 'http://webroot-membros.com/cancelar',
        'verdadeiro': False,
        'explicacao': 'FALSO: Domínio não oficial. Erros de português ("com exito", "sera"), formato suspeito com ID de transação e telefone entre chaves são sinais clássicos de spam.'
    },
    {
        'grupo': 1,
        'titulo': 'Alerta: Vírus Detectado no Seu Dispositivo!',
        'remetente': 'suporte@microsoft-protecao.com',
        'avatar_text': 'M',
        'avatar_color': '#0078D4',
        'data': 'Hoje 11:20',
        'corpo': 'Detectamos atividade suspeita no seu computador.\n\nUm virus foi encontrado e pode comprometer seus dados bancarios.\n\nPara remover imediatamente, ligue agora:\n{ 0800 721-4456 }\n\nNão desligue seu computador.\n\nMicrosoft Suporte Tecnico',
        'link': 'http://microsoft-protecao.com/remover-virus',
        'verdadeiro': False,
        'explicacao': 'FALSO: A Microsoft nunca envia alertas pedindo para ligar por telefone. Domínio não oficial, erros ortográficos ("virus", "bancarios") e tom alarmista são sinais de golpe.'
    },
    {
        'grupo': 1,
        'titulo': 'Seu pedido Amazon foi confirmado — Pagamento aprovado',
        'remetente': 'noreply@amazon-pedidos.net',
        'avatar_text': 'A',
        'avatar_color': '#FF9900',
        'data': 'Ontem 22:15',
        'corpo': 'Obrigado pela sua compra!\n\nProduto: Echo Dot 5ª Geração\nValor cobrado: R$ 619,00\nFormato pagamento: Cartão terminado em 4521\n\nCaso não reconhece esta compra, acesse o link para cancelar:\n\n[CANCELAR PEDIDO AGORA]\n\nAmazon do Brasil Servicos.',
        'link': 'http://amazon-pedidos.net/cancelar-compra',
        'verdadeiro': False,
        'explicacao': 'FALSO: Domínio suspeito (.net), erro gramatical ("não reconhece"), e a Amazon sempre usa amazon.com.br nos e-mails oficiais.'
    },

    # ═══════════════════════════════════════════════════════════════════
    # GRUPO 2 — URGÊNCIA / IMEDIATISMO  |  2 FALSOS + 2 VERDADEIROS
    # Linguagem de pressão; verdadeiros usam urgência real, sem contagem regressiva
    # ═══════════════════════════════════════════════════════════════════
    {
        'grupo': 2,
        'titulo': '🔥 ÚLTIMA HORA: iPhone 15 por R$ 1.299 — Só 2 unidades!',
        'remetente': 'ofertas@americanas-blackfriday.net',
        'avatar_text': 'A',
        'avatar_color': '#E53935',
        'data': 'Hoje 08:05',
        'corpo': 'ATENÇÃO! Estoque quase esgotado!\n\nCompre AGORA antes que acabe:\n\niPhone 15 128GB — De R$ 5.499 por R$ 1.299\n\n⏰ Oferta expira em 47 minutos.\n\n[GARANTIR MEU IPHONE AGORA]\n\nAmericanas Promoções',
        'link': 'http://americanas-blackfriday.net/iphone15',
        'verdadeiro': False,
        'explicacao': 'FALSO: Domínio não oficial (.net), preço impossível para um iPhone 15 e contagem regressiva artificial são técnicas clássicas de golpe por pressão.'
    },
    {
        'grupo': 2,
        'titulo': '⚠️ Sua conta foi bloqueada — Confirme seus dados em 2h',
        'remetente': 'seguranca@bradesco-conta.com',
        'avatar_text': 'B',
        'avatar_color': '#CC0000',
        'data': 'Hoje 07:30',
        'corpo': 'Identificamos uma transação suspeita e bloqueamos sua conta preventivamente.\n\nVocê tem 2 horas para confirmar seus dados, caso contrário sua conta será encerrada permanentemente.\n\n[DESBLOQUEAR MINHA CONTA]\n\nBradesco Segurança',
        'link': 'http://bradesco-conta.com/desbloquear',
        'verdadeiro': False,
        'explicacao': 'FALSO: Domínio não oficial. Prazo artificial de 2 horas e ameaça de encerramento permanente são táticas de pressão. Bancos nunca pedem confirmação de dados por e-mail.'
    },
    {
        'grupo': 2,
        'titulo': 'Novo acesso à sua conta Google detectado',
        'remetente': 'no-reply@accounts.google.com',
        'avatar_text': 'G',
        'avatar_color': '#4285F4',
        'data': 'Hoje 03:17',
        'corpo': 'Detectamos um novo acesso à sua Conta Google.\n\nDispositivo: Windows — Chrome\nLocalização: Moscou, Rússia\n\nSe não foi você, proteja sua conta alterando sua senha agora.\n\n[VERIFICAR ATIVIDADE]\n\nEquipe de Segurança do Google',
        'link': 'https://accounts.google.com/signin/activity',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial do Google. Alertas de acesso de locais incomuns são legítimos e importantes — o Google envia exatamente esse tipo de notificação.'
    },
    {
        'grupo': 2,
        'titulo': 'Novo dispositivo conectado à sua conta Nubank',
        'remetente': 'seguranca@nubank.com.br',
        'avatar_text': 'N',
        'avatar_color': '#8A05BE',
        'data': 'Hoje 14:52',
        'corpo': 'Um novo dispositivo acessou sua conta.\n\nDispositivo: Samsung Galaxy A55\nHorário: 14:51 — São Paulo, SP\n\nFoi você? Se não reconhece este acesso, bloqueie pelo app imediatamente.\n\n[FOI EU] [NÃO FUI EU]\n\nNubank Segurança',
        'link': 'https://nubank.com.br/confirmar-dispositivo',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial do Nubank (.com.br). Alertas de novo dispositivo são padrão de segurança e devem ser verificados — especialmente se você não reconhece o aparelho.'
    },

    # ═══════════════════════════════════════════════════════════════════
    # GRUPO 3 — PERSONALIZADO COM NOME  |  2 FALSOS + 2 VERDADEIROS
    # Usa [NOME]; falsos têm domínio parecido mas errado; linguagem formal
    # ═══════════════════════════════════════════════════════════════════
    {
        'grupo': 3,
        'titulo': 'Notificação de Débito Pendente — DETRAN MG',
        'remetente': 'notificacao@detran-digital.org',
        'avatar_text': 'D',
        'avatar_color': '#1565C0',
        'data': 'Hoje 10:03',
        'corpo': 'Prezado(a) [NOME],\n\nIdentificamos passagens de pedágio pendentes vinculadas ao seu veículo.\n\nCaso não regularizadas, o débito será registrado no DETRAN, gerando multa de R$ 195,23 e restrição veicular.\n\n[CONSULTAR DÉBITOS]\n\nAtenciosamente,\nEquipe DETRAN Digital',
        'link': 'http://detran-digital.org/consultar',
        'verdadeiro': False,
        'explicacao': 'FALSO: O DETRAN usa exclusivamente domínio .gov.br, nunca .org. O e-mail usa seu nome e linguagem oficial para parecer legítimo, mas o domínio entrega o golpe.'
    },
    {
        'grupo': 3,
        'titulo': 'Pendência Identificada — Receita Federal',
        'remetente': 'malha-fina@receitafederal.net',
        'avatar_text': 'R',
        'avatar_color': '#1B5E20',
        'data': 'Ontem 16:44',
        'corpo': 'Prezado(a) [NOME],\n\nIdentificamos uma inconsistência na sua Declaração de Imposto de Renda 2025.\n\nPara evitar autuação e multa, regularize sua situação em até 5 dias úteis acessando o link abaixo.\n\n[REGULARIZAR PENDÊNCIA]\n\nAtenciosamente,\nReceita Federal do Brasil',
        'link': 'http://receitafederal.net/malha-fina',
        'verdadeiro': False,
        'explicacao': 'FALSO: A Receita Federal usa apenas .gov.br. O domínio .net é um sinal imediato de golpe, mesmo com linguagem formal, uso do nome e estrutura institucional.'
    },
    {
        'grupo': 3,
        'titulo': 'Seu pedido foi confirmado — Shopee',
        'remetente': 'notificacoes@shopee.com.br',
        'avatar_text': 'S',
        'avatar_color': '#EE4D2D',
        'data': 'Hoje 15:40',
        'corpo': 'Obrigado pela sua compra, [NOME]!\n\nPedido: #SH987654\nValor: R$ 147,90\nStatus: Em separação\n\nAcompanhe sua entrega pelo aplicativo.\n\n[ACOMPANHAR PEDIDO]\n\nAtenciosamente,\nEquipe Shopee Brasil',
        'link': 'https://shopee.com.br/acompanhar-pedido',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial da Shopee (.com.br), linguagem padrão de confirmação com número de pedido real e sem urgência artificial.'
    },
    {
        'grupo': 3,
        'titulo': 'Cadastro realizado com sucesso — Gov.br',
        'remetente': 'nao-responda@gov.br',
        'avatar_text': 'G',
        'avatar_color': '#0D47A1',
        'data': 'Ontem 10:15',
        'corpo': 'Prezado(a) [NOME],\n\nSeu cadastro no Portal Gov.br foi concluído com sucesso.\n\nCPF: ***.***.***-**\nData: 10/04/2026\n\nCaso não tenha realizado este cadastro, acesse os canais oficiais.\n\nAtenciosamente,\nGoverno Federal',
        'link': 'https://gov.br/acessar-conta',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial .gov.br, linguagem institucional sem urgência e CPF parcialmente ocultado — padrão legítimo de comunicações governamentais.'
    },

    # ═══════════════════════════════════════════════════════════════════
    # GRUPO 4 — SOFISTICADO  |  2 FALSOS + 2 VERDADEIROS
    # Difícil de identificar; falsos com domínio enganoso bem elaborado
    # ═══════════════════════════════════════════════════════════════════
    {
        'grupo': 4,
        'titulo': 'Sua fatura de abril está disponível — Itaú',
        'remetente': 'faturas@itau.com.br.conta-digital.com',
        'avatar_text': 'I',
        'avatar_color': '#FF6B00',
        'data': 'Hoje 08:00',
        'corpo': 'Prezado cliente,\n\nSua fatura de abril no valor de R$ 1.847,32 está disponível.\n\nVencimento: 15/04/2026\n\nEvite juros acessando sua fatura pelo link abaixo.\n\n[ACESSAR FATURA]\n\nItaú Unibanco — Atendimento ao Cliente',
        'link': 'https://itau.com.br.conta-digital.com/fatura',
        'verdadeiro': False,
        'explicacao': 'FALSO: O domínio "itau.com.br.conta-digital.com" parece legítimo à primeira vista, mas o domínio real é conta-digital.com. O Itaú usa somente itau.com.br — tudo após o segundo ponto é parte de outro domínio.'
    },
    {
        'grupo': 4,
        'titulo': 'Tentativa de entrega — Correios',
        'remetente': 'rastreio@correios-online.com.br',
        'avatar_text': 'C',
        'avatar_color': '#FF6B35',
        'data': 'Hoje 13:28',
        'corpo': 'Prezado cliente,\n\nTentamos realizar a entrega do seu pacote, mas não havia ninguém no local.\n\nCódigo: BR741852963BR\nNova tentativa: 12/04/2026\n\nConfirme seu endereço para reagendar.\n\n[CONFIRMAR ENDEREÇO]\n\nCorreios — Central de Atendimento',
        'link': 'https://correios-online.com.br/reagendar',
        'verdadeiro': False,
        'explicacao': 'FALSO: O domínio dos Correios é correios.com.br. "Correios-online.com.br" é um domínio diferente criado para enganar. Sempre verifique o domínio antes do primeiro ponto.'
    },
    {
        'grupo': 4,
        'titulo': 'Recibo de pagamento — Netflix',
        'remetente': 'netflix@account.netflix.com',
        'avatar_text': 'N',
        'avatar_color': '#E50914',
        'data': '10/04/2026',
        'corpo': 'Seu pagamento foi processado com sucesso.\n\nPlano: Standard com anúncios\nValor: R$ 39,90\nPróxima cobrança: 10/05/2026\n\nPara gerenciar sua assinatura, acesse sua conta.\n\n[VER DETALHES]\n\nNetflix',
        'link': 'https://account.netflix.com/billing',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial da Netflix (account.netflix.com). Subdomínios como "account." são legítimos quando o domínio principal é netflix.com.'
    },
    {
        'grupo': 4,
        'titulo': 'Acesso incomum detectado — Amazon',
        'remetente': 'security-noreply@amazon.com.br',
        'avatar_text': 'A',
        'avatar_color': '#FF9900',
        'data': 'Hoje 02:34',
        'corpo': 'Detectamos um acesso à sua conta Amazon de um local incomum.\n\nLocalização: Fortaleza, CE\nDispositivo: iPhone — Safari\n\nSe não foi você, recomendamos alterar sua senha.\n\n[REVISAR ATIVIDADE DA CONTA]\n\nAmazon — Equipe de Segurança',
        'link': 'https://www.amazon.com.br/seguranca-conta',
        'verdadeiro': True,
        'explicacao': 'VERDADEIRO: Domínio oficial da Amazon Brasil (amazon.com.br). Alerta de segurança padrão sem pedido de dados sensíveis ou prazo artificial.'
    },

    # ═══════════════════════════════════════════════════════════════════
    # GRUPO 5 — ENGENHARIA VISUAL  |  todos FALSOS
    # Truques homoglíficos: "rn" imita "m", "I" maiúsculo imita "l" minúsculo
    # ═══════════════════════════════════════════════════════════════════
    {
        'grupo': 5,
        'titulo': 'Sua licença Microsoft 365 expira em 48 horas',
        'remetente': 'conta@rnicrosoft.com',
        'avatar_text': 'M',
        'avatar_color': '#0078D4',
        'data': 'Hoje 09:00',
        'corpo': 'Prezado usuário,\n\nSua licença Microsoft 365 vencerá em breve. Para manter acesso ao OneDrive e ao Outlook sem interrupção, renove agora com 30% de desconto exclusivo.\n\nOferta válida por 48 horas.\n\nPlano Anual: R$ 89,90 (de R$ 127,00)\n\n[RENOVAR MINHA LICENÇA]\n\nMicrosoft — Gestão de Conta',
        'link': 'https://rnicrosoft.com/renovar-licenca',
        'verdadeiro': False,
        'explicacao': 'FALSO: O remetente é "rnicrosoft.com" — as letras "rn" juntas imitam visualmente a letra "m", simulando "microsoft.com". Esse truque é chamado de ataque homoglífico e engana até quem lê com atenção.'
    },
    {
        'grupo': 5,
        'titulo': 'Reembolso aprovado — Pedido #AMZ-00192',
        'remetente': 'reembolso@arnazon.com.br',
        'avatar_text': 'A',
        'avatar_color': '#FF9900',
        'data': 'Hoje 11:15',
        'corpo': 'Olá,\n\nSeu reembolso referente ao pedido cancelado foi aprovado e será processado em até 7 dias úteis.\n\nPedido: #AMZ-00192\nValor: R$ 312,40\nDestino: Cartão de crédito cadastrado\n\nPara acompanhar o status ou contestar o valor, acesse o link abaixo.\n\n[ACOMPANHAR REEMBOLSO]\n\nArnazon Brasil — Central do Cliente',
        'link': 'https://arnazon.com.br/reembolso',
        'verdadeiro': False,
        'explicacao': 'FALSO: O domínio é "arnazon.com.br" — novamente as letras "rn" imitam o "m" de "amazon". Reembolsos legítimos da Amazon sempre vêm de amazon.com.br.'
    },
    {
        'grupo': 5,
        'titulo': 'Transferência iniciada na sua conta PayPal',
        'remetente': 'servico@paypaI.com.br',
        'avatar_text': 'P',
        'avatar_color': '#003087',
        'data': 'Hoje 16:07',
        'corpo': 'Prezado cliente,\n\nUma transferência de R$ 750,00 foi iniciada da sua conta PayPal.\n\nBeneficiário: Conta Desconhecida\nData/Hora: 11/04/2026 às 16:05\n\nCaso não reconheça esta operação, suspenda sua conta imediatamente para evitar a conclusão da transferência.\n\n[SUSPENDER MINHA CONTA]\n\nPayPal — Segurança e Proteção',
        'link': 'https://paypaI.com.br/suspender-conta',
        'verdadeiro': False,
        'explicacao': 'FALSO: O domínio usa "I" maiúsculo no lugar do "l" minúsculo em "PayPal", criando "paypaI.com.br". Além disso, o PayPal não tem versão .com.br — o domínio oficial é paypal.com.'
    },
]
