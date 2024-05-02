import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the model
model = pickle.load(open('catboostModel.pkl', 'rb'))


st.title("Taxi Fare Prediction 🚕")

day = st.selectbox("Select day", 
                   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

hour = st.number_input("hour", min_value=0, max_value=23)  
minute = st.number_input("minute", min_value=0, max_value=59)
distance = st.number_input("Distance (meters)", min_value=0) 
pickup_area = st.number_input("Pickup Commnunity Area", min_value=1)
dropoff_area = st.number_input("Dropoff Commnunity Area", min_value=1)
pickup_census = st.number_input("Pickup Census Tract", min_value=1)
dropoff_census = st.number_input("Dropoff Census Tract", min_value=1)

if st.button('Predict'):
    weekday_value = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday': 5, 'Sunday':6 }[day]
    time = hour*4 + round(minute/15)
    features = [pickup_census, dropoff_census, pickup_area, dropoff_area, weekday_value, time, distance]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)[0]

    st.success(f'Predicted Fare: ${prediction}')
