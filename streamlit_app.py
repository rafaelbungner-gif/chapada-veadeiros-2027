from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Chapada a dois · Julho 2027", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")

st.html("""<style>
header[data-testid="stHeader"]{display:none}
.stMainBlockContainer{padding:0!important;max-width:none!important}
[data-testid="stVerticalBlock"]{gap:0}
iframe[title$=".guide"]{width:100%;height:100dvh;border:0;display:block}
</style>""")

guide = components.declare_component("guide", path=str(Path(__file__).parent / "site"))
guide(key="chapada")
