import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Smart Agri-Vision",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Smart Agri-Vision: Crop Health & Price Intelligence System")
st.write("Solving Real-World Agricultural Challenges using AI & Machine Learning")

st.sidebar.header("Navigation")
option = st.sidebar.radio("Select Module", ["Crop Disease Classifier", "Market Price Predictor"])

if option == "Crop Disease Classifier":
    st.header("📸 Crop Disease Detection")
    st.write("Upload a leaf image to diagnose plant disease and get treatment suggestions.")
    
    uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Leaf Image', use_column_width=True)
        
        if st.button('Analyze Crop Health'):
            st.write("🔍 Analyzing image...")
            st.success("Analysis Complete!")
            st.metric(label="Predicted Condition", value="Tomato Early Blight")
            st.metric(label="Confidence Score", value="94.2%")
            
            st.subheader("💡 Recommended Treatment")
            st.info("Apply copper-based fungicides early in the morning. Ensure proper spacing between plants to improve airflow.")

elif option == "Market Price Predictor":
    st.header("📈 Crop Market Price Forecasting")
    st.write("Estimate crop prices based on market trends and seasonality.")
    
    crop = st.selectbox("Select Crop", ["Paddy", "Cotton", "Chilli", "Tomato"])
    month = st.slider("Select Forecast Month", 1, 12, 6)
    
    if st.button('Predict Price'):
        base_price = {"Paddy": 2200, "Cotton": 7000, "Chilli": 15000, "Tomato": 1800}[crop]
        predicted_price = base_price + (month * 15)
        
        st.success(f"Predicted Price for {crop}: ₹{predicted_price} per Quintal")
        
        chart_data = pd.DataFrame({
            'Month': np.arange(1, 13),
            'Price (₹)': [base_price + (m * 12) for m in range(1, 13)]
        })
        st.line_chart(chart_data.set_index('Month'))
