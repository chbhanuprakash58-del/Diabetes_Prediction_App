# import streamlit as st
# import requests

# st.title("🩺 Diabetes Prediction System")
# st.write("Enter your health details below:")

# # Take user input
# preg = st.number_input("Pregnancies", 0, 20)
# glucose = st.number_input("Glucose Level", 0, 200)
# bp = st.number_input("Blood Pressure", 0, 150)
# skin = st.number_input("Skin Thickness", 0, 100)
# insulin = st.number_input("Insulin Level", 0, 900)
# bmi = st.number_input("BMI", 0.0, 70.0)
# dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
# age = st.number_input("Age", 1, 120)

# # When user clicks predict
# if st.button("Predict"):
#     input_data = {
#         "pregnancies": preg,
#         "glucose": glucose,
#         "blood_pressure": bp,
#         "skin_thickness": skin,
#         "insulin": insulin,
#         "bmi": bmi,
#         "dpf": dpf,
#         "age": age
#     }

#     try:
#         # Call FastAPI
#         response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
#         if response.status_code == 200:
#             result = response.json()["prediction"]
#             st.success(f"Prediction: {result}")
#         else:
#             st.error("Error: Could not get response from API")
#     except:
#         st.error("Error: Make sure FastAPI server is running")



################ here it shows references expample values#############

# import streamlit as st
# import requests

# st.title("🩺 Diabetes Prediction System")
# st.write("Enter your health details below:")

# # Show example reference values side by side
# st.subheader("Reference Example Values")
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("**Diabetic Example**")
#     st.write("""
#     Pregnancies: 5  
#     Glucose: 180  
#     Blood Pressure: 85  
#     Skin Thickness: 30  
#     Insulin: 130  
#     BMI: 35.0  
#     DPF: 0.8  
#     Age: 45
#     """)

# with col2:
#     st.markdown("**Non-Diabetic Example**")
#     st.write("""
#     Pregnancies: 2  
#     Glucose: 120  
#     Blood Pressure: 70  
#     Skin Thickness: 20  
#     Insulin: 79  
#     BMI: 25.6  
#     DPF: 0.5  
#     Age: 33
#     """)

# # Take user input
# preg = st.number_input("Pregnancies", 0, 20)
# glucose = st.number_input("Glucose Level", 0, 200)
# bp = st.number_input("Blood Pressure", 0, 150)
# skin = st.number_input("Skin Thickness", 0, 100)
# insulin = st.number_input("Insulin Level", 0, 900)
# bmi = st.number_input("BMI", 0.0, 70.0)
# dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
# age = st.number_input("Age", 1, 120)

# # Predict button
# if st.button("Predict"):
#     input_data = {
#         "pregnancies": preg,
#         "glucose": glucose,
#         "blood_pressure": bp,
#         "skin_thickness": skin,
#         "insulin": insulin,
#         "bmi": bmi,
#         "dpf": dpf,
#         "age": age
#     }

#     try:
#         # Call FastAPI
#         response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
#         if response.status_code == 200:
#             result = response.json()["prediction"]
#             if result == "Diabetic":
#                 st.error(f"Prediction: {result}")
#             else:
#                 st.success(f"Prediction: {result}")
#         else:
#             st.error("Error: Could not get response from API")
#     except:
#         st.error("Error: Make sure FastAPI server is running")





#####We can simplify your project so it doesn’t need FastAPI — the Streamlit app will load the trained model directly and make predictions.####


import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")
st.title("🩺 Diabetes Prediction System")
st.write("Enter your health details below:")

# Show example reference values side by side
st.subheader("Reference Example Values")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Diabetic Example**")
    st.write("""
    Pregnancies: 5  
    Glucose: 180  
    Blood Pressure: 85  
    Skin Thickness: 30  
    Insulin: 130  
    BMI: 35.0  
    DPF: 0.8  
    Age: 45
    """)

with col2:
    st.markdown("**Non-Diabetic Example**")
    st.write("""
    Pregnancies: 2  
    Glucose: 120  
    Blood Pressure: 70  
    Skin Thickness: 20  
    Insulin: 79  
    BMI: 25.6  
    DPF: 0.5  
    Age: 33
    """)

# Take user input
preg = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose Level", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin Level", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 120)

# Load the trained model and scaler
@st.cache_resource
def load_model():
    model = pickle.load(open("model/diabetes_model.pkl", "rb"))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))
    return model, scaler

model, scaler = load_model()

# Predict button
if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]

    if prediction == 1:
        st.error("Prediction: Diabetic")
    else:
        st.success("Prediction: Not Diabetic")
