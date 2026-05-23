import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("student-mat.csv", sep=";")
print(df.columns)
# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Average Final Grade
avg_grade = df["G3"].mean()
print("\nAverage Final Grade:", avg_grade)

# Students scored above 15
above_15 = df[df["G3"] > 15].shape[0]
print("Students scored above 15:", above_15)

# Correlation between study time and grades
correlation = df["studytime"].corr(df["G3"])
print("Correlation between Study Time and G3:", correlation)

# Gender wise average score
gender_avg = df.groupby("sex")["G3"].mean()
print("\nGender Wise Average:")
print(gender_avg)

# ---------------- VISUALIZATIONS ---------------- #

# Histogram of Grades
plt.figure(figsize=(6,4))
plt.hist(df["G3"], bins=10)
plt.title("Histogram of Final Grades")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

# Bar Chart
gender_avg.plot(kind="bar")
plt.title("Male vs Female Average Score")
plt.xlabel("Gender")
plt.ylabel("Average Grade")
plt.show()