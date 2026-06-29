# Machine Learning-Based Phishing URL Detector

## Overview

The Machine Learning-Based Phishing URL Detector is a full-stack web application that analyzes URLs and determines whether they are **Safe** or **Phishing**. The project combines a Random Forest machine learning model with rule-based URL analysis to improve detection reliability.

The application consists of:

* A custom HTML/CSS/JavaScript frontend
* A Node.js (Express.js) backend
* A FastAPI machine learning API
* A Random Forest classifier trained using Scikit-learn

## Features

* Detects phishing URLs using Machine Learning.
* Performs rule-based URL analysis.
* Combines ML prediction and heuristic rules to generate the final result.
* Displays:
  * Safe/Phishing prediction
  * Confidence score
  * Risk score
* Responsive and user-friendly interface.

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Node.js
* Express.js
* Axios

### Machine Learning

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Joblib

## Working

1. The user enters a URL in the web interface.
2. The frontend sends the URL to the Express.js backend.
3. The backend forwards the request to the FastAPI service.
4. FastAPI extracts URL features and uses the trained Random Forest model to generate a prediction and confidence score.
5. Express.js performs additional rule-based analysis.
6. Both results are combined to determine the final verdict.
7. The result is displayed to the user.

## Machine Learning Features

The model extracts several features from each URL, including:

* URL length
* Number of dots
* Number of hyphens
* '@' symbol count
* Number of digits
* HTTPS usage
* Domain length
* Suspicious keywords
* Additional URL characteristics

## Rule-Based Analysis

The application also checks for common phishing indicators such as:

* Long URLs
* '@' symbols
* Multiple subdomains
* Numeric characters
* Suspicious keywords:

  * login
  * verify
  * secure
  * bank

The rule score is combined with the machine learning prediction to improve overall decision making.

## Model performance

Accuracy: approx. 85%

## Installation

### Install Python dependencies

```bash
pip install -r requirements.txt
```

### Install Node.js dependencies

```bash
cd backend
npm install
```

---

## Running the Project

### Start the FastAPI server

```bash
cd ml-api
python -m uvicorn app:app --reload
```

### Start the Express.js backend

```bash
cd backend
node server.js
```

### Launch the frontend

Open:

```
frontend/index.html
```

in your browser.

---

## Dataset

The model was trained using a phishing URL dataset from Kaggle.
Source: https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset?resource=download


