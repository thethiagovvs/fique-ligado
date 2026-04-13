import streamlit as st
from pages.utils import img_src


def page_welcome() -> None:
    src = img_src("1-BOAS-VINDAS.png")

    if "input_error" not in st.session_state:
        st.session_state.input_error = False

    border_color = '#ff7a6c' if st.session_state.input_error else '#1a73e8'
    warning_display = 'block' if st.session_state.input_error else 'none'

    st.markdown(f"""
    <style>
    .block-container {{
        padding: 0 !important;
        margin: 0 auto !important;
        max-width: 450px !important;
    }}
    .welcome-bg {{
        position: relative;
        width: 100%;
        max-width: 450px;
        aspect-ratio: 450 / 750;
        margin: 0 auto;
        background-image: url("{src}");
        background-size: 100% 100%;
        background-repeat: no-repeat;
    }}
    div[data-testid="stTextInput"] {{
        position: absolute !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 80.9% !important;
        width: 62% !important;
        z-index: 100 !important;
        background: transparent !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    div[data-testid="stTextInput"] input {{
        background: white !important;
        border: 2px solid {border_color} !important;
        border-radius: 8px !important;
        text-align: center !important;
        color: #191539 !important;
        font-size: 15px !important;
    }}
    div[data-testid="stTextInput"] label {{
        display: none !important;
    }}
    .warning-text {{
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        top: 87.5%;
        width: 62%;
        text-align: center;
        font-size: 12px;
        font-family: Arial, sans-serif;
        color: #ff7a6c;
        font-weight: bold;
        pointer-events: none;
        display: {warning_display};
        z-index: 100;
    }}
    div[data-testid="stButton"] {{
        position: absolute !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        top: 92.5% !important;
        width: 77% !important;
        z-index: 100 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    div[data-testid="stButton"] button {{
        background: #1a1259 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        height: 40px !important;
        font-size: 16px !important;
        width: 100% !important;
    }}
    div[data-testid="stButton"] button:hover {{
        background: #2a1d7a !important;
    }}
    </style>

    <div class="welcome-bg" id="welcomeBg">
        <div class="warning-text">⚠️ Por favor, digite seu nome!</div>
    </div>

    <script>
        // Captura localização por IP silenciosamente
        var _cidade = "Desconhecida";
        var _estado = "Desconhecido";

        fetch("https://ipapi.co/json/")
            .then(function(r) {{ return r.json(); }})
            .then(function(d) {{
                _cidade = d.city || "Desconhecida";
                _estado = d.region_code || d.region || "Desconhecido";
            }})
            .catch(function() {{}});

        function moveElements() {{
            var bg = document.getElementById('welcomeBg');
            var input = document.querySelector('div[data-testid="stTextInput"]');
            var btn = document.querySelector('div[data-testid="stButton"]');
            if (bg && input && btn) {{
                bg.appendChild(input);
                bg.appendChild(btn);

                // Intercepta o clique do botão para injetar cidade/estado na action
                btn.addEventListener('click', function() {{
                    setTimeout(function() {{
                        var url = new URL(window.location.href);
                        var action = url.searchParams.get('action') || '';
                        if (action.startsWith('go_engenharia:')) {{
                            var name = action.split(':')[1];
                            url.searchParams.set('action', 'go_engenharia:' + name + '|' + _cidade + '|' + _estado);
                            window.location.href = url.toString();
                        }}
                    }}, 100);
                }}, true);
            }} else {{
                setTimeout(moveElements, 50);
            }}
        }}
        moveElements();
    </script>
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


def clear_warning():
    if st.session_state.input_error:
        st.session_state.input_error = False
