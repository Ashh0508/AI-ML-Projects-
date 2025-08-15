# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Title
st.title("Concrete Strength Prediction App 🏗️")

# Sidebar for user input
st.sidebar.header('Input Concrete Features')

def user_input_features():
    cement = st.sidebar.slider('Cement (kg/m^3)', 100.0, 600.0, 270.0)
    blast_furnace_slag = st.sidebar.slider('Blast Furnace Slag (kg/m^3)', 0.0, 360.0, 72.0)
    fly_ash = st.sidebar.slider('Fly Ash (kg/m^3)', 0.0, 200.0, 54.0)
    water = st.sidebar.slider('Water (kg/m^3)', 100.0, 250.0, 180.0)
    superplasticizer = st.sidebar.slider('Superplasticizer (kg/m^3)', 0.0, 32.0, 6.0)
    coarse_aggregate = st.sidebar.slider('Coarse Aggregate (kg/m^3)', 800.0, 1200.0, 972.0)
    fine_aggregate = st.sidebar.slider('Fine Aggregate (kg/m^3)', 500.0, 1000.0, 780.0)
    age = st.sidebar.slider('Age (days)', 1, 365, 28)

    data = {
        'cement': cement,
        'blast_furnace_slag': blast_furnace_slag,
        'fly_ash': fly_ash,
        'water': water,
        'superplasticizer': superplasticizer,
        'coarse_aggregate': coarse_aggregate,
        'fine_aggregate': fine_aggregate,
        'age': age
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Collect user input
input_df = user_input_features()

# Load the dataset from local file
@st.cache_data
def load_data():
    data = pd.read_csv('concrete_data.csv')
    data.columns = data.columns.str.strip()  # Remove any unwanted spaces in column names
    return data

data = load_data()

# Features and target
X = data.drop(['concrete_compressive_strength'], axis=1)
y = data['concrete_compressive_strength']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Display dataset
st.subheader('Concrete Dataset Sample')
st.dataframe(data.tail())

# Show model performance
st.subheader('Model Performance')
st.write(f'Mean Squared Error: {mse:.2f}')

# Make predictions
st.subheader('Predicted Concrete Strength')
prediction = model.predict(input_df)
st.write(f'**Predicted Strength:** {prediction[0]:.2f} MPa')

# Footer
st.caption('Created with ❤️ using Streamlit')
