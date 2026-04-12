import random
import streamlit as st
from pages.utils import img_src
from quiz_data import QUIZ_ITEMS


def iniciar_quiz():
    """Seleciona 1 email de cada grupo em ordem crescente de dificuldade."""
    grupos = {}
    for item in QUIZ_ITEMS:
        g = item['grupo']
        grupos.setdefault(g, []).append(item)

    items = [random.choice(grupos[g]) for g in sorted(grupos.keys())]

    st.session_state.quiz_items        = items
    st.session_state.quiz_index        = 0
    st.session_state.quiz_score        = 0
    st.session_state.quiz_answers      = []
    st.session_state.show_popup        = False
    st.session_state.popup_explanation = ""
    st.session_state.show_success_popup = False


def page_qrcode() -> None:
    src = img_src("6-QR Code.png")

    st.markdown(f"""
    <div style="position:relative; width:450px; height:750px; margin:0 auto;">
        <img src="{src}" style="width:100%; height:100%; display:block;">
    </div>

    <style>
    div[data-testid="stButton"] {{
        position: fixed !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 694px !important;
        width: 350px !important;
        z-index: 100 !important;
    }}
    div[data-testid="stButton"] button {{
        background: #1a1259 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        height: 40px !important;
        font-size: 16px !important;
    }}
    div[data-testid="stButton"] button:hover {{
        background: #2a1d7a !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    if st.button("CONTINUAR", key="btn_qr", use_container_width=True):
        st.session_state.page = "testemail"
        st.rerun()
