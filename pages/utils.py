import os
import base64
import streamlit as st

# ============================================================
# CONFIGURAÇÕES PADRÃO
# ============================================================
DEFAULTS = {
    "page":                 "welcome",
    "user_name":            "",
    "quiz_score":           0,
    "two_factor_knowledge": None,
    "quiz_answers":         [],
    "quiz_index":           0,
    "quiz_items":           [],
    "show_popup":           False,
    "popup_explanation":    "",
}

# ============================================================
# FUNÇÕES DE IMAGEM
# ============================================================
@st.cache_data
def _load_b64(name: str) -> str:
    path = os.path.join("imagens", name)
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def img_src(name: str) -> str:
    b64 = _load_b64(name)
    return f"data:image/png;base64,{b64}" if b64 else ""

# ============================================================
# FUNÇÕES DE ESCAPE
# ============================================================
def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
            .replace("\n", "<br>")
    )

# ============================================================
# FUNÇÕES DE NAVEGAÇÃO
# ============================================================
def set_page(page: str) -> None:
    st.session_state.page = page
    st.rerun()

# ============================================================
# FUNÇÃO SCREEN (com padding-bottom para responsividade)
# ============================================================
def screen(img_name: str, extra_html: str = "") -> None:
    """Renderiza a imagem como container responsivo com proporção 450x750."""
    b64 = _load_b64(img_name)
    st.markdown(f"""
    <div id="fica-screen" style="position:relative;width:100%;padding-bottom:166.67%;overflow:hidden;">
        <img src="data:image/png;base64,{b64}"
             style="position:absolute;top:0;left:0;width:100%;height:100%;display:block;pointer-events:none;">
        <div style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:5;">
            {extra_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FUNÇÃO BTN_OVER (posiciona botão do Streamlit via CSS)
# ============================================================
def btn_over(key: str, left: str, top: str, width: str, height: str) -> None:
    """CSS para posicionar um st.button sobre a imagem usando porcentagem."""
    st.markdown(f"""
    <style>
    [data-testid="stButton"][st-key="{key}"] {{
        position: absolute !important;
        left: {left} !important;
        top: {top} !important;
        width: {width} !important;
        height: {height} !important;
        z-index: 20 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stButton"][st-key="{key}"] button {{
        width: 100% !important;
        height: 100% !important;
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        cursor: pointer !important;
        padding: 0 !important;
        min-height: 0 !important;
        box-shadow: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# FUNÇÃO INPUT_OVER (posiciona input do Streamlit via CSS)
# ============================================================
def input_over(key: str, left: str, top: str, width: str, height: str) -> None:
    """CSS para posicionar um st.text_input sobre a imagem usando porcentagem."""
    st.markdown(f"""
    <style>
    [data-testid="stTextInput"][st-key="{key}"] {{
        position: absolute !important;
        left: {left} !important;
        top: {top} !important;
        width: {width} !important;
        height: {height} !important;
        z-index: 20 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stTextInput"][st-key="{key}"] input {{
        width: 100% !important;
        height: 100% !important;
        background: transparent !important;
        border: none !important;
        font-size: 16px !important;
        color: #191539 !important;
        text-align: center !important;
        padding: 0 !important;
        outline: none !important;
        box-shadow: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# FUNÇÃO RENDER (NOVA VERSÃO - SEM IFRAME!)
# ============================================================
def render(img_name: str, overlays: str = "") -> None:
    """Renderiza imagem + overlays em HTML puro (sem iframe)."""
    b64 = _load_b64(img_name)
    
    # IMPORTANTE: Script para enviar ações via query_params
    js_script = """
    <script>
    function sendAction(action) {
        var url = new URL(window.location.href);
        url.searchParams.set('action', action);
        window.location.href = url.toString();
    }
    </script>
    """
    
    # Converte overlays para usar sendAction em vez de href direto
    # (os ibuttons usam href, precisamos converter)
    overlays_fixed = overlays.replace('href="/?action=', 'href="#" onclick="sendAction(\'')
    overlays_fixed = overlays_fixed.replace('" target="_top"', '\'); return false;"')
    
    html = f"""
    {js_script}
    <div style="position:relative;width:450px;height:750px;overflow:hidden;margin:0 auto;">
        <img src="data:image/png;base64,{b64}"
             style="position:absolute;top:0;left:0;width:450px;height:750px;display:block;z-index:1;">
        <div style="position:absolute;top:0;left:0;width:450px;height:750px;z-index:10;">
            {overlays_fixed}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ============================================================
# FUNÇÃO IBUTTON (com sendAction em vez de href)
# ============================================================
def ibutton(action: str, x: int, y: int, w: int, h: int) -> str:
    """Botão invisível que chama sendAction."""
    return (
        f"<a href='#' onclick=\"sendAction('{action}'); return false;\""
        f" style='position:absolute;left:{x}px;top:{y}px;"
        f"width:{w}px;height:{h}px;display:block;z-index:10;"
        f"text-decoration:none;'></a>"
    )