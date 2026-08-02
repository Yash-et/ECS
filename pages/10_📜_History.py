import streamlit as st

from services.history_service import HistoryService

st.title("📜 Calculation History")

history = HistoryService.get_all()

if not history:

    st.info("No calculations yet.")

else:

    for expression, result, timestamp in history:

        st.code(
            f"{expression} = {result}\n{timestamp}"
        )

if st.button("Clear History"):

    HistoryService.clear()

    st.success("History cleared.")

    st.rerun()

if st.button("Export CSV"):

    from services.export_service import ExportService

    ExportService.export(history)

    st.success("history.csv exported.")