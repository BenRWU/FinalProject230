import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


data_path = 'dataset/AdultsData_OnlyUS.csv'  # Update this path if necessary
us_data = pd.read_csv(data_path)

# Prepare the Data
us_data = pd.get_dummies(us_data, drop_first=True)  # Convert categorical variables to dummy variables
X = us_data.drop('income_>50K', axis=1)  # Features
y = us_data['income_>50K']  # Target

# Split the Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build the Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions and Evaluations
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

# Interpret the Results
# Look at the model coefficients
print(pd.DataFrame(model.coef_, columns=X.columns))
