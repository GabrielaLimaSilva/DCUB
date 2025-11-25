import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Deveria Começar uma Briga?",
    page_icon="💥",
    layout="centered"
)

# Estilo customizado
st.markdown("""
    <style>
    .big-font {
        font-size: 40px !important;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 30px;
    }
    .question-font {
        font-size: 24px !important;
        text-align: center;
        margin-bottom: 40px;
        line-height: 1.6;
    }
    .stButton>button {
        width: 100%;
        height: 80px;
        font-size: 18px !important;
        margin: 10px 0;
    }
    .pontos-box {
        background-color: #FF4B4B;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin: 20px 0;
    }
    .resposta-box {
        background-color: #f0f2f6;
        color: #000000 !important;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        margin: 20px 0;
        border: 2px solid #FF4B4B;
    }
    </style>
""", unsafe_allow_html=True)

# Banco de perguntas
PERGUNTAS = [
    {
        "id": 1,
        "emoji": "🧙‍♂️",
        "texto": "Um mago me colocou no corpo da sua ex e sua ex no meu corpo.<br><br>Para desfazer a maldição, você deve beijar uma.<br><br><strong>Quem você escolhe?</strong>",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "💋 Sua ex no meu corpo", "resposta": "Então ela é mais bonita?"},
            {"texto": "💋 Eu no corpo da sua ex", "resposta": "Então ela é mais legal?"}
        ]
    },
    {
        "id": 2,
        "emoji": "📱",
        "texto": "O que você faria se comentasse num vídeo de uma mulher e ela comentasse com risadinhas?",
        "tipo": "texto",
        "resposta": "Não gostei"
    },
    {
        "id": 3,
        "emoji": "💋",
        "texto": "Meu beijo é o melhor de todos que você já experimentou?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "😍 Sim", "resposta": "Então lembra de todos e tá comparando?"},
            {"texto": "😬 Não", "resposta": "Como assim NÃO???"}
        ]
    },
    {
        "id": 4,
        "emoji": "😢",
        "texto": "Você está triste?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "😔 Sim", "resposta": "Então tá triste me namorando?"},
            {"texto": "😊 Não", "resposta": "Então você tá feliz de estar longe de mim?"}
        ]
    },
    {
        "id": 5,
        "emoji": "🚪",
        "texto": "Você ficaria sozinho com outra mulher que não eu?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "✅ Sim", "resposta": "O que você está fazendo num quarto com outra mulher??"},
            {"texto": "❌ Não", "resposta": "Você tá com medo de ficar com outra mulher por quê??"}
        ]
    },
    {
        "id": 6,
        "emoji": "💰",
        "texto": "Você prefere me beijar ou beijar a mulher mais bonita do mundo por 1 milhão?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "👸 Mulher mais linda", "resposta": "Vai lá com ela então!"},
            {"texto": "❤️ Você", "resposta": "Então não sou a mulher mais linda do mundo?"}
        ]
    },
    {
        "id": 7,
        "emoji": "🙏",
        "texto": "Desculpas por estar te perturbando muito esses dias.",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "✅ Desculpo", "resposta": "Ahh então eu tava te perturbando??"},
            {"texto": "❌ Não desculpo", "resposta": "Então não aguenta minhas perturbações??"}
        ]
    },
    {
        "id": 8,
        "emoji": "🗽",
        "texto": "Você prefere ter liberdade ou ter eu?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "🕊️ Liberdade", "resposta": "Eu te prendo então?"},
            {"texto": "❤️ Você", "resposta": "Então 'eu' significa não ter liberdade?"}
        ]
    },
    {
        "id": 9,
        "emoji": "🪟",
        "texto": "O que você faria se tivesse eu, tua ex e você no seu apartamento e as duas caíssem pela janela?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "🦸 Salvaria você", "resposta": "O que sua ex tá fazendo no seu apartamento??"},
            {"texto": "🦸 Salvaria minha ex", "resposta": "Vai lá com ela então!"}
        ]
    },
    {
        "id": 10,
        "emoji": "🤔",
        "texto": "Seu tipo é mulher feia?",
        "tipo": "botoes",
        "opcoes": [
            {"texto": "✅ Sim", "resposta": "Então eu sou feia!"},
            {"texto": "❌ Não", "resposta": "Então suas ex são bonitas?"}
        ]
    }
]

