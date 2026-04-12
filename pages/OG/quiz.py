import streamlit as st
import streamlit.components.v1 as components
from pages.utils import img_src, esc


def handle_quiz_answer(resposta: bool) -> None:
    if st.session_state.show_popup or st.session_state.get("show_success_popup", False):
        return
    idx = st.session_state.quiz_index
    if idx >= len(st.session_state.quiz_items):
        return
    item    = st.session_state.quiz_items[idx]
    correct = (resposta == item["verdadeiro"])
    st.session_state.quiz_answers.append({"email": item["titulo"], "correct": correct})
    if correct:
        st.session_state.quiz_score += 1
        st.session_state.show_success_popup = True
    else:
        st.session_state.show_popup        = True
        st.session_state.popup_explanation = item["explicacao"]


def page_quiz() -> None:
    if st.session_state.quiz_index >= len(st.session_state.quiz_items):
        st.session_state.page = "resultado"
        st.rerun()
        return

    item     = st.session_state.quiz_items[st.session_state.quiz_index]
    nome     = st.session_state.user_name
    corpo    = item["corpo"].replace("[NOME]", nome)
    av_color = item.get("avatar_color", "#1a73e8")
    av_text  = item.get("avatar_text",  "?")

    src = img_src("8-Quiz.png")

    # POPUP DE SUCESSO
    if st.session_state.get("show_success_popup", False):
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * { margin:0; padding:0; box-sizing:border-box; }
                body { width:450px; height:750px; margin:0 auto; background:transparent; }
                .popup-overlay {
                    position:fixed; top:0; left:0; width:100%; height:100%;
                    background:rgba(0,0,0,0.76); display:flex;
                    align-items:center; justify-content:center; z-index:1000;
                }
                .popup-box {
                    background:#fff; border-radius:16px; padding:30px 24px;
                    max-width:350px; min-width:280px; text-align:center;
                    box-shadow:0 10px 40px rgba(0,0,0,0.45);
                }
                .popup-icon { font-size:48px; margin-bottom:14px; }
                .popup-title {
                    font-size:16px; color:#191539; font-family:Arial,sans-serif;
                    font-weight:bold; margin-bottom:8px;
                }
                .popup-text {
                    font-size:14px; color:#555; line-height:1.6;
                    font-family:Arial,sans-serif;
                }
            </style>
        </head>
        <body>
            <div class="popup-overlay">
                <div class="popup-box">
                    <div class="popup-icon">✅</div>
                    <div class="popup-title">Bom trabalho!</div>
                    <div class="popup-text">Você identificou corretamente este e-mail.</div>
                </div>
            </div>
            <script>
                setTimeout(function() {
                    var buttons = window.parent.document.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++) {
                        if (buttons[i].innerText.trim() === 'PROXIMA') {
                            buttons[i].click();
                            return;
                        }
                    }
                }, 1500);
            </script>
        </body>
        </html>
        """, height=750, width=450)

        st.markdown("""
        <style>
        div[data-testid="stButton"][st-key="btn_proxima"] {
            position: absolute !important;
            top: -9999px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("PROXIMA", key="btn_proxima"):
            st.session_state.show_success_popup = False
            st.session_state.quiz_index += 1
            st.rerun()
        return

    # POPUP DE ERRO
    if st.session_state.show_popup:
        expl = esc(st.session_state.popup_explanation)
        components.html(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{ margin:0; padding:0; box-sizing:border-box; }}
                body {{ width:450px; height:750px; margin:0 auto; background:transparent; }}
                .popup-overlay {{
                    position:fixed; top:0; left:0; width:100%; height:100%;
                    background:rgba(0,0,0,0.76); display:flex;
                    align-items:center; justify-content:center; z-index:1000;
                }}
                .popup-box {{
                    background:#fff; border-radius:16px; padding:30px 24px;
                    max-width:350px; text-align:center;
                    box-shadow:0 10px 40px rgba(0,0,0,0.45);
                }}
                .popup-icon {{ font-size:48px; margin-bottom:14px; }}
                .popup-text {{
                    font-size:14px; color:#191539; line-height:1.6;
                    margin-bottom:24px; font-family:Arial,sans-serif;
                }}
                .popup-button {{
                    background:#1a1259; color:white; border:none;
                    border-radius:8px; padding:12px 30px; font-size:15px;
                    font-weight:bold; cursor:pointer; font-family:Arial,sans-serif;
                }}
                .popup-button:hover {{ background:#2a1d7a; }}
            </style>
        </head>
        <body>
            <div class="popup-overlay">
                <div class="popup-box">
                    <div class="popup-icon">❌</div>
                    <div class="popup-text">{expl}</div>
                    <button class="popup-button" id="closePopup">Continuar</button>
                </div>
            </div>
            <script>
                document.getElementById('closePopup').addEventListener('click', function() {{
                    var buttons = window.parent.document.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++) {{
                        if (buttons[i].innerText.trim() === 'CONTINUAR') {{
                            buttons[i].click();
                            return;
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        """, height=750, width=450)

        st.markdown("""
        <style>
        div[data-testid="stButton"][st-key="btn_continuar"] {
            position: absolute !important;
            top: -9999px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("CONTINUAR", key="btn_continuar"):
            st.session_state.show_popup        = False
            st.session_state.popup_explanation = ""
            st.session_state.quiz_index       += 1
            st.rerun()
        return

    # TELA PRINCIPAL
    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ margin:0; padding:0; box-sizing:border-box; }}
            body {{ width:450px; height:750px; margin:0 auto; overflow:hidden; }}
            .container {{ position:relative; width:450px; height:750px; }}
            img {{ width:100%; height:100%; display:block; z-index:1; }}
            .email-bg {{
                position:absolute; left:12%; top:16.67%; width:76.22%; height:72.13%;
                background:#d9d9d9; border-radius:10px; overflow:hidden; z-index:2;
            }}
            .email-content {{
                position:absolute; left:17.56%; top:20%; width:65.11%; height:65.47%;
                overflow:hidden; font-family:Arial,sans-serif; z-index:3;
            }}
            .avatar {{
                width:32px; height:32px; min-width:32px; background:{av_color};
                border-radius:50%; display:flex; align-items:center; justify-content:center;
                color:#fff; font-weight:bold; font-size:14px;
            }}
            .btn {{
                position:absolute; height:40px; background:transparent;
                border:none; cursor:pointer; z-index:10;
            }}
            #btnV {{ left:53px; top:677px; width:154px; }}
            #btnF {{ left:243px; top:677px; width:154px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{src}">
            <div class="email-bg"></div>
            <div class="email-content">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;">
                    <div class="avatar">{av_text}</div>
                    <div>
                        <div style="font-weight:bold;font-size:12px;color:#191539;">{esc(item['remetente'])}</div>
                        <div style="font-size:10px;color:#666;">{esc(item.get('data','Hoje'))}</div>
                    </div>
                </div>
                <div style="font-weight:bold;font-size:12px;color:#191539;margin-bottom:8px;">{esc(item['titulo'])}</div>
                <div style="font-size:11px;color:#333;line-height:1.45;margin-bottom:10px;">{esc(corpo)}</div>
                <div style="font-size:10px;color:#1a73e8;word-break:break-all;">&#128279; {esc(item['link'])}</div>
            </div>
            <button id="btnV" class="btn"></button>
            <button id="btnF" class="btn"></button>
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
            document.getElementById('btnV').onclick = function() {{ clickByText('VERDADEIRO'); }};
            document.getElementById('btnF').onclick = function() {{ clickByText('FALSO'); }};
        </script>
    </body>
    </html>
    """, height=750, width=450)

    st.markdown("""
    <style>
    div[data-testid="stButton"][st-key="btn_verd"],
    div[data-testid="stButton"][st-key="btn_falso"] {
        position: absolute !important;
        top: -9999px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("VERDADEIRO", key="btn_verd"):
        handle_quiz_answer(True)
        st.rerun()

    if st.button("FALSO", key="btn_falso"):
        handle_quiz_answer(False)
        st.rerun()
