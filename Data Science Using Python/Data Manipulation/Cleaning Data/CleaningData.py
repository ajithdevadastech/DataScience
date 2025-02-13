#In this demo, you will be shown how to inspect and remove various inconsistencies from data in order to prepare it for analysis.

# Import the required libraries

import pandas as pd
import numpy as np

# Read sample of diabetes data from a CSV file

df = pd.read_csv('diabetes_sample.csv')
print(df)
print(df.shape)

# Check if there are any null values in the data

print(df.isnull())

# Check for null values in column Insulin

print(df.Insulin.isnull())

# Fill the rows containing null values in Insulin column with the mean value of that column

df.Insulin = df.Insulin.fillna(df.Insulin.mean())
print(df)
print(df.Insulin)

# Observe that the null value is filled using the mean

# Check for duplicate rows

print(df.duplicated())

# Here, only row 5 is displayed since row 4 & 5 are exact copies of each other

# Check if any patient has a duplicate entry using PatientID column

print(df.duplicated(['PatientID']))

# Observe that one more entry is returned as True in this case