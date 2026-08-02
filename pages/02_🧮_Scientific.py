import streamlit as st

from core.scientific import ScientificEngine

st.title("🧮 Scientific Calculator")

expression = st.text_input(
    "Enter Expression",
    placeholder="Example: sqrt(25)+sin(pi/2)",
)

if st.button("Calculate"):

    if expression.strip():

        try:

            result = ScientificEngine.evaluate(expression)

            st.success(result)

        except Exception as e:

            st.error(str(e))