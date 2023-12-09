import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'dataset/AdultsData_OnlyUS.csv'
us_data = pd.read_csv(data_path)

# Graph 1: Male vs Female
gender_counts = us_data['sex'].value_counts()
print("Gender Distribution:\n", gender_counts, "\n")
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.title('Gender Distribution in US Data')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Graph 2: Different Races
race_counts = us_data['race'].value_counts()
print("Race Distribution:\n", race_counts, "\n")
plt.figure(figsize=(8, 6))
sns.barplot(x=race_counts.index, y=race_counts.values)
plt.title('Race Distribution in US Data')
plt.xlabel('Race')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Graph 3: Different Levels of Education
education_counts = us_data['education'].value_counts()
print("Education Level Distribution:\n", education_counts, "\n")
plt.figure(figsize=(10, 8))
sns.barplot(x=education_counts.values, y=education_counts.index)
plt.title('Education Level Distribution in US Data')
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.show()
