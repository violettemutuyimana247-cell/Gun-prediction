# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:49:26 2025

@author: user
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

#loaded_model = pickle.load(open('C:/Users/user/Downloads/MUTUYIMANA Violette','rb'))
import os
loaded_model=os.path.isfile(r'C:\Users\user\Downloads\MV.pkl')

with open('MV.pkl','rb') as f:
    loaded_model=pickle.load(f)
    
def Gun_Price_Prediction(age, weight, muzzle_velocity, max_range):
    # Create a dataframe for the model
    gun = pd.DataFrame([{
        'Age (in years)': age,
        'Weight (in kg)': weight,
        'Muzzle Velocity (m/s)': muzzle_velocity,
        'Max Range (m)': max_range
    }])
    
    # Predict the price
    predicted_price = loaded_model.predict(gun)
    return predicted_price[0]

def main():
    st.title('Gun Price Prediction')

    # Input fields
    age = st.text_input('Enter the Age of Gun (in years)')
    weight = st.text_input('Enter the Weight (in kg)')
    muzzle_velocity = st.text_input('Enter the Muzzle Velocity (m/s)')
    max_range = st.text_input('Enter the Max Range (m)')

    if st.button('Predict Price'):
        try:
            # Convert inputs to numeric types
            age = float(age)
            weight = float(weight)
            muzzle_velocity = float(muzzle_velocity)
            max_range = float(max_range)
            
            # Get prediction
            price = Gun_Price_Prediction(age, weight, muzzle_velocity, max_range)
            st.success(f'The predicted price for the Gun is: $ {price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for Age, Weight, Muzzle Velocity, and Max Range.")

if __name__ == '__main__':
    main()
