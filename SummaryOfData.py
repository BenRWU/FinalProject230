import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'dataset/AdultsData_OnlyUS.csv'
us_data = pd.read_csv(data_path)

# Define Numerical and Categorical Features
numerical_features = ['age', 'hours_per_week']
categorical_features = ['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'income']


# Box Plot for Age by Education Level, grouped by Income
plt.figure(figsize=(12, 6))
sns.boxplot(x='education', y='age', hue='income', data=us_data)
plt.title('Age Distribution by Education Level and Income')
plt.xlabel('Education Level')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()

# Box Plot for Hours Per Week by Occupation, grouped by Income
plt.figure(figsize=(12, 6))
sns.boxplot(x='occupation', y='hours_per_week', hue='income', data=us_data)
plt.title('Hours Per Week by Occupation and Income')
plt.xlabel('Occupation')
plt.ylabel('Hours Per Week')
plt.xticks(rotation=90)
plt.show()




# Numerical Features Analysis
print("Numerical Features Analysis:")
for feature in numerical_features:
    print(us_data[feature].describe(), "\n")
    plt.figure(figsize=(6, 4))
    sns.histplot(us_data[feature], kde=True)
    plt.title(f'Distribution of {feature}')
    plt.show()

# Categorical Features Analysis
print("Categorical Features Analysis:")
for feature in categorical_features:
    print(f"{feature} Value Counts:\n{us_data[feature].value_counts()}\n")
    plt.figure(figsize=(8, 6))
    sns.countplot(y=feature, data=us_data)
    plt.title(f'Frequency of {feature}')
    plt.show()
