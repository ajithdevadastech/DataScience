#In this demo, you will be shown how to use functions from pandas to combine data available in different data sets.

import pandas as pd
import numpy as np

# Read diabetes data from first file

df1 = pd.read_csv('diabetes_data1.csv', index_col='PatientID')
print(df1.head())

#Print the shape of the DataFrame
print(df1.shape)
# Note that there are 20 rows in this DataFrame

# Read data from second file which contains additional rows

df2 = pd.read_csv('diabetes_data1_newRows.csv', index_col='PatientID')
print(df2.shape)

print(df2.head())

# Note that there are 5 rows with the same column structure in the second dataFrame

# Concatenate the rows using concat function

data1 = pd.concat([df1,df2])
print(data1.shape)

print(data1)

# Note the total number of rows in the resulting dataFrame

# Read data from third CSV file which contains additional columns

df3 = pd.read_csv('diabetes_data2.csv', index_col='PatientID')
print(df3.shape)

print(df3)

# Observe the new columns present in this dataFrame

# Concatenate the columns from data1 & df3 using concat function

data2 = pd.concat([data1,df3], axis=1)
print(data2.shape)

print(data2)

# Note that this function combines all the rows in both the dataFrames to result in 27 rows

# Left join
df_left=pd.merge(data1, df3, on='PatientID', how='left')
print(df_left.shape)
print(df_left)

# Observe that this function results in a dataFrame containing only 25 records from left dataFrame

# Right join
df_right=pd.merge(data1, df3, on='PatientID', how='right')
print(df_right.shape)
print(df_right)

# Observe that this function results in a dataFrame containing only 7 records from right dataFrame

# Outer join
df_outer=pd.merge(data1, df3, on='PatientID', how='outer')
print(df_outer.shape)
print(df_outer)

# Observe that this function results in a dataFrame containing all 27 records from both the dataFrames

# Inner join
df_inner=pd.merge(data1, df3, on='PatientID', how='inner')
print(df_inner.shape)
print(df_inner)

# Observe that this function results in a DataFrame containing only 5 records which are common to both DataFrames
