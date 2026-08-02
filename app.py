import streamlit as st

st.set_page_config(
    page_title="Engineering Calculator Suite",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧮 Engineering Calculator Suite")

st.markdown(
    """
Welcome to the **Engineering Calculator Suite**.

Use the sidebar to navigate between modules.

Current Status:
- ✅ Project Initialized
- 🚧 Scientific Calculator
- 🚧 Graphing
- 🚧 Matrix
- 🚧 Statistics
- 🚧 Finance
- 🚧 Programmer
- 🚧 Unit Converter
"""
)