import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


data = pd.read_csv("student_data.csv")


X = data[["StudyHours", "Attendance", "SleepHours"]]
y = data["FinalScore"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("===== MODEL PERFORMANCE =====")
print("R2 Score:", round(r2_score(y_test, y_pred), 2))
print("MAE:", round(mean_absolute_error(y_test, y_pred), 2))


print("\n===== ACADEMIC RISK AND PERFORMANCE PREDICTION =====")

study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))
sleep = float(input("Enter Sleep Hours: "))

prediction = model.predict([[study, attendance, sleep]])

print("\nPredicted Final Score:", round(prediction[0], 2))


print("\n===== RECOMMENDATIONS =====")

if study < 4:
    print("- Increase study hours.")

if attendance < 75:
    print("- Improve attendance.")

if sleep < 6:
    print("- Get more sleep.")

if study >= 4 and attendance >= 75 and sleep >= 6:
    print("- Keep up the good work!")
    
print("\n===== ACADEMIC RISK AND PERFORMANCE PREDICTION =====")

study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))
sleep = float(input("Enter Sleep Hours: "))


prediction = model.predict([[study, attendance, sleep]])

print("\nPredicted Final Score:", round(prediction[0], 2))

print("\n===== RECOMMENDATIONS =====")

if study < 4:
    print("- Increase study hours.")

if attendance < 75:
    print("- Improve attendance.")

if sleep < 6:
    print("- Get more sleep.")

if study >= 4 and attendance >= 75 and sleep >= 6:
    print("- Keep up the good work!")

import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)