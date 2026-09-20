import pandas as pd

# Read the dataset
df = pd.read_csv("students.csv")

# Display the complete dataset
print("Student Performance Data:")
print(df)

# Display basic information
print("\nNumber of students:", len(df))

# Calculate average marks
print("\nAverage Marks:")
print(df[["Maths", "Physics", "Programming", "Data_Science"]].mean())

# Find the highest programming marks
print("\nHighest Programming Marks:")
print(df["Programming"].max())
