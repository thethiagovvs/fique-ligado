import streamlit as st
import streamlit.components.v1 as components
from pages.utils import img_src


def page_welcome() -> None:
    src = img_src("1-BOAS-VINDAS.png")

    if "input_error" not in st.session_state:
        st.session_state.input_error = False

    border_color = '#ff7a6c' if st.session_state.input_error else '#1a73e8'
    warning_display = 'block' if st.session_state.input_error else 'none'

    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=450, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <style>
            * {{ margin:0; padding:0; box-sizing:border-box; }}
            body {{ width:450px; height:750px; margin:0 auto; overflow:hidden; background:#1a73e8; }}
            .container {{ position:relative; width:450px; height:750px; }}
            img {{ width:100%; height:100%; display:block; }}

            .input-box {{
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                top: 80.9%;
                width: 62.7%;
                z-index: 100;
            }}
            .input-box input {{
                width: 100%;
                height: 36px;
                background: white;
                border: 2px solid {border_color};
                border-radius: 8px;
                text-align: center;
                color: #191539;
                font-size: 15px;
                font-family: Arial, sans-serif;
                outline: none;
                padding: 0 8px;
            }}

            .warning-text {{
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                top: 87.5%;
                width: 62.7%;
                text-align: center;
                font-size: 12px;
                font-family: Arial, sans-serif;
                color: #ff7a6c;
                font-weight: bold;
                display: {warning_display};
                pointer-events: none;
            }}

            .btn-continuar {{
                position: absolute;
                left: 50%;
                transform: translateX(-50%);
                top: 92.5%;
                width: 77.7%;
                height: 40px;
                background: #1a1259;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-family: Arial, sans-serif;
                cursor: pointer;
                z-index: 100;
            }}
            .btn-continuar:hover {{ background: #2a1d7a; }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{src}">

            <div class="input-box">
                <input type="text" id="nameInput" placeholder="Digite seu nome" maxlength="50">
            </div>

            <div class="warning-text" id="warningText">⚠️ Por favor, digite seu nome!</div>

            <button class="btn-continuar" id="btnContinuar">CONTINUAR</button>
        </div>

        <script>
            var input = document.getElementById('nameInput');
            var warning = document.getElementById('warningText');
            var btn = document.getElementById('btnContinuar');

            input.addEventListener('focus', function() {{
                warning.style.display = 'none';
                input.style.border = '2px solid #1a73e8';
            }});

            btn.addEventListener('click', function() {{
                var name = input.value.trim();
                var semDigitos = name.replace(/[0-9]/g, '').trim();
                if (semDigitos.length >= 2) {{
                    warning.style.display = 'none';
                    var url = new URL(window.location.href);
                    url.searchParams.set('action', 'go_engenharia:' + encodeURIComponent(name));
                    window.top.location.href = url.toString();
                }} else {{
                    warning.style.display = 'block';
                    input.style.border = '2px solid #ff7a6c';
                }}
            }});

            input.addEventListener('keydown', function(e) {{
                if (e.key === 'Enter') btn.click();
            }});
        </script>
    </body>
    </html>
    """, height=750, width=450)
