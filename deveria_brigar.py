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
    </style>
""", unsafe_allow_html=True)

# Inicializar estado da sessão
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Função para mudar de tela
def ir_para_pergunta():
    st.session_state.tela = 'pergunta1'

def registrar_resposta(pergunta, resposta):
    st.session_state.respostas[pergunta] = resposta
    st.session_state.tela = 'resultado'

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

# TELA DA PERGUNTA 1
elif st.session_state.tela == 'pergunta1':
    st.markdown('<p class="big-font">🧙‍♂️ PERGUNTA 1</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('''
        <p class="question-font">
        Um mago me colocou no corpo da sua ex e sua ex no meu corpo. 
        <br><br>
        Para desfazer a maldição, você deve beijar uma. 
        <br><br>
        <strong>Quem você escolhe?</strong>
        </p>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💋 Sua ex no meu corpo", key="opcao1", use_container_width=True):
            registrar_resposta("pergunta1", "ex_no_corpo_atual")
    
    with col2:
        if st.button("💋 Eu no corpo da sua ex", key="opcao2", use_container_width=True):
            registrar_resposta("pergunta1", "atual_no_corpo_ex")

# TELA DE RESULTADO
elif st.session_state.tela == 'resultado':
    st.markdown('<p class="big-font">🔥 RESULTADO 🔥</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    resposta = st.session_state.respostas.get("pergunta1")
    
    if resposta == "ex_no_corpo_atual":
        st.markdown('''
            <p class="question-font">
            Você escolheu beijar <strong>sua ex no meu corpo</strong>! 😱
            <br><br>
            Então você ainda pensa na sua ex? 🤔
            <br><br>
            <strong>DEVERIA COMEÇAR UMA BRIGA? SIM! 💥</strong>
            </p>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
            <p class="question-font">
            Você escolheu beijar <strong>eu no corpo da sua ex</strong>! 😏
            <br><br>
            Interessante... Você gosta mesmo é do corpo dela? 🤨
            <br><br>
            <strong>DEVERIA COMEÇAR UMA BRIGA? SIM! 💥</strong>
            </p>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 JOGAR NOVAMENTE", key="btn_restart", use_container_width=True):
            st.session_state.tela = 'inicio'
            st.session_state.respostas = {}
            st.rerun()
