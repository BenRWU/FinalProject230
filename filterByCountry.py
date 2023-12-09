import pandas as pd
import matplotlib.pyplot as plt


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

# Filter data for only individuals from the United States
us_data = adult_data[adult_data['native_country'] == 'United-States']

# Save this filtered data to a new CSV file
us_data.to_csv('dataset/AdultsData_OnlyUS.csv', index=False)

# Get the count of individuals from each country, excluding the US
non_us_data = adult_data[adult_data['native_country'] != 'United-States']
country_counts = non_us_data['native_country'].value_counts()

# Count the number of people from the US and not from the US
num_from_us = len(us_data)
num_not_from_us = len(non_us_data)

# Print the results
print(f"Number of people from the United States: {num_from_us}")
print(f"Number of people not from the United States: {num_not_from_us}")

# Create a bar chart
plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar')
plt.title('Number of Individuals from Each Country (Excluding the United States)')
plt.xlabel('Country')
plt.ylabel('Number of Individuals')
plt.xticks(rotation=45)
plt.show()
