import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('disease_liver.sav', 'rb'))
st.text('Fernando Aji Perdana Hutapea')
st.text('191351032')
st.title('PREDICTION OF LIVER DISEASE')

col1, col2, col3 = st.columns(3)

with col1:
    Age = st.text_input('Age')
with col1:
    Gender = st.text_input('Gender')
with col1:
    Total_Bilirubin = st.text_input('Total Bilirubin')
with col1:
    Direct_Bilirubin = st.text_input('Direct Bilirubin')
with col2:
    Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')
with col2:
    Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')
with col2:
    Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')
with col3:
    Total_Protiens = st.text_input('Total Protiens')
with col3:
    Albumin = st.text_input('Albumin')
with col3:
    Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')


liver_diagnosis =''

if st.button('SUBMIT'):
    liver_prediction = model.predict([[Age,Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

    if (liver_prediction[0]==1):
        liver_diagnosis = 'Pasien tidak terindikasi penyakit liver'
    else:
        liver_diagnosis = 'Pasien terindikasi penyakit liver'

st.success(liver_diagnosis)
