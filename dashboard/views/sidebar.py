import streamlit as st

def viewSidebar(min_date_days, max_date_days):
    with st.sidebar:
        st.image("https://cdn.vectorstock.com/i/1000x1000/21/37/logo-for-bicycle-rental-vector-25512137.webp")

        start_date, end_date = st.date_input(
            label='Date Range',
            min_value=min_date_days,
            max_value=max_date_days,
            value=[min_date_days, max_date_days])

    return start_date, end_date