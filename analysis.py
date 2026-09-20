import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("students.csv")

# Display the dataset
print("Student Performance Data:")
print(df)

# Calculate average marks
subjects = ["Maths", "Physics", "Programming", "Data_Science"]
averages = df[subjects].mean()

print("\nAverage Marks:")
print(averages)

# Find highest programming marks
print("\nHighest Programming Marks:", df["Programming"].max())

# Create a bar chart
plt.figure(figsize=(8, 5))
averages.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("average_marks.png")
plt.show()
