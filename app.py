import streamlit as st
from PIL import Image
import numpy as np
from predict import load_model_and_predict

st.set_page_config(page_title="CIFAR-10 Classifier", layout="centered")
st.title("CIFAR-10 Image Classifier")

uploaded_file= st.file_uploader("Upload a CIFAR-10 image (32x32 pixels)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image=Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption="Uploaded Image", use_column_width=False)
    
    if st.button("Predict"):
        with st.spinner("Classifying..."):
            class_name, prob= load_model_and_predict(image)
            st.success(f"Predicted Class: {class_name} ({prob:.2f}% confidence)")
            

