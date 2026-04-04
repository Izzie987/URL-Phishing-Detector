import streamlit as st
import joblib
import numpy as np
from urllib.parse import urlparse
#Load model scaler
model= joblib.load("model.pkl")
scaler= joblib.load("scaler.pkl")
#Feature extraction
def extract_features(url):
    features= []
    parsed= urlparse(url)
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    features.append(url.count('?'))
    features.append(url.count('&'))
    features.append(url.count('='))
    features.append(url.count('/'))
    features.append(sum(c.isdigit() for c in url))
    features.append(1 if parsed.scheme == "https" else 0)
    features.append(len(parsed.netloc))
    suspicious_words= ['login', 'secure', 'bank', 'verify','update', 'account', 'confirm','password', 'signin', 'wp', 'webscr']
    features.append(sum(word in url.lower() for word in suspicious_words))
#UI
st.title("Phishing URL Detector")
st.write("Enter URL to check if it's Safe or Phishing.")
url_input= st.text_input("Enter URL")
if st.button("Check"):
    if url_input:
        features= extract_features(url_input)
        features= scaler.transform(features)
        prediction= model.predict(features)[0]
        probability= model.predict_proba(features)[0][1]
        if prediction == 1:
            st.error(f"PHISHING detected! (Confidence: {probability:.2f})")
        else:
            st.success(f"SAFE URL (Confidence: {1 - probability:.2f})")
    else:
        st.warning("Please enter a URL.")