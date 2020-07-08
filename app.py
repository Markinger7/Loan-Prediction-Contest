#imports
import numpy as np
import pandas as pd

import streamlit as st

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle

from PIL import Image

##### load final model #####
filename = 'final_class.sav'
final_model = pickle.load(open(filename, 'rb'))


st.title('Loan Predictions')

image = Image.open('loan.jpg')
st.image(image, use_column_width=True)

st.write('Plese input your data to get an automatic prediction if your eligible for a loan')


##### sidebar #####

#st.sidebar.info()



##### user inputs #####
# Income
income = st.number_input('Monthly applicant income', min_value=0, value=2000)

# Co Income
co_income = st.number_input('Monthly coapplicant income', min_value=0, value=0)

# Loan Amount
loan_amount = st.number_input('Loan Amount in thousand', min_value=0, value=50)

# Loan Amount Term 
loan_amount_term = st.number_input('Term of loan in months', min_value=0, value=100)

# Gender
gender = st.selectbox('Gender', ['male', 'female'])

# Married
married = st.selectbox('Married', ['yes', 'no'])

# Dependents
dependents = st.selectbox('Number of dependents', ['0', '1', '2', '3+'])

# Graduated (0-y / 1-n)
graduated = st.selectbox('Applicant Education', ['Graduate', 'Not Graduated'])

# Self employed (0-n / 1-y)
self_employed = st.selectbox('Self employed', ['Yes', 'No'])

# Property Area
property_area = st.selectbox('Property Area', ['Urban', 'Semi Urban', 'Rural'])


##### Calulate Features #####
# TotalIncomeLog
total_Income_Log = np.log(income + co_income)

# EMI
EMI = loan_amount / loan_amount_term

# BalanceIncome
Balance_Income = income + co_income - (EMI * 1000)

##### assign values to cat features #####
# Gender_male
if gender == 'male':
    gender = 1
else:
    gender = 0
    
# married
if married == 'yes':
    married = 1
else:
    married = 0
    
# dependents 
if dependents == '1':
    dependents_1 = 1
else:
    dependents_1 = 0
    
if dependents == '2':
    dependents_2 = 1
else:
    dependents_2 = 0
    
if dependents == '3+':
    dependents_3 = 1
else:
    dependents_3 = 0
    
# Education
if graduated == 'Not Graduated':
    not_graduated = 1
else:
    not_graduated = 0

# Self Employed
if self_employed == 'Yes':
    self_employed_yes = 1
else:
    self_employed_yes = 0

# Property Area
if property_area == 'Semi Urban':
    property_area_semiurban = 1
else:
    property_area_semiurban = 0

if property_area == 'Urban':
    property_area_urban = 1
else:
    property_area_urban = 0



##### Create Input DataFrame #####
input_dict = {'TotalIncomeLog': total_Income_Log, 'EMI': EMI, 'BalanceIncome': Balance_Income, 'Gender_male': gender, 
              'Married_yes': married, 'Dependents_1': dependents_1, 'Dependents_2': dependents_2, 'Dependents_3': dependents_3,
              'Education_not_graduated': not_graduated, 'Self_Employed_yes': self_employed_yes, 
              'Property_Area_Semiurban': property_area_semiurban, 'Property_Area_urban': property_area_urban}
input_df = pd.DataFrame([input_dict])



##### test inputs #####
# st.dataframe(input_df)



# make prediction with data
if st.button('Predict'):
    output = final_model.predict(input_df)
    
    if output == 1:
        st.write('Loan is approved')
    else:
        st.write('Loan is not approved')
    