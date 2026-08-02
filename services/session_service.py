"""
Session state management.
"""

import streamlit as st


class SessionService:

    DEFAULTS = {
        "expression": "",
        "memory": 0.0,
        "precision": 6,
        "angle_mode": "Radians",
    }

    @classmethod
    def initialize(cls):

        for key, value in cls.DEFAULTS.items():
            if key not in st.session_state:
                st.session_state[key] = value