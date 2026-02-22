import pandas as pd
import numpy as np
import joblib
import re
from urllib.parse import urlparse

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler


# ===============================
# Feature Extraction Function
# ===============================
def extract_features(url):
    features = []
    
    parsed = urlparse(url)
    
    # Basic structural features
    features.append(len(url))  # URL length
    features.append(url.count('.'))  # number of dots
    features.append(url.count('-'))  # hyphens
    features.append(url.count('@'))  # @ symbol
    features.append(url.count('?'))  # query symbol
    features.append(url.count('&'))  # parameter count
    features.append(url.count('='))  # assignment count
    features.append(url.count('/'))  # number of subdirectories
    
    # Digit count
    features.append(sum(c.isdigit() for c in url))
    
    # HTTPS usage
    features.append(1 if parsed.scheme == "https" else 0)
    
    # Domain length
    features.append(len(parsed.netloc))
    
    # Suspicious words
    suspicious_words = [
        'login', 'secure', 'bank', 'verify',
        'update', 'account', 'confirm',
        'password', 'signin', 'wp', 'webscr'
    ]
    
    features.append(sum(word in url.lower() for word in suspicious_words))
    
    return features


# ===============================
# Load Dataset
# ===============================
data = pd.read_csv("dataset_phishing.csv")

# Convert label
data['label'] = data['status'].str.lower().map({
    'legitimate': 0,
    'phishing': 1
})

# Drop missing rows if any
data = data.dropna()

# Extract Features
X = data['url'].apply(extract_features)
X = np.array(X.tolist())
y = data['label']

# ===============================
# Train Test Split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Scaling (helps consistency)
# ===============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ===============================
# Train Model (Random Forest)
# ===============================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)

# ===============================
# Evaluate
# ===============================
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print("\nClassification Report:\n")
print(classification_report(y_test, preds))

# ===============================
# Save Model + Scaler
# ===============================
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel and scaler saved successfully!")