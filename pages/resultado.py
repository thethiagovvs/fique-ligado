import streamlit as st
import streamlit.components.v1 as components
import requests
import base64
import os
from datetime import datetime
from pages.utils import esc, DEFAULTS

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

RESULTADO_LABEL = {
    "9-EXPERT (5_5 + usa 2FA).png":           "EXPERT",
    "10-BOM (4-5_5 + NÃO usa 2FA).png":       "BOM",
    "11-ATENÇÃO (3-4_5 + usa 2FA).png":       "ATENCAO",
    "12-ESTUDAR (3-4_5 + NÃO usa 2FA).png":   "ESTUDAR",
    "13-CUIDADO (0-2_5 - qualquer 2FA).png":  "CUIDADO",
}

DOIS_FA_LABEL = {
    "nao":                 "Nao conhece",
    "sim_conheco_nao_uso": "Conhece mas nao usa",
    "sim_utilizo":         "Utiliza",
}


def _img_base64(filename: str) -> str:
    caminho = os.path.join("imagens", filename)
    with open(caminho, "rb") as f:
        dados = base64.b64encode(f.read()).decode()
    ext = filename.rsplit(".", 1)[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    return f"data:{mime};base64,{dados}"


def get_location():
    """Tenta obter localização pelo IP real do usuário via headers."""
    try:
        # Tenta pegar o IP real do usuário pelo header X-Forwarded-For
        headers = st.context.headers
        ip = headers.get("X-Forwarded-For", "").split(",")[0].strip()
        
        if ip:
            geo = requests.get(f"https://ipapi.co/{ip}/json/", timeout=4).json()
        else:
            geo = requests.get("https://ipapi.co/json/", timeout=4).json()

        cidade = geo.get("city", "Desconhecida")
        estado = geo.get("region_code", geo.get("region", "Desconhecido"))
        return cidade, estado
    except Exception:
        return "Desconhecida", "Desconhecido"


def enviar_resultado(score: int, two_fa: str, img: str, nome_completo: str) -> None:
    if st.session_state.get("resultado_enviado", False):
        return

    primeiro_nome = nome_completo.strip().split()[0].capitalize() if nome_completo.strip() else "Anonimo"

    cidade, estado = get_location()

    payload = {
        "nome":      primeiro_nome,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "cidade":    cidade,
        "estado":    estado,
        "score":     f"{score}/5",
        "dois_fa":   DOIS_FA_LABEL.get(two_fa, two_fa),
        "resultado": RESULTADO_LABEL.get(img, img),
    }

    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=6)
        st.session_state.resultado_enviado = True
    except Exception:
        pass


def page_resultado() -> None:
    score  = st.session_state.quiz_score
    two_fa = st.session_state.two_factor_knowledge

    if   score >= 5 and two_fa == "sim_utilizo":  img = "9-EXPERT (5_5 + usa 2FA).png"
    elif score >= 4 and two_fa != "sim_utilizo":  img = "10-BOM (4-5_5 + NÃO usa 2FA).png"
    elif score >= 3 and two_fa == "sim_utilizo":  img = "11-ATENÇÃO (3-4_5 + usa 2FA).png"
    elif score >= 3 and two_fa != "sim_utilizo":  img = "12-ESTUDAR (3-4_5 + NÃO usa 2FA).png"
    else:                                          img = "13-CUIDADO (0-2_5 - qualquer 2FA).png"

    enviar_resultado(score, two_fa, img, st.session_state.user_name)

    nome      = esc(st.session_state.user_name)
    score_txt = f"{score}/5"
    src       = _img_base64(img)

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
            .overlay-nome {{
                position:absolute; left:77px; top:262px;
                width:296px; height:33px;
                display:flex; align-items:center; justify-content:center;
                color:#191539; font-size:26px; font-weight:bold;
                font-family:Arial,sans-serif;
                overflow:hidden; white-space:nowrap; z-index:2;
            }}
            .overlay-score {{
                position:absolute; left:146px; top:536px;
                width:158px; height:33px;
                display:flex; align-items:center; justify-content:center;
                color:#191539; font-size:26px; font-weight:bold;
                font-family:Arial,sans-serif; z-index:2;
            }}
            .btn {{
                position:absolute; height:40px;
                background:transparent; border:none;
                cursor:pointer; z-index:10;
            }}
            #btnRefazer   {{ left:53px;  top:618px; width:154px; }}
            #btnFinalizar {{ left:243px; top:618px; width:154px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{src}">
            <div class="overlay-nome">{nome}</div>
            <div class="overlay-score">{score_txt}</div>
            <button id="btnRefazer"   class="btn"></button>
            <button id="btnFinalizar" class="btn"></button>
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
            document.getElementById('btnRefazer').onclick   = function() {{ clickByText('REFAZER');   }};
            document.getElementById('btnFinalizar').onclick = function() {{ clickByText('FINALIZAR'); }};
        </script>
    </body>
    </html>
    """, height=750, width=450)

    st.markdown("""
    <style>
    div[data-testid="stButton"][st-key="btn_refazer"],
    div[data-testid="stButton"][st-key="btn_finalizar"] {
        position: absolute !important;
        top: -9999px !important;
    }
    .camuflar-botoes {
        position: fixed !important;
        bottom: -20px !important;
        left: 0 !important;
        width: 100vw !important;
        height: 200px !important;
        background: #1a73e8 !important;
        z-index: 99 !important;
        pointer-events: none !important;
    }
    </style>
    <div class="camuflar-botoes"></div>
    """, unsafe_allow_html=True)

    if st.button("REFAZER", key="btn_refazer"):
        st.session_state.resultado_enviado = False
        for k, v in DEFAULTS.items():
            st.session_state[k] = v
        st.rerun()

    if st.button("FINALIZAR", key="btn_finalizar"):
        st.session_state.page = "finalizado"
        st.rerun()
