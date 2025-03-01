"""
<h2><u>Statistical Foundations</u></h2>

# Module 5: Inferential Statistics - 1
<h2> Demo 3: Margin of Error and Confidence Interval </h2>

In this demo, you will be shown how to calculate margin of error and confidence interval.

"""

#Step1: Import the required library
import pandas as pd
import numpy as np

#Step2: Load sample data set
#from sklearn.datasets import load_boston
from sklearn.utils import shuffle

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']

X, y = shuffle(data, target, random_state=13)

df = pd.DataFrame(data,columns= columns)
df['target'] = target
print(df.head())

#Step3: Generate sample
sample_size = 200
sample = df.sample(n=sample_size, random_state=1)

### Calculate Z-critical, margin of error, and confidence interval.

import math
from scipy import stats

sample_mean = sample.target.mean()
np.random.seed(1)

"""
signifies the number of standard deviations 
you'd have to go from the mean of the normal 
distribution to capture the proportion of the
data associated with the desired confidence level
"""
### Calculate Z-critical, margin of error, and confidence interval.

#Step4: Get the z-critical value
z_critical = stats.norm.ppf(q = 0.975)

#Step5: Get the population standard deviation
pop_stdev = sample.target.std()

#Step6: Calculate margin of error
margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

#Step7: Calculate confidence interval
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)

print("Z-critical value:", z_critical)
print("Margin of Error:", margin_of_error)
print("Confidence Interval:", confidence_interval)



