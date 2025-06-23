# 🧠 CIFAR-10 Image Classifier Web App

This project is a web-based image classification tool built with TensorFlow and Streamlit. It uses a Convolutional Neural Network (CNN) to classify images into one of 10 categories from the CIFAR-10 dataset.

🌐 **Live Demo**: [Click here to open the Streamlit app](https://imageclassifier-74eszbunvulerpiixj5tbb.streamlit.app)

---

## 📌 Features

- Upload any image file for prediction
- Pretrained CNN model on CIFAR-10 dataset
- Predicts image class with confidence score
- Clean, minimal UI using Streamlit

---

## 🧠 Model Details

- **Input Shape**: 32x32x3
- **Architecture**:
  - Conv2D + BatchNorm + MaxPooling + Dropout
  - Fully connected Dense layers
  - Output: 10-class softmax
- **Optimizer**: Adam (lr = 0.0005)
- **Loss Function**: Categorical Crossentropy
- **Test Accuracy**: ~79%

---

## 🔢 CIFAR-10 Classes

0 - airplane
1 - automobile
2 - bird
3 - cat
4 - deer
5 - dog
6 - frog
7 - horse
8 - ship
9 - truck


---

## 📁 Project Structure

image_classifier/
├── app.py # Streamlit app
├── predict.py # Model loading and prediction
├── cifar10cnn_model.h5 # Trained model
├── requirements.txt # Main dependencies
├── packages.txt # Additional packages for deployment
└── README.md # This file


---

## 🚀 Run the App Locally

```bash
git clone https://github.com/Logicrithm/image_classifier.git
cd image_classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
