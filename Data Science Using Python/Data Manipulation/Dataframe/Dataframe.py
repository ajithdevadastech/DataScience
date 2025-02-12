##### Question 1:

"""
Perform the following pandas operations

    1) From the raw data below create a DataFrame

    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]

    2) Save the dataFrame into a csv file as example.csv
    3) Read the example.csv and print the DataFrame
    4) Read the example.csv without column heading
    5) Read the example.csv and make the index columns as 'First Name’ and 'Last   Name'
    6) Read the first 3 rows of the dataFrame and print the dataFrame
    7) The column 'postTestScore' has "," in their values around numbers to represent thousands. Load example.csv file which ignores the default behaviour of comma while reading the 'postTestScore' column

"""

# Import the required libraries

import pandas as pd
import numpy as np

# 1.1

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print(df)

# 1.2 Save the DataFrame into a CSV file

df.to_csv('example.csv')

# 1.3 Read data from CSV and print the DataFrame

df = pd.read_csv('example.csv', header=0)
print(df)

# 1.4 Read data from CSV without headers

df = pd.read_csv('example.csv', header=None)
print(df)

# 1.5 Read the data again with headers and make the index columns as 'First Name’ and 'Last Name'

df = pd.read_csv('example.csv', header=0, index_col=['First Name', 'Last Name'],
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
print(df)

# 1.6 Read the first 3 rows of the DataFrame and print the DataFrame

df = pd.read_csv('example.csv', nrows=3)
print(df)

# 1.7
df = pd.read_csv('example.csv',  thousands=',')
print(df)


##### Question 2:

"""

    1) Read diabetes data from a CSV file
    2) Print the first 10 rows and last 5 of the DataFrame
    3) Display a summary of the data in DataFrame
    4) Display summary of only Glucose column
    5) Take a sample of the data using first 15 rows
    6) Add a new column "New_Age" in the DataFrame by adding 1 to values in existing "Age" column
    7) Drop the column "SkinThickness" as it is not relevant to our analysis
    8) Filter rows where patient's age is greater than or equal to 50 since such patients have high possibility of having diabetes. Use column New_Age. Incorporate another condition for filtering rows as Outcome = 1.
    9) Sort values in the DataFrame df4 by "Glucose" in descending order
"""

# Read diabetes data from a CSV file

df = pd.read_csv('diabetes.csv')


# Print the first 10 rows of the DataFrame
print(df.head(10))

# Print the last 5 rows of the DataFrame
print(df.tail())

# Display a summary of the data in DataFrame
print(df.describe())

# Display summary of only Glucose column
print(df.Glucose.describe())

# Take a sample of the data using first 15 rows
df2 = df.iloc[:15]
print(df2)

# Add a new column "New_Age" in the dataframe by adding 1 to values in existing "Age" column
df2['New_Age']=df['Age'] + 1
print(df2)

# Drop the column "SkinThickness" as it is not relevant to our analysis

df3 = df2.drop(['SkinThickness'], axis=1)
print(df3.head())

# Filter rows where patient's age is greater than or equal to 50 since such patients have high possibility of having diabetes.
# Use column New_Age

print(df3[df3['New_Age']>= 50])

# Incorporate another condition for filtering rows as Outcome is '1'

df4 = df3[(df3['New_Age']>= 50) & (df3['Outcome'] == 1)]
print(df4)

# Sort values in the DataFrame df4 by "Glucose" in descending order

df4.sort_values(by=['Glucose'], ascending = False)


