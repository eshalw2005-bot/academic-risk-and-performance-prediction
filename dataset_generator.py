import pandas as pd
import numpy as np

np.random.seed(42)


n = 200

study_hours = np.random.randint(1, 11, n)      # 1-10 hours
attendance = np.random.randint(50, 101, n)     # 50-100%
sleep_hours = np.random.randint(4, 10, n)      # 4-9 hours


final_score = (
    study_hours * 5 +
    attendance * 0.5 +
    sleep_hours * 2 +
    np.random.randint(-10, 11, n)  # random variation
)


final_score = np.clip(final_score, 0, 100)


df = pd.DataFrame({
    "StudyHours": study_hours,
    "Attendance": attendance,
    "SleepHours": sleep_hours,
    "FinalScore": final_score
})


df.to_csv("student_data.csv", index=False)

print("Dataset Created Successfully!")
print("\nFirst 5 Records:")
print(df.head())