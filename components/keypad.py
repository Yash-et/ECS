import streamlit as st


BUTTONS = [
    ["7", "8", "9", "/", "sqrt("],
    ["4", "5", "6", "*", "^"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "+", ")", "+"],
    ["sin(", "cos(", "tan(", "log(", "ln("],
    ["pi", "e", "exp(", "factorial(", "C"],
]


def draw_keypad():

    for row in BUTTONS:

        cols = st.columns(len(row))

        for col, button in zip(cols, row):

            with col:

                if st.button(button, use_container_width=True):

                    if button == "C":

                        st.session_state.expression = ""

                    else:

                        st.session_state.expression += button