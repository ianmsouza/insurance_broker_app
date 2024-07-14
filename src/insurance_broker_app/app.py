import streamlit as st
from broker import Agent
import time
from streamlit_lottie import st_lottie
import requests

# Key OpenAI
agent = Agent("sk-proj-xxxxxxxxxxxxxxxxxxxxx") 

st.set_page_config(page_title="Corretor Virtual de Seguros de Vida", page_icon="🛡️", layout='wide')
st.title('Corretor Virtual de Seguros de Vida')

def initialize_session_state():
    """Inicializa o estado da sessão do Streamlit com valores padrão."""
    if "profile" not in st.session_state:
        st.session_state.profile = ""
    if "suggestion" not in st.session_state:
        st.session_state.suggestion = None

def reset_session_state():
    """Reseta o estado da sessão do Streamlit, preservando 'profile' e 'suggestion'."""
    for key in st.session_state.keys():
        if key not in ["profile", "suggestion"]:
            del st.session_state[key]
    initialize_session_state()

st.write("Este aplicativo sugere os melhores planos de **Seguro de Vida** de acordo com seu perfil!")

def load_lottie_url(url: str):
    """Carrega uma animação Lottie a partir de uma URL.
    
    Args:
        url (str): A URL da animação Lottie.
    
    Returns:
        dict or None: O JSON da animação Lottie se a requisição for bem-sucedida, senão None.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL da animação Lottie
lottie_typing_url = "https://lottie.host/ec21a7f7-2e47-4e78-b3eb-4bf658515317/lRhyHR5KuE.json"

# Exemplo de URL Lottie para uma animação de digitação
# lottie_typing_url = "https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json"

lottie_typing_json = load_lottie_url(lottie_typing_url)

initialize_session_state()

# Definindo as colunas
col1, _ = st.columns([3, 1])  # Coluna 1 ocupando 75% da largura e coluna 2 ocupando 25%

profile_temp = ""  # Variável temporária para armazenar o perfil temporariamente

with col1:
    profile_temp = st.text_area("Conte-nos sobre você: (por exemplo, idade, ocupação, condição de saúde, histórico médico familiar, estilo de vida e hábitos como tabagismo e prática de exercícios físicos)", height=100, max_chars=500, key="profile_temp")
    button_clicked = st.button("Obter Sugestão de Seguro")

    if button_clicked and profile_temp:
        with st.spinner("Analisando seu perfil..."):
            st_lottie(lottie_typing_json, height=150, width=150)  # Exibindo a animação Lottie
            time.sleep(2)  # Simulando um processamento de 2 segundos
            reset_session_state()
            st.session_state.profile = profile_temp
            st.session_state.suggestion = agent.get_suggestion(profile_temp)

        st.experimental_rerun()  # Rerun the script to show suggestions after processing

if st.session_state.suggestion:
    st.header("📝 Planos de Seguro Sugeridos")
    try:
        st.write(st.session_state.suggestion['agent_suggestion'])
    except KeyError:
        st.write("Desculpe, não conseguimos encontrar um plano de seguro adequado para você.")
