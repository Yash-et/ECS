import streamlit as st

BUTTONS = [
    ["7", "8", "9", "/", "sqrt("],
    ["4", "5", "6", "*", "^"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "+", ")", "="],
    ["sin(", "cos(", "tan(", "log(", "ln("],
    ["pi", "e", "exp(", "factorial(", "C"],
]


def draw_keypad():
    """Render the scientific calculator keypad."""

    if "expression" not in st.session_state:
        st.session_state.expression = ""

    for row_idx, row in enumerate(BUTTONS):
        cols = st.columns(len(row))

        for col_idx, (col, button) in enumerate(zip(cols, row)):
            with col:
                if st.button(
                    button,
                    key=f"btn_{row_idx}_{col_idx}",
                    use_container_width=True,
                ):
                    if button == "C":
                        st.session_state.expression = ""
                    elif button == "=":
                        # Evaluation is handled elsewhere in the app.
                        pass
                    else:
                        st.session_state.expression += button