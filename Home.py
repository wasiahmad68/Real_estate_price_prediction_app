import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)


st.write("# Welcome to Streamlit! 👋")

st.markdown("""
## Gurgaon Real Estate Price Prediction App

This project is a data-driven web application for predicting property prices in Gurgaon. It leverages machine learning models trained on real estate data to provide price estimates for flats and houses based on user inputs such as location, property type, number of bedrooms, amenities, and more.

**Features:**
- Predict property prices for Gurgaon using advanced ML models
- Interactive analytics and visualizations
- Explore sector-wise trends and property features

**How to use:**
1. Use the sidebar to navigate between the Home, Price Predictor, and Analysis pages.
2. On the Price Predictor page, enter property details to get an estimated price range.
3. On the Analysis page, explore trends and insights about Gurgaon real estate.
""")

st.sidebar.success("Select a demo above.")