from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from urllib.parse import urlparse
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model= joblib.load("model.pkl")
scaler= joblib.load("scaler.pkl")
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
    sus_words = ['login','secure','bank','verify','update','account']
    features.append(sum(word in url.lower() for word in sus_words))
    return features
@app.post("/predict")
def predict(data: dict):
    url= data["url"]
    features= extract_features(url)
    features= scaler.transform([features])
    pred= model.predict(features)[0]
    prob= model.predict_proba(features)[0][1]
    return {"prediction": int(pred), "confidence": float(prob)}