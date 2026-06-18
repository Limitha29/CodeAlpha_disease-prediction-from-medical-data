# Disease Prediction System

## Overview

The Disease Prediction System is a Machine Learning based web application that predicts the likelihood of diseases based on patient health data. The system supports prediction for:

* Heart Disease
* Diabetes
* Breast Cancer

Users can select a disease, enter the required medical parameters, and receive an instant prediction through a user-friendly interface.

---

## Features

* Predicts Heart Disease risk
* Predicts Diabetes risk
* Predicts Breast Cancer risk
* Interactive and responsive frontend
* Flask backend API
* Machine Learning models using Random Forest Classifier
* Real-time prediction results

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* NumPy
* Pandas
* Joblib

---

## Project Structure

Disease-Prediction-System/

├── backend/

│   ├── app.py

│   ├── train_models.py

│   ├── heart_model.pkl

│   ├── diabetes_model.pkl

│   └── cancer_model.pkl

│

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── script.js

│

└── README.md

---

## Installation

### Clone Repository

git clone https://github.com/your-username/Disease-Prediction-System.git

cd Disease-Prediction-System

### Install Dependencies

pip install flask flask-cors scikit-learn pandas numpy joblib

### Train Models

python train_models.py

### Run Backend

python app.py

### Run Frontend

Open index.html using Live Server in VS Code.

---

## How It Works

1. Select a disease from the dropdown menu.
2. Enter the required health parameters.
3. Click the Predict button.
4. The data is sent to the Flask backend.
5. The Machine Learning model processes the input.
6. The prediction result is displayed instantly.

---

## Machine Learning Models

| Disease       | Algorithm     |
| ------------- | ------------- |
| Heart Disease | Random Forest |
| Diabetes      | Random Forest |
| Breast Cancer | Random Forest |

---

## Future Enhancements

* Add more disease prediction models
* Improve model accuracy with larger datasets
* User authentication system
* Prediction history tracking
* Deployment on cloud platforms

---

## Author

Limitha

---

## License

This project is developed for educational and learning purposes.
