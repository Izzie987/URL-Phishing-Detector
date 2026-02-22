import streamlit as st
import joblib
import numpy as np
from urllib.parse import urlparse

# Load trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Feature extraction function
def extract_features(url):
    features = []
    
    parsed = urlparse(url)
    
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
    
    suspicious_words = [
        'login', 'secure', 'bank', 'verify',
        'update', 'account', 'confirm',
        'password', 'signin', 'wp', 'webscr'
    ]
    
    features.append(sum(word in url.lower() for word in suspicious_words))
    
    return np.array(features).reshape(1, -1)

# ---------------- UI ----------------
st.title("🔐 Phishing URL Detector")
st.write("Enter a URL to check if it is Safe or Phishing.")

url_input = st.text_input("Enter URL")

if st.button("Check"):
    if url_input:
        features = extract_features(url_input)
        features = scaler.transform(features)
        
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        
        if prediction == 1:
            st.error(f"⚠️ PHISHING detected! (Confidence: {probability:.2f})")
        else:
            st.success(f"✅ SAFE URL (Confidence: {1 - probability:.2f})")
    else:
        st.warning("Please enter a URL.")