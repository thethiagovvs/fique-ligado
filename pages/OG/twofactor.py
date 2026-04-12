import streamlit as st
import streamlit.components.v1 as components
from pages.utils import img_src


def page_twofactor() -> None:
    src = img_src("5-Autenticação de Dois Fatores.png")

    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ margin:0; padding:0; box-sizing:border-box; }}
            body {{ width:450px; height:750px; margin:0 auto; overflow:hidden; background:#1a73e8; }}
            .container {{ position:relative; width:450px; height:750px; }}
            img {{ width:100%; height:100%; display:block; }}
            .btn {{
                position: absolute;
                left: 98px;
                width: 254px;
                height: 38px;
                background: transparent;
                border: none;
                cursor: pointer;
                z-index: 10;
            }}
            #btn1 {{ top: 544px; }}
            #btn2 {{ top: 600px; }}
            #btn3 {{ top: 656px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{src}">
            <button id="btn1" class="btn"></button>
            <button id="btn2" class="btn"></button>
            <button id="btn3" class="btn"></button>
        </div>
        <script>
            function clickByText(text) {{
                var buttons = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < buttons.length; i++) {{
                    if (buttons[i].innerText.trim() === text) {{
                        buttons[i].click();
                        return;
                    }}
                }}
            }}
            document.getElementById('btn1').onclick = function() {{ clickByText('1'); }};
            document.getElementById('btn2').onclick = function() {{ clickByText('2'); }};
            document.getElementById('btn3').onclick = function() {{ clickByText('3'); }};
        </script>
    </body>
    </html>
    """, height=750, width=450)

    # CSS ANTES dos botões
    st.markdown("""
    <style>
    div[data-testid="stButton"][st-key="btn_nao"],
    div[data-testid="stButton"][st-key="btn_conheco"],
    div[data-testid="stButton"][st-key="btn_uso"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("1", key="btn_nao"):
        st.session_state.two_factor_knowledge = "nao"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("2", key="btn_conheco"):
        st.session_state.two_factor_knowledge = "sim_conheco_nao_uso"
        st.session_state.page = "qrcode"
        st.rerun()

    if st.button("3", key="btn_uso"):
        st.session_state.two_factor_knowledge = "sim_utilizo"
        st.session_state.page = "qrcode"
        st.rerun()
