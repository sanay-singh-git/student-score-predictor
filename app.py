import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("final_model.pkl")

st.title("Student Math Score Predictor")

gender = st.selectbox("Gender", ['female', 'male'])
race = st.selectbox("Race/Ethnicity", ['group A', 'group B', 'group C', 'group D', 'group E'])
parent_edu = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
prep_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading = st.slider("Reading Score", 0, 100, 50)
writing = st.slider("Writing Score", 0, 100, 50)

if st.button("Predict Math Score"):
    input_df = pd.DataFrame([{
        'gender': gender,
        'race/ethnicity': race,
        'parental level of education': parent_edu,
        'lunch': lunch,
        'test preparation course': prep_course,
        'reading score': reading,
        'writing score': writing
    }])
    
    prediction = model.predict(input_df)
    st.success(f"Predicted Math Score: {prediction[0]:.2f}")
