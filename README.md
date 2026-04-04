Phishing URL Detector:
An ML-based web app that detects whether a URL is legitimate or phishing.

Features include:
- URL feature extraction
- Random Forest classifier
- Probability-based confidence scoring
- Streamlit web interface

Libraries used:
- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy

Model Performance:
- Accuracy: approx. ~84%

How to Run/Execute:
1. Install:
   pip install -r requirements.txt
2. Train model:
   python train_model.py
3. Run app:
   streamlit run app.py

Dataset:
Sourced from Kaggle: https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset?resource=download