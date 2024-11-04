import streamlit as st

def columns(days_bike_rent_df_count, reg_df, cas_df):
    st.header('Bike Rent Dashboard')

    st.subheader('Daily Rent')
    col1, col2, col3 = st.columns(3)

    with col1:
        total_orders = days_bike_rent_df_count.count_cr.sum()
        st.metric("Total Rented", value=total_orders)

    with col2:
        total_sum = reg_df.register_sum.sum()
        st.metric("Total Registered Rent", value=total_sum)

    with col3:
        total_sum = cas_df.casual_sum.sum()
        st.metric("Total Casual Rent", value=total_sum)