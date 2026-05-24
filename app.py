import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Dropout Predictor", page_icon="🎓")

st.title("🎓 AI Student Dropout Risk Predictor")
st.markdown("**For Nigerian Universities**")

st.write("Enter student details below:")

# Input fields
cgpa = st.slider("Current CGPA", 0.0, 5.0, 2.5)
attendance = st.slider("Attendance (%)", 0, 100, 70)
age = st.number_input("Age", 16, 45, 21)
gender = st.selectbox("Gender", ["Male", "Female"])
sponsorship = st.selectbox("Sponsorship", ["Self", "Parent", "Scholarship"])
level = st.selectbox("Level", ["100", "200", "300", "400"])
strike_impact = st.slider("Strike Impact (0-10)", 0, 10, 4)

if st.button("Predict Risk"):
    st.info("✅ Model would predict here (demo version)")
    st.success("Low Risk") if cgpa > 2.5 and attendance > 60 else st.error("High Risk")
    st.write("**Recommendation:** Seek academic advising if risk is high.")
