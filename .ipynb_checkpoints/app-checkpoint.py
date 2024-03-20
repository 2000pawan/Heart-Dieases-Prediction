# Import Important Library.

import joblib
import streamlit as st 
from PIL import Image
import pandas as pd


# Load Model

model=joblib.load('model.pkl')

# load datase

df_main=pd.read_csv('test.csv')

# Load Image

image=Image.open('img.png')

# Streamlit Function For Building Button & app.

def main():
    st.image(image,width=650)
    st.title('Heart Disease Prediction')
    html_temp='''
    <div style='background-color:red; padding:12px'>
    <h1 style='color:  #000000; text-align: center;'>Heart Disease Prediction Machine Learning Model</h1>
    </div>
    <h2 style='color:  red; text-align: center;'>Please Enter Input</h2>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.number_input('Enter Your Age.',value=None)
    chest_pain= st.selectbox("(Chest_pain(0:Typical angina (chest pain related decrease blood supply to the heart) or 1: Atypical angina (chest pain not related to heart) or 2: Non-anginal pain (typically esophageal spasms) or 3: Asymptomatic (chest pain not showing signs of disease)))",df_main['chest_pain'].unique())
    blood_pressure=st.number_input('Enter Your Blood-Pressure(normal range:-(130-140)).',value=None)
    cholesterol=st.number_input('Enter Your cholesterol(above 200 is cause for concern).',value=None)
    fasting_blood_sugar= st.selectbox("Fasting-Blood-Sugar((fasting blood sugar > 120 mg/dl) (1 = above 120 or 0 = below 120)).",df_main['fasting_blood_sugar'].unique()) 
    ecg= st.selectbox("ECG (0: Nothing to note or 1: mild symptoms to severe problems signals non-normal heartbeat or 2: symptoms of abnormal heartbeat).",df_main['ecg'].unique())
    max_heart_rate=st.number_input('Maximum Heart Rate of Person(Maximum Heart Rate in per minute).',value=None)
    input=[age,chest_pain,blood_pressure,cholesterol,fasting_blood_sugar,ecg,max_heart_rate]
    result=''
    if st.button('Predict',''):
        result=prediction(input)
    temp='''
     <div style='background-color:navy; padding:8px'>
     <h1 style='color: gold  ; text-align: center;'>{}</h1>
     </div>
     '''.format(result)
    st.markdown(temp,unsafe_allow_html=True)
    


# Prediction Function to predict from model.

def prediction(input):
    test=[input]
    predict=model.predict(test)
    if predict==0:
        return ("Hello Dear! It's great to hear that you're not experiencing any symptoms related to heart disease. Remember to keep up with your healthy lifestyle choices and regular check-ups to maintain your well-being. If you ever have any health concerns or questions, feel free to reach out. Wishing you continued good health and happiness! 😊😊😊😊😊")
    else:
        return ("Hello Dear! Your heart disease prediction indicates symptoms present. It's crucial to prioritize your health and seek medical attention promptly. Consulting with a doctor can provide vital support and guidance for your well-being.😔😔😔😔😔")


if __name__=='__main__':
    main()


