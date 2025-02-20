"""
<h2><u>Statistical Foundations</u></h2>

# Module 2: Exploratory Data Analysis
<h2>Demo 1: Detecting and Removing Outliers</h2>

In this demo, you will be shown how to detect and remove outliers using Z-score and IQR score.

"""

#Step1: Import the required libraries
import pandas as pd
from sklearn import datasets
from scipy import stats
import numpy as np

#Step2: Load the Boston House Pricing Dataset which is included in the sklearn dataset API


# boston = datasets.load_boston()

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

x = data
y = target
columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']


# print(x)
# print(y)

#Step3: Create the dataframe
boston_df = pd.DataFrame(x)
boston_df.columns = columns
print(boston_df.head())

### Using Z-Score

#Step1: Use Z-score function defined in scipy library to detect the outliers
boston_df_z = boston_df
z = np.abs(stats.zscore(boston_df))
print(z)

#Step2: Define a threshold
threshold = 3
print(np.where(z > 3))

#The first array contains the list of row numbers and second array contains the respective column numbers, which means that <b><i>z[55][1]</i> has a z-score higher than 3</b>.

#Step3: Remove the outliers using the z-score
boston_df_z = boston_df_z[(z < 3).all(axis=1)]

print("The no. of rows before outlier filtering was: ", boston_df.shape)
print("The no. of rows after outlier filtering is: ", boston_df_z.shape)

#Hence, we filtered out around 90+ rows from the dataset, that is, outliers have been removed.

### Using IQR Score

#Step1: Calculate the IQR
boston_df_iqr = boston_df
Q1 = boston_df_iqr.quantile(0.25)
Q3 = boston_df_iqr.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

#Step2: Detect the outliers
print ((boston_df_iqr < (Q1 - 1.5 * IQR)) | (boston_df_iqr > (Q3 + 1.5 * IQR)))

#The data point where we have <b>False</b> means that these values are valid whereas <b>True indicates presence of an outlier</b>.

#Step3: Remove the outliers using the IQR score
boston_df_out = boston_df_iqr[~((boston_df_iqr < (Q1 - 1.5 * IQR)) |(boston_df_iqr > (Q3 + 1.5 * IQR))).any(axis=1)]

print("The no. of rows before outlier filtering was: ", boston_df_iqr.shape)
print("The no. of rows after outlier filtering is: ", boston_df_out.shape)

#Hence, the outliers have been removed.
