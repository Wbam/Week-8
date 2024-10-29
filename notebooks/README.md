# Fraud Detection Project

## Overview
This project aims to enhance the detection of fraud cases for e-commerce and banking transactions using advanced machine learning models and geolocation analysis. The project involves analyzing transaction data, building and deploying models, and creating a dashboard for visualization of fraud insights.

## Table of Contents
- [Technologies](#technologies)
- [Datasets](#datasets)
- [Tasks Overview](#tasks-overview)
  - [Task 1: Data Analysis and Preprocessing](#task-1-data-analysis-and-preprocessing)
  - [Task 2: Model Building and Training](#task-2-model-building-and-training)
  - [Task 3: Model Explainability](#task-3-model-explainability)
  - [Task 4: Model Deployment and API Development](#task-4-model-deployment-and-api-development)
  - [Task 5: Build a Dashboard with Flask and Dash](#task-5-build-a-dashboard-with-flask-and-dash)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies
- **Python 3.10**
- **Flask**: For building the API.
- **Dash**: For creating the dashboard.
- **Joblib**: For loading machine learning models.
- **Pandas**: For data manipulation and analysis.
- **Plotly**: For visualizations.

## Datasets
1. **Fraud_Data.csv**: E-commerce transaction data for identifying fraudulent activities.
   - Features: `user_id`, `signup_time`, `purchase_time`, `purchase_value`, `device_id`, `source`, `browser`, `sex`, `age`, `ip_address`, `class`.
2. **IpAddress_to_Country.csv**: Maps IP addresses to countries.
   - Features: `lower_bound_ip_address`, `upper_bound_ip_address`, `country`.
3. **Creditcard.csv**: Bank transaction data curated for fraud detection analysis.
   - Features: `Time`, `V1` to `V28`, `Amount`, `Class`.

## Tasks Overview

### Task 1: Data Analysis and Preprocessing
- **Handle Missing Values**: Imputed or dropped missing values.
- **Data Cleaning**: Removed duplicates and corrected data types.
- **Exploratory Data Analysis (EDA)**: Conducted univariate and bivariate analysis.
- **Merge Datasets for Geolocation Analysis**: Converted IP addresses to integer format and merged datasets.
- **Feature Engineering**: Created transaction frequency, velocity, and time-based features.
- **Normalization and Scaling**: Scaled numerical features.
- **Encode Categorical Features**: Encoded categorical features for model training.

### Task 2: Model Building and Training
- **Data Preparation**: Separated features and targets, and split data into training and test sets.
- **Model Selection**: Compared performance of various models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - Multi-Layer Perceptron (MLP)
  - Convolutional Neural Network (CNN)
  - Recurrent Neural Network (RNN)
  - Long Short-Term Memory (LSTM)
- **Model Training and Evaluation**: Trained and evaluated models for both credit card and fraud data.
- **MLOps Steps**: Implemented versioning and experiment tracking using MLflow.

### Task 3: Model Explainability
- **Using SHAP**: Utilized SHAP values for feature importance and model explanation.
  - Created summary, force, and dependence plots.
- **Using LIME**: Employed LIME for local interpretability and prediction explanations.

### Task 4: Model Deployment and API Development
- **Flask API**: Built a Flask application to serve the trained models.
- **Docker Setup**: Created a Dockerfile for containerization of the API.
- **Logging**: Integrated logging to monitor incoming requests and predictions.
- **API Endpoints**: Defined endpoints for making predictions with the selected model.

### Task 5: Build a Dashboard with Flask and Dash
- **Flask Endpoint**: Developed an endpoint to serve fraud data and summary statistics.
- **Dash Visualizations**: Created an interactive dashboard to visualize insights:
  - Summary statistics for total transactions, fraud cases, and fraud percentages.
  - Line chart for the number of detected fraud cases over time.
  - Geographical analysis of fraud occurrences.
  - Bar charts comparing fraud cases across different devices and browsers.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fraud_detection_project.git
   cd fraud_detection_project
