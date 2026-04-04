import pandas as pd
import numpy as np
import joblib
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
#Feature extract
def extract_features(url):
    features = []
    parsed = urlparse(url)
    features.append(len(url)) #URL length
    features.append(url.count('.')) #no. of dots
    features.append(url.count('-')) #hyphens
    features.append(url.count('@')) #@ symbol
    features.append(url.count('?')) #? symbol
    features.append(url.count('&')) #& count
    features.append(url.count('=')) #= count
    features.append(url.count('/')) #no. of /
    #Digit count
    features.append(sum(c.isdigit() for c in url))
    #HTTPS usage
    features.append(1 if parsed.scheme == "https" else 0)
    #Domain length
    features.append(len(parsed.netloc))
    
    #Suspicious words
    suspicious_words= ['login', 'secure', 'bank', 'verify','update', 'account', 'confirm','password', 'signin', 'wp', 'webscr']
    features.append(sum(word in url.lower() for word in suspicious_words))
    return features
#Load Data
data = pd.read_csv("dataset_phishing.csv")

data['label'] = data['status'].str.lower().map({'legitimate': 0,'phishing': 1})
#Drop missing rows 
data = data.dropna()
#Extract features
X = data['url'].apply(extract_features)
X = np.array(X.tolist())
y = data['label']
#Train Test split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)
#Scaling 
scaler= StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)
#Train Model (Random Forest)
model= RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)
model.fit(X_train, y_train)
#Evaluate
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))
print("\nClassification Report:\n")
print(classification_report(y_test, preds))

joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("\nModel and scaler saved successfully!")