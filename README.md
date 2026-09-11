# Adsorption Prediction App

An interactive machine learning application built with **Streamlit** for predicting adsorption capacity from experimental conditions.

## Overview

This application allows users to enter experimental parameters and obtain a machine learning prediction of adsorption capacity.

The app is designed around adsorption experiments involving variables such as contact time, temperature, pH, solution volume, initial concentration, and adsorbent mass.

## Features

* Interactive input fields for experimental conditions
* Machine learning-based adsorption prediction
* Simple and user-friendly interface
* Real-time predictions
* Trained model loaded using Joblib
* Web-based interface powered by Streamlit

## Input Variables

The application can use experimental conditions including:

* Contact Time (min)
* Temperature (°C)
* pH
* Solution Volume (mL)
* Initial Concentration (mg/L)
* Adsorbent Mass (g)

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib

## Project Structure

```text
adsorption-app/
│
├── ad_app.py
├── adsorption_model.pkl
├── requirements.txt
└── README.md
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd adsorption-app
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run ad_app.py
```

The application will open in your web browser.

## Purpose

The project demonstrates how machine learning can be integrated with experimental chemistry data to create an interactive prediction tool for adsorption studies.

It also provides a foundation for developing data-driven approaches to experimental optimization and materials research.

## Author

**Victor Agbo**

B.Sc. Pure and Industrial Chemistry

Interested in the application of **machine learning, data science, and materials chemistry to sustainable energy and environmental research**.