# Inicializar estado da sessão
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
if 'pergunta_atual' not in st.session_state:
    st.session_state.pergunta_atual = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0
if 'resposta_texto' not in st.session_state:
    st.session_state.resposta_texto = ""
if 'mostrar_resposta' not in st.session_state:
    st.session_state.mostrar_resposta = False

# Funções
def ir_para_pergunta():
    st.session_state.tela = 'pergunta'
    st.session_state.pergunta_atual = 0
    st.session_state.pontos = 0
    st.session_state.mostrar_resposta = False

def proxima_pergunta():
    st.session_state.pergunta_atual += 1
    st.session_state.mostrar_resposta = False
    st.session_state.resposta_texto = ""
    if st.session_state.pergunta_atual >= len(PERGUNTAS):
        st.session_state.tela = 'final'

def mostrar_resultado(resposta_texto):
    st.session_state.pontos -= 5
    st.session_state.resposta_texto = resposta_texto
    st.session_state.mostrar_resposta = True

# TELA INICIAL
if st.session_state.tela == 'inicio':
    st.markdown('<p class="big-font">💥 DEVERIA COMEÇAR UMA BRIGA? 💥</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("▶️ COMEÇAR", key="btn_start", use_container_width=True):
            ir_para_pergunta()
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>⚠️ Jogue por sua conta e risco!</p>", unsafe_allow_html=True)

# TELA DE PERGUNTAS
elif st.session_state.tela == 'pergunta':
    pergunta = PERGUNTAS[st.session_state.pergunta_atual]
    
    # Cabeçalho
    st.markdown(f'<p class="big-font">{pergunta["emoji"]} PERGUNTA {pergunta["id"]}/10</p>', unsafe_allow_html=True)
    
    # Pontuação atual
    st.markdown(f'<div class="pontos-box">PONTOS: {st.session_state.pontos}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Pergunta
    st.markdown(f'<p class="question-font">{pergunta["texto"]}</p>', unsafe_allow_html=True)
    
    # Se já respondeu, mostra a resposta
    if st.session_state.mostrar_resposta:
        st.markdown(f'<div class="resposta-box">😤 {st.session_state.resposta_texto}</div>', unsafe_allow_html=True)
        st.markdown('<div class="pontos-box">-5 PONTOS! 💥</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("➡️ PRÓXIMA PERGUNTA", key="btn_next", use_container_width=True):
                proxima_pergunta()
                st.rerun()
    
    # Tipo de pergunta: botões
    elif pergunta["tipo"] == "botoes":
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(pergunta["opcoes"][0]["texto"], key="opcao1", use_container_width=True):
                mostrar_resultado(pergunta["opcoes"][0]["resposta"])
                st.rerun()
        
        with col2:
            if st.button(pergunta["opcoes"][1]["texto"], key="opcao2", use_container_width=True):
                mostrar_resultado(pergunta["opcoes"][1]["resposta"])
                st.rerun()
    
    # Tipo de pergunta: texto livre
    elif pergunta["tipo"] == "texto":
        resposta_usuario = st.text_area("Digite sua resposta:", key="txt_resposta", height=100)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✅ ENVIAR RESPOSTA", key="btn_enviar", use_container_width=True):
                if resposta_usuario.strip():
                    mostrar_resultado(pergunta["resposta"])
                    st.rerun()
                else:
                    st.error("Digite algo primeiro!")

# TELA FINAL
elif st.session_state.tela == 'final':
    st.markdown('<p class="big-font">🔥 RESULTADO FINAL 🔥</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f'<div class="pontos-box">PONTUAÇÃO TOTAL: {st.session_state.pontos} PONTOS</div>', unsafe_allow_html=True)
    
    st.markdown('''
        <p class="question-font">
        <strong>VOU COMEÇAR UMA BRIGA! 💥</strong>
        <br><br>
        Você conseguiu -50 pontos respondendo todas as perguntas!
        <br><br>
        Amo você meu amorrr <3
        </p>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 JOGAR NOVAMENTE", key="btn_restart", use_container_width=True):
            st.session_state.tela = 'inicio'
            st.session_state.pergunta_atual = 0
            st.session_state.pontos = 0
            st.session_state.mostrar_resposta = False
            st.rerun()
