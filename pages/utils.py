import os, base64
import streamlit as st

DEFAULTS = {
    "page":                  "welcome",
    "user_name":             "",
    "quiz_score":            0,
    "two_factor_knowledge":  None,
    "quiz_answers":          [],
    "quiz_index":            0,
    "quiz_items":            [],
    "show_popup":            False,
    "popup_explanation":     "",
    "show_success_popup":    False,
}

@st.cache_data
def _logo_b64() -> str:
    path = os.path.join("imagens", "LOGO.png")
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def logo_html() -> str:
    b64 = _logo_b64()
    if b64:
        return f'<div style="text-align:center;padding:16px 0 10px;"><img src="data:image/png;base64,{b64}" style="width:280px;max-width:90%;object-fit:contain;"></div>'
    return '<div style="text-align:center;padding:16px 0 10px;"><span style="font-family:Georgia,serif;font-style:italic;font-size:2rem;color:#fff;">fique</span><br><span style="font-family:Arial Black,sans-serif;font-weight:900;font-size:3rem;color:#fff;letter-spacing:2px;">LIGADO</span></div>'

def esc(text: str) -> str:
    return (
        text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;").replace("'","&#39;").replace("\n","<br>")
    )

BASE_CSS = """
<style>
  .stApp { background: linear-gradient(160deg,#1565c0 0%,#1a237e 100%) !important; min-height:100vh; }
  .block-container { max-width:450px !important; padding:0.5rem 1rem 2rem !important; margin:0 auto !important; }
  header, footer, #MainMenu { display:none !important; }

  /* ── Card ── */
  .card {
    background:#fff; border-radius:16px;
    padding:22px 20px 20px; margin-bottom:12px;
  }
  .card-content { min-height:560px; }
  .card-logo    { min-height:440px; }

  /* ── Tipografia ── */
  .page-title {
    text-align:center; font-size:22px; font-weight:800;
    color:#fff; margin:8px 0 12px; letter-spacing:.5px;
  }
  .section-title { font-size:16px; font-weight:700; color:#1a237e; margin:12px 0 4px; }
  .body-text     { font-size:14px; color:#333; line-height:1.65; margin:0 0 8px; }
  .small-text    { font-size:12px; color:#777; line-height:1.4; }

  /* ── Highlight boxes ── */
  .box-blue {
    background:#e8f0fe; border-radius:10px;
    padding:14px 16px; margin:10px 0;
    font-size:14px; color:#1a237e; line-height:1.6;
  }
  .box-yellow {
    background:#fff8e1; border:1.5px solid #f9a825;
    border-radius:10px; padding:14px 16px; margin:10px 0;
    font-size:14px; color:#5d4037; line-height:1.6;
  }

  /* ── Listas ── */
  .clean-list { padding-left:18px; margin:6px 0 0; font-size:14px; line-height:1.8; color:#333; }

  /* ── Stat rows ── */
  .stat-row { display:flex; gap:10px; align-items:flex-start; margin:10px 0; }
  .stat-badge {
    background:#1a73e8; color:#fff; font-weight:800; font-size:.95rem;
    border-radius:8px; padding:6px 8px; min-width:48px; text-align:center; flex-shrink:0;
  }
  .stat-text { font-size:14px; color:#333; line-height:1.55; }

  /* ── Email demo (phishing) ── */
  .email-demo { background:#f5f5f5; border-radius:8px; padding:12px 14px; margin:10px 0; font-size:13px; color:#333; line-height:1.6; }
  .email-field { margin-bottom:3px; }
  .email-field span { font-weight:700; color:#1a237e; }
  .email-body { margin-top:8px; color:#444; }
  .email-link { color:#1a73e8; font-style:italic; word-break:break-all; margin-top:6px; }

  /* ── Botão padrão (CONTINUAR etc.) ── */
  div[data-testid="stButton"] > button {
    background:#1a1259 !important; color:#fff !important;
    font-weight:700 !important; font-size:15px !important;
    border:none !important; border-radius:8px !important;
    height:46px !important; letter-spacing:.5px;
    transition:background .15s;
  }
  div[data-testid="stButton"] > button:hover { background:#2a1d7a !important; }

  /* ── Botões 2FA ── */
  div[data-testid="stButton"][st-key="btn_nao"]    > button { background:#ff7a6c !important; color:#fff !important; }
  div[data-testid="stButton"][st-key="btn_nao"]    > button:hover { background:#e55a50 !important; }
  div[data-testid="stButton"][st-key="btn_conheco"]> button { background:#ffde59 !important; color:#333 !important; }
  div[data-testid="stButton"][st-key="btn_conheco"]> button:hover { background:#e5c840 !important; }
  div[data-testid="stButton"][st-key="btn_uso"]    > button { background:#82c271 !important; color:#fff !important; }
  div[data-testid="stButton"][st-key="btn_uso"]    > button:hover { background:#66a857 !important; }

  /* ── Botões quiz VERDADEIRO / FALSO ── */
  div[data-testid="stButton"][st-key="btn_verd"] > button {
    background:#43a047 !important; font-size:15px !important; height:50px !important;
  }
  div[data-testid="stButton"][st-key="btn_verd"] > button:hover { background:#2e7d32 !important; }
  div[data-testid="stButton"][st-key="btn_falso"] > button {
    background:#e53935 !important; font-size:15px !important; height:50px !important;
  }
  div[data-testid="stButton"][st-key="btn_falso"] > button:hover { background:#b71c1c !important; }

  /* ── Botões resultado ── */
  div[data-testid="stButton"][st-key="btn_refazer"] > button { background:#546e7a !important; }
  div[data-testid="stButton"][st-key="btn_refazer"] > button:hover { background:#37474f !important; }

  /* ── Input ── */
  div[data-testid="stTextInput"] label { display:none !important; }
  div[data-testid="stTextInput"] input {
    text-align:center !important; font-size:15px !important;
    border-radius:8px !important; border:2px solid #1a73e8 !important; color:#1a237e !important;
  }
  div[data-testid="stTextInput"] [data-testid="InputInstructions"] { display:none !important; }

  /* ── Popup overlay ── */
  .popup-overlay {
    position:fixed; top:0; left:0; width:100%; height:100%;
    background:rgba(0,0,0,.7); display:flex; align-items:center;
    justify-content:center; z-index:9999;
  }
  .popup-box {
    background:#fff; border-radius:16px; padding:28px 24px;
    max-width:340px; width:90%; text-align:center;
    box-shadow:0 8px 32px rgba(0,0,0,.35);
  }
  .popup-icon  { font-size:3rem; margin-bottom:10px; }
  .popup-title { font-size:16px; font-weight:700; color:#1a237e; margin-bottom:6px; }
  .popup-text  { font-size:14px; color:#333; line-height:1.6; margin-bottom:18px; }
</style>
"""
