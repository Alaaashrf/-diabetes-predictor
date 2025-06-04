
import streamlit as st
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🔍 Diabetes Prediction App")
st.write("أدخل البيانات التالية للتنبؤ بمرحلة السكر:")

# Input fields (based on your dataset)
HighBP = st.selectbox("Do you have High Blood Pressure?", [0, 1])
HighChol = st.selectbox("Do you have High Cholesterol?", [0, 1])
CholCheck = st.selectbox("Have you checked your cholesterol?", [0, 1])
BMI = st.number_input("BMI", 10.0, 60.0, 25.0)
Smoker = st.selectbox("Are you a smoker?", [0, 1])
Stroke = st.selectbox("Have you had a stroke?", [0, 1])
HeartDiseaseorAttack = st.selectbox("Heart Disease or Heart Attack?", [0, 1])
PhysActivity = st.selectbox("Physical Activity in last 30 days?", [0, 1])
Fruits = st.selectbox("Do you consume fruits daily?", [0, 1])
Veggies = st.selectbox("Do you consume vegetables daily?", [0, 1])
HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption?", [0, 1])
AnyHealthcare = st.selectbox("Do you have any healthcare coverage?", [0, 1])
NoDocbcCost = st.selectbox("Did you not see a doctor due to cost?", [0, 1])
GenHlth = st.slider("General Health (1=Excellent to 5=Poor)", 1, 5, 3)
MentHlth = st.slider("Mental Health (days not good)", 0, 30, 5)
PhysHlth = st.slider("Physical Health (days not good)", 0, 30, 5)
DiffWalk = st.selectbox("Difficulty walking or climbing stairs?", [0, 1])
Sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
Age = st.slider("Age (grouped)", 1, 13, 5)
Education = st.slider("Education Level (1 = no schooling to 6 = college grad)", 1, 6, 4)
Income = st.slider("Income Level (1 = low to 8 = high)", 1, 8, 4)

# Put all features into a DataFrame
data = pd.DataFrame([[
    HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,
    PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare,
    NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income
]], columns=[
    'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
    'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
    'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
    'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income'
])

if st.button("🔍 Predict"):
    prediction = model.predict(data)[0]
    if prediction == 0:
        st.success("✅ النتيجة: لا يوجد سكر")
    elif prediction == 1:
        st.warning("⚠️ النتيجة: مرحلة ما قبل السكر")
    else:
        st.error("❗النتيجة: مصاب بالسكر")
