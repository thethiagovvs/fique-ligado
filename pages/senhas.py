import streamlit as st
from pages.utils import img_src


def page_senhas() -> None:
    # Mostra a imagem
    src = img_src("4-Entropia de Senhas.png")
    
    st.markdown(f"""
    <div style="position:relative; width:450px; height:750px; margin:0 auto;">
        <img src="{src}" style="width:100%; height:100%; display:block;">
    </div>
    """, unsafe_allow_html=True)
    
    # Botão CONTINUAR
    if st.button("CONTINUAR", key="btn_senhas", use_container_width=True):
        st.session_state.page = "twofactor"
        st.rerun()
    
    # CSS para posicionar o botão sobre a imagem
    st.markdown("""
    <style>
    /* Posiciona o botão sobre a imagem */
    div[data-testid="stButton"] {
        position: fixed !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 694px !important;
        width: 350px !important;
        z-index: 100 !important;
    }
    
    div[data-testid="stButton"] button {
        background: #1a1259 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        height: 40px !important;
        font-size: 16px !important;
    }
    
    div[data-testid="stButton"] button:hover {
        background: #2a1d7a !important;
    }
    </style>
    """, unsafe_allow_html=True)