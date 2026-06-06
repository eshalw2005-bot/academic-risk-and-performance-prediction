import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


st.set_page_config(page_title="Academic Risk and Performance Prediction", layout="centered")
st.title("🎓 Academic Risk and Performance Prediction")
st.write("Enter the details below to predict the student's final score.")


@st.cache_resource  
def train_model():
    data = pd.read_csv('student_data.csv')
    X = data[['StudyHours', 'Attendance', 'SleepHours']]
    y = data['FinalScore']
    mdl = LinearRegression()
    mdl.fit(X, y)
    return mdl

model = train_model()


st.subheader("📊 Input Features")


with st.form("prediction_form"):
    study_hours = st.number_input("Study Hours (Daily):", min_value=0.0, max_value=24.0, value=5.0, step=0.5)
    attendance = st.number_input("Attendance (%):", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
    sleep_hours = st.number_input("Sleep Hours (Daily):", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    
    
    submit_button = st.form_submit_button(label="Predict Score")


if submit_button:
    
    input_data = pd.DataFrame(
        [[study_hours, attendance, sleep_hours]], 
        columns=['StudyHours', 'Attendance', 'SleepHours']
    )
    
    
    prediction = model.predict(input_data)
    final_score = min(100.0, max(0.0, prediction[0])) # Score ko 0-100 ke darmiyan rakhne ke liye
    
    
    st.success(f"### 🎯 Predicted Final Score: **{final_score:.2f}%**")
    
    # Choti si recommendation
    st.write("---")
    st.write("💡 **Recommendation:**")
    if sleep_hours < 6:
        st.warning("- Get more sleep! Lack of sleep affects performance.")
    if attendance < 75:
        st.warning("- Try to improve attendance to get better results.")
    if study_hours > 2 and sleep_hours >= 6 and attendance >= 75:
        st.info("- Keep up the good work! Maintain this routine.")