import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np


def sellingCharts(days_df):
    st.subheader("Chart of company sales performance in recent years")

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        days_df["dteday"],
        days_df["count_cr"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

def sellingHoursRentChart(sum_order_items_df):
    st.subheader("Chart Comparison of the number of bike renters with Hours")
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

    sns.barplot(x="hours", y="count_cr", data=sum_order_items_df.head(5), palette=["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3"], ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Hours (PM)", fontsize=30)
    ax[0].set_title("Hours with lots of bike renters", loc="center", fontsize=30)
    ax[0].tick_params(axis='y', labelsize=35)
    ax[0].tick_params(axis='x', labelsize=30)

    sns.barplot(x="hours", y="count_cr", data=sum_order_items_df.sort_values(by="hours", ascending=True).head(5), palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#90CAF9"], ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Hours (AM)",  fontsize=30)
    ax[1].set_title("Hours with few bike renters", loc="center", fontsize=30)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].tick_params(axis='y', labelsize=35)
    ax[1].tick_params(axis='x', labelsize=30)

    st.pyplot(fig)

def seasonRentChart(season_df):
    st.subheader("Comparative chart of Rental Amount and Season")

    colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9"]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
            y="count_cr", 
            x="season",
            data=season_df.sort_values(by="season", ascending=False),
            palette=colors,
            ax=ax
        )
    ax.set_title("Inter-Seasonal Chart", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

def rentTypeDistribution():
    st.subheader("Comparative chart between registered and casual customers")

    labels = 'casual', 'registered'
    sizes = [18.8, 81.2]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors=["#D3D3D3", "#90CAF9"],
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

def heatmapCorrelationVIew(hours_bike_rent_df):
    st.subheader("Correlation Heatmap between rental amount and all indicator")
    numeric_df = hours_bike_rent_df.select_dtypes(include=[np.number])

    corr_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')

    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)