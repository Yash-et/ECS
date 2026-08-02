import streamlit as st

from core.scientific import ScientificEngine
from services.session_service import SessionService
from components.keypad import draw_keypad

SessionService.initialize()

st.title("🧮 Scientific Calculator")

col1, col2 = st.columns([4, 1])

with col1:

    st.session_state.expression = st.text_input(
        "Expression",
        value=st.session_state.expression,
    )

with col2:

    st.selectbox(
        "Mode",
        ["Radians", "Degrees"],
        key="angle_mode",
    )

st.slider(
    "Precision",
    min_value=2,
    max_value=15,
    key="precision",
)

draw_keypad()

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("Calculate", use_container_width=True):

        try:

            result = ScientificEngine.evaluate(
                st.session_state.expression
            )

            if isinstance(result, float):

                result = round(
                    result,
                    st.session_state.precision,
                )

            st.success(result)

        except Exception as e:

            st.error(str(e))

with col2:

    if st.button("⌫", use_container_width=True):

        st.session_state.expression = (
            st.session_state.expression[:-1]
        )

        st.rerun()

with col3:

    if st.button("Clear", use_container_width=True):

        st.session_state.expression = ""

        st.rerun()

with col4:

    if st.button("Copy", use_container_width=True):

        st.info("Copy feature coming soon.")