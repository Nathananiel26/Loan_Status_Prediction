import streamlit as st
import joblib

import streamlit as st
import numpy as np

# Title of the app
st.title("Loan Application Form")

# Instructions
st.write("Please fill in the details below to submit your loan application:")

with st.form(key='Loan'):
    Gender = st.selectbox(label='Select your gender', options=['Male', 'Female'])
    Gender_val = 1 if Gender == 'Male' else 0
    
    Marriedd = st.selectbox(label='Are you married ?',options=['Yes','No'])
    Marriedd_val = 1 if Marriedd == 'Yes' else 0
    
    Dependents = st.number_input('Enter the number of your chilredn',min_value=0,max_value=200000)
    
    education = st.selectbox(label='Are you educated ?',options=['Graduate','Not Graduate'])
    education_val = 1 if education == 'Graduate' else 0

    employed = st.selectbox(label='Are you self employed ?',options=['Yes','No'])
    employed_val = 1 if employed == 'Yes' else 0

    ApplicantIncome = st.number_input('Enter your income amount',min_value=0,max_value=200000)

    CoapplicantIncome = st.number_input('Enter co-applicant income amount',min_value=0,max_value=200000)

    LoanAmount = st.number_input('Enter amount to request ?',min_value=0,max_value=200000)

    LoanTerm= st.selectbox(label='Select loan term ?',options=[360,720])

    Credit_History = st.selectbox(label='Select loan term ?',options=[1,0])

    PropertyArea = st.selectbox(label='Select your Property Area',options=['Rural', 'Urban', 'Semiurban'])
    PropertyArea_val = 0
    if PropertyArea == 'Rural':
        PropertyArea_val = 1
    elif PropertyArea == 'Urban':
        PropertyArea_val = 2
    else :
        PropertyArea_val = 3


    display_button = st.form_submit_button(label='Predict')

if display_button:
    model = joblib.load('Loan_model')
    result = model.predict([[Gender_val,Marriedd_val,Dependents,education_val,employed_val,ApplicantIncome,CoapplicantIncome,LoanAmount,LoanTerm, Credit_History,PropertyArea_val ]])
    st.success(f'Your Medical Insurance Price is :{result}')
    st.balloons()


