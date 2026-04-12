import streamlit as st
from pages.utils import img_src


def page_welcome() -> None:
    src = img_src("1-BOAS-VINDAS.png")

    if "input_error" not in st.session_state:
        st.session_state.input_error = False

    border_color = '#ff7a6c' if st.session_state.input_error else '#1a73e8'

    st.markdown(f"""
    <div style="position:relative; width:450px; height:750px; margin:0 auto;">
        <img src="{src}" style="width:100%; height:100%; display:block;">
    </div>

    <style>
    div[data-testid="stTextInput"] {{
        position: fixed !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 607px !important;
        width: 282px !important;
        z-index: 100 !important;
        background: transparent !important;
    }}
    div[data-testid="stTextInput"] input {{
        background: white !important;
        border: 2px solid {border_color} !important;
        border-radius: 8px !important;
        text-align: center !important;
        color: #191539 !important;
        transition: border 0.2s ease !important;
    }}
    .warning-text {{
        position: fixed !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 656px !important;
        width: 282px !important;
        text-align: center !important;
        font-size: 12px !important;
        font-family: Arial, sans-serif !important;
        color: #ff7a6c !important;
        font-weight: bold !important;
        z-index: 100 !important;
        background: transparent !important;
        pointer-events: none !important;
        display: {'block' if st.session_state.input_error else 'none'} !important;
    }}
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
    }}
    div[data-testid="stButton"] button:hover {{
        background: #2a1d7a !important;
    }}
    div[data-testid="stTextInput"] label {{
        display: none !important;
    }}
    </style>

    <div id="warning-text" class="warning-text">⚠️ Por favor, digite seu nome!</div>
    """, unsafe_allow_html=True)

    name = st.text_input("nome", key="welcome_name", label_visibility="collapsed",
                         placeholder="Digite seu nome", on_change=clear_warning)

    if st.button("CONTINUAR", key="welcome_btn", use_container_width=True):
        name_sem_digitos = ''.join(c for c in (name or '') if not c.isdigit()).strip()
        if len(name_sem_digitos) >= 2:
            st.session_state.user_name   = name.strip()
            st.session_state.input_error = False
            st.session_state.page        = "engenharia"
            st.rerun()
        else:
            st.session_state.input_error = True
            st.rerun()

    st.markdown("""
    <script>
        var input = document.querySelector('div[data-testid="stTextInput"] input');
        if (input) {
            input.addEventListener('focus', function() {
                var warning = document.getElementById('warning-text');
                if (warning) warning.style.display = 'none';
            });
        }
        setTimeout(function() {
            var inputField = document.querySelector('div[data-testid="stTextInput"] input');
            if (inputField && inputField.style.border === '2px solid rgb(255, 122, 108)') {
                inputField.style.border = '2px solid #1a73e8';
                var warning = document.getElementById('warning-text');
                if (warning) warning.style.display = 'none';
            }
        }, 1500);
    </script>
    """, unsafe_allow_html=True)


def clear_warning():
    if st.session_state.input_error:
        st.session_state.input_error = False
