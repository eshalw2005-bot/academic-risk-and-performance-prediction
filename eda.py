from pyexpat import model

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("student_data.csv")


plt.figure(figsize=(6,4))
plt.scatter(data["StudyHours"], data["FinalScore"])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.grid(True)
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(data["Attendance"], data["FinalScore"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")
plt.grid(True)
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(data["SleepHours"], data["FinalScore"])
plt.xlabel("Sleep Hours")
plt.ylabel("Final Score")
plt.title("Sleep Hours vs Final Score")
plt.grid(True)
plt.show()


correlation = data.corr()

plt.figure(figsize=(6,4))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
