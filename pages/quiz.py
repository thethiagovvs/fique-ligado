import streamlit as st
import streamlit.components.v1 as components
from pages.utils import esc

GMAIL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="28" height="28">
  <path fill="#EA4335" d="M6 40h6V23.8L4 18v18c0 2.2 1.8 4 4 4z"/>
  <path fill="#34A853" d="M36 40h6c2.2 0 4-1.8 4-4V18l-8 5.8z"/>
  <path fill="#FBBC05" d="M36 10l-12 8.7L12 10H6l18 13 18-13z"/>
  <path fill="#4285F4" d="M4 18l8 5.8V10H6c-2.2 0-4 1.8-4 4v4z"/>
  <path fill="#EA4335" d="M44 14c0-2.2-1.8-4-4-4h-4v13.8L44 18v-4z"/>
</svg>"""


def handle_quiz_answer(resposta: bool) -> None:
    idx = st.session_state.quiz_index
    if idx >= len(st.session_state.quiz_items):
        return
    item    = st.session_state.quiz_items[idx]
    correct = (resposta == item["verdadeiro"])
    st.session_state.quiz_answers.append({"email": item["titulo"], "correct": correct})
    if correct:
        st.session_state.quiz_score        += 1
        st.session_state.show_success_popup = True
    else:
        st.session_state.show_popup        = True
        st.session_state.popup_explanation = item["explicacao"]


def page_quiz() -> None:
    if st.session_state.quiz_index >= len(st.session_state.quiz_items):
        st.session_state.page = "resultado"
        st.rerun()
        return

    # ── POPUP SUCESSO com countdown 1.5s ──────────────────────────────────────
    if st.session_state.get("show_success_popup", False):
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * { margin:0; padding:0; box-sizing:border-box; }
                body { background:transparent; font-family:Arial,sans-serif; }
                .overlay {
                    position:fixed; top:0; left:0; width:100%; height:100%;
                    background:rgba(0,0,0,0.7); display:flex;
                    align-items:center; justify-content:center; z-index:9999;
                }
                .box {
                    background:#fff; border-radius:16px; padding:32px 24px;
                    max-width:320px; width:90%; text-align:center;
                    box-shadow:0 8px 32px rgba(0,0,0,0.35);
                }
                .icon { font-size:3.5rem; margin-bottom:12px; }
                .title { font-size:17px; font-weight:700; color:#1a237e; margin-bottom:6px; }
                .text  { font-size:14px; color:#555; line-height:1.6; }
                .bar-wrap { margin-top:16px; background:#e0e0e0; border-radius:8px; height:6px; overflow:hidden; }
                .bar { height:6px; background:#43a047; border-radius:8px;
                       width:100%; animation:shrink 1.5s linear forwards; }
                @keyframes shrink { from{width:100%} to{width:0%} }
            </style>
        </head>
        <body>
            <div class="overlay">
                <div class="box">
                    <div class="icon">✅</div>
                    <div class="title">Bom trabalho!</div>
                    <div class="text">Você identificou corretamente este e-mail.</div>
                    <div class="bar-wrap"><div class="bar"></div></div>
                </div>
            </div>
            <script>
                setTimeout(function() {
                    var btns = window.parent.document.querySelectorAll('button');
                    for (var i = 0; i < btns.length; i++) {
                        if (btns[i].innerText.trim() === '__PROXIMA__') {
                            btns[i].click();
                            return;
                        }
                    }
                }, 1500);
            </script>
        </body>
        </html>
        """, height=400)

        if st.button("__PROXIMA__", key="btn_proxima"):
            st.session_state.show_success_popup = False
            st.session_state.quiz_index        += 1
            st.rerun()
        return

    # ── POPUP ERRO ─────────────────────────────────────────────────────────────
    if st.session_state.show_popup:
        expl = st.session_state.popup_explanation
        st.markdown(f"""
<div class="card" style="text-align:center;padding:28px 22px;">
  <div style="font-size:3.5rem;margin-bottom:10px;">❌</div>
  <p class="body-text">{expl}</p>
</div>
""", unsafe_allow_html=True)
        if st.button("CONTINUAR →", key="btn_continuar", use_container_width=True):
            st.session_state.show_popup        = False
            st.session_state.popup_explanation = ""
            st.session_state.quiz_index       += 1
            st.rerun()
        return

    # ── TELA PRINCIPAL ─────────────────────────────────────────────────────────
    item     = st.session_state.quiz_items[st.session_state.quiz_index]
    total    = len(st.session_state.quiz_items)
    atual    = st.session_state.quiz_index + 1
    nome     = st.session_state.user_name
    corpo    = esc(item["corpo"].replace("[NOME]", nome))
    av_color = item.get("avatar_color", "#1a73e8")
    av_text  = item.get("avatar_text",  "?")

    components.html(f"""<!DOCTYPE html><html><head>
<meta charset="utf-8">
<style>
  *{{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif;}}
  body{{background:transparent;}}
  .card{{background:#fff;border-radius:16px;overflow:hidden;}}
  .header{{display:flex;align-items:center;justify-content:space-between;
    padding:10px 14px 8px;border-bottom:1px solid #e8e8e8;}}
  .brand{{display:flex;align-items:center;gap:7px;}}
  .gmail-txt{{font-size:1rem;color:#5f6368;font-weight:400;}}
  .counter{{font-size:12px;color:#888;background:#f1f3f4;
    border-radius:12px;padding:3px 10px;}}
  .meta{{padding:10px 14px 8px;border-bottom:1px solid #f0f0f0;}}
  .sender{{display:flex;align-items:center;gap:8px;margin-bottom:5px;}}
  .avatar{{width:32px;height:32px;min-width:32px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    background:{av_color};color:#fff;font-weight:700;font-size:.85rem;}}
  .sname{{font-weight:700;font-size:12px;color:#202124;}}
  .sdate{{font-size:11px;color:#888;}}
  .subject{{font-weight:700;font-size:13px;color:#202124;}}
  .body{{padding:10px 14px 14px;font-size:12px;color:#333;line-height:1.6;}}
  .link{{margin-top:8px;font-size:11px;color:#1a73e8;word-break:break-all;}}
</style>
</head><body>
<div class="card">
  <div class="header">
    <div class="brand">{GMAIL_SVG}<span class="gmail-txt">Gmail</span></div>
    <span class="counter">E-mail {atual} de {total}</span>
  </div>
  <div class="meta">
    <div class="sender">
      <div class="avatar">{av_text}</div>
      <div>
        <div class="sname">{esc(item['remetente'])}</div>
        <div class="sdate">{esc(item.get('data','Hoje'))}</div>
      </div>
    </div>
    <div class="subject">{esc(item['titulo'])}</div>
  </div>
  <div class="body">
    {corpo}
    <div class="link">🔗 {esc(item['link'])}</div>
  </div>
</div>
</body></html>""", height=340, scrolling=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ VERDADEIRO", key="btn_verd", use_container_width=True):
            handle_quiz_answer(True)
            st.rerun()
    with col2:
        if st.button("❌ FALSO", key="btn_falso", use_container_width=True):
            handle_quiz_answer(False)
            st.rerun()
