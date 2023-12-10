import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'dataset/AdultsData_OnlyUS.csv'
us_data = pd.read_csv(data_path)

# Convert categorical variables to dummy variables
us_data = pd.get_dummies(us_data, drop_first=True)

# Define columns to be excluded
excluded_features = ['income_<=50K', 'income_>50K', 'fnlwgt']  # Adjust based on actual column names

# Check if the columns to be excluded exist in the DataFrame
excluded_features = [col for col in excluded_features if col in us_data.columns]

# Define your features (X) and target (y)
X = us_data.drop(excluded_features, axis=1)
y = us_data['income_>50K']  # Assuming 'income_>50K' is the binary target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression(max_iter=50000)  # Increased max_iter
model.fit(X_train, y_train)

# Predictions and Evaluations
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Fit logistic regression model on the entire dataset for complete coefficient analysis
full_model = LogisticRegression(max_iter=50000)  # Increased max_iter
full_model.fit(X, y)

# Create a DataFrame for the coefficients
coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': full_model.coef_[0]})
coefficients['Influence'] = coefficients['Coefficient'].apply(lambda x: 'Positive' if x > 0 else 'Negative')
coefficients = coefficients.sort_values(by='Coefficient', ascending=False)

# Save the coefficients to a CSV file
coefficients.to_csv('dataset/logistic_regression_coefficients_filtered.csv', index=False)

# Plotting with emphasis on Positive/Negative Influence
plt.figure(figsize=(10, 8))
sns.barplot(x='Coefficient', y='Feature', hue='Influence', data=coefficients)
plt.title('Logistic Regression Coefficients (Positive vs Negative Influence)')
plt.xlabel('Coefficient Value')
plt.ylabel('Features')
plt.show()
