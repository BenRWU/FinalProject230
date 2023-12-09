import pandas as pd

# Define the column names based on the dataset documentation
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
    'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
    'hours_per_week', 'native_country', 'income'
]

# Load the cleaned dataset
data_path = 'dataset/AdultsCombined_Cleaned.csv'
adult_data = pd.read_csv(data_path, names=column_names, skiprows=1)  # Skip the header row

# Convert necessary columns to numeric and explicitly handle non-convertible values
convert_columns = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
for column in convert_columns:
    adult_data[column] = pd.to_numeric(adult_data[column], errors='coerce')

# Drop rows with NaN values in the specified columns after conversion
adult_data.dropna(subset=convert_columns, inplace=True)

# Function to perform query on the dataset by country
def query_data_by_country(country):
    return adult_data[adult_data['native_country'] == country]

# Example usage:
# Query the dataset for individuals from a specific country, e.g., United-States
result = query_data_by_country("United-States")

# Display the result
print(result.head())  # This will print the first 5 rows of the filtered data
print(f"Total count of individuals from United-States: {len(result)}")  # This will print the total count
