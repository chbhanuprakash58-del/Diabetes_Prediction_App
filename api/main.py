# from fastapi import FastAPI
# from pydantic import BaseModel
# import numpy as np
# import pickle

# app = FastAPI(title="Diabetes Prediction API")

# # Load trained model and scaler
# model = pickle.load(open("model/diabetes_model.pkl", "rb"))
# scaler = pickle.load(open("model/scaler.pkl", "rb"))

# # Define input data structure
# class UserData(BaseModel):
#     pregnancies: float
#     glucose: float
#     blood_pressure: float
#     skin_thickness: float
#     insulin: float
#     bmi: float
#     dpf: float
#     age: float

# @app.get("/")
# def home():
#     return {"message": "Diabetes Prediction API is running"}

# @app.post("/predict")
# def predict(data: UserData):
#     # Convert input data to numpy array
#     features = np.array([[data.pregnancies, data.glucose, data.blood_pressure,
#                           data.skin_thickness, data.insulin, data.bmi,
#                           data.dpf, data.age]])
    
#     # Scale features
#     scaled_features = scaler.transform(features)
    
#     # Predict
#     prediction = model.predict(scaled_features)
    
#     result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
#     return {"prediction": result}
