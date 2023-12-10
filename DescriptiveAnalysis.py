import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'dataset/AdultsData_OnlyUS.csv'
us_data = pd.read_csv(data_path)

# Histogram for Age
plt.figure(figsize=(8, 4))
sns.histplot(us_data['age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bar Chart for Education
education_counts = us_data['education'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=education_counts.values, y=education_counts.index)
plt.title('Education Level Distribution')
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.show()

# Box Plot for Income by Education
plt.figure(figsize=(10, 6))
sns.boxplot(x='income', y='education_num', data=us_data)
plt.title('Income by Education Level')
plt.xlabel('Income')
plt.ylabel('Education Number')
plt.show()
