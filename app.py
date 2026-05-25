import streamlit as st

st.set_page_config(page_title="RetailPulse", layout="wide")

st.sidebar.title("🛍️ RetailPulse")
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "EDA",
        "Customer Segmentation",
        "Demand Forecasting",
        "Churn Prediction",
        "Inventory Optimization",
        "Power BI Dashboard"
    ]
)

# HOME PAGE
if page == "Home":
    st.title("🛍️ RetailPulse")
    st.subheader("AI-Powered Customer Analytics & Demand Forecasting Platform")

    st.markdown("""
    ## Project Overview

    RetailPulse is an end-to-end retail analytics platform developed
    for customer analytics and demand forecasting.

    ### Features Implemented

    ✅ Data Cleaning & Preprocessing  
    ✅ Exploratory Data Analysis (EDA)  
    ✅ RFM Customer Segmentation  
    ✅ Demand Forecasting using Prophet  
    ✅ Churn Prediction using Random Forest  
    ✅ Inventory Optimization  
    ✅ Interactive Power BI Dashboard
    """)

# EDA PAGE
elif page == "EDA":
    st.title("📊 Exploratory Data Analysis")

    st.subheader("Monthly Sales Trend")
    st.image("images/monthly_sales.png", use_container_width=True)

    st.subheader("Top Selling Products")
    st.image("images/top_products.png", use_container_width=True)

    st.subheader("Top Countries by Revenue")
    st.image("images/countries_revenue.png", use_container_width=True)

    st.subheader("Revenue Distribution")
    st.image("images/revenue_distribution.png", use_container_width=True)

# CUSTOMER SEGMENTATION
elif page == "Customer Segmentation":
    st.title("👥 Customer Segmentation")
    st.write("RFM Analysis and KMeans clustering were used to segment customers.")

    st.image("images/rfm.png", use_container_width=True)

# DEMAND FORECASTING
elif page == "Demand Forecasting":
    st.title("📈 Demand Forecasting")
    st.write("30-day sales forecasting using Prophet model.")

    st.image("images/forecast.png", use_container_width=True)

# CHURN
elif page == "Churn Prediction":
    st.title("⚠️ Churn Prediction")
    st.write("Random Forest model used for churn prediction.")

    st.image("images/churn.png", use_container_width=True)

# INVENTORY
elif page == "Inventory Optimization":
    st.title("📦 Inventory Optimization")
    st.write("Inventory priority classification.")

    st.image("images/inventory.png", use_container_width=True)

# POWER BI DASHBOARD
elif page == "Power BI Dashboard":
    st.title("📊 Power BI Dashboard")

    st.subheader("Executive Summary Dashboard")
    st.image("images/dashboard1.png", use_container_width=True)

    st.subheader("Sales Analysis Dashboard")
    st.image("images/dashboard2.png", use_container_width=True)

    st.subheader("Customer Analytics Dashboard")
    st.image("images/dashboard3.png", use_container_width=True)

    st.subheader("Forecast Dashboard")
    st.image("images/dashboard4.png", use_container_width=True)

    st.subheader("Churn Dashboard")
    st.image("images/dashboard5.png", use_container_width=True)

    st.subheader("Inventory Dashboard")
    st.image("images/dashboard6.png", use_container_width=True)