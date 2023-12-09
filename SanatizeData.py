import pandas as pd
import numpy as np

# Column names based on the dataset description
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country', 'income'
]

# Load the datasets
adult1 = pd.read_csv('dataset/adult1.csv', header=None, names=column_names)
adult2 = pd.read_csv('dataset/adult2.csv', header=None, names=column_names, skiprows=1) # skip the first row for the test set

# Combine the datasets
adult_combined = pd.concat([adult1, adult2])

# Apply strip function to each string element in the DataFrame
adult_combined = adult_combined.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Replace '?' with NaN
adult_combined.replace('?', np.nan, inplace=True)

# Save the cleaned dataset
adult_combined.to_csv('dataset/AdultsCombined_Cleaned.csv', index=False)
