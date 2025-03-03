#Step1: Import the required library
import pandas as pd
import numpy as np

#Step2: Load sample data set

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

### Check if the sample mean differs from the population mean.

#Step3: Population mean and population standard deviation
population_target = df.target
mu = population_target.mean()
sigma = population_target.std()
print("Population Mean:", mu,"\nPopulation std:", sigma)

#Step4: Draw sample of 100
sample_size = 100
sample = df.sample(n=sample_size, random_state=4).target
sample_mu = sample.mean()
sample_sigma = sample.std()
print("Sample Mean:", sample_mu,"\nSample std:", sample_sigma)

### Perform Null Hypothesis using Z-statistic

"""
Null Hypothesis: population mean = sample mean
"""
import math
from scipy import stats

#Step5: Calculate z-critical and z-statistic

#margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
z_critical = stats.norm.ppf(q = 0.975) #1.96
N = 100
SE = sigma/np.sqrt(N)
z_stat = (sample_mu - mu)/SE
print("Z-Statistic: ", z_stat)

print("Z-Critical: ", z_critical)

### One Sample T-test

#Step6: Perform t-test at 95% confidence level
print(stats.ttest_1samp(a= sample,                         # Sample data
                 popmean= population_target.mean())) # Pop mean

#Step7: Check if a 95% confidence interval will capture the population mean of 22.53

sigma = sample.std()/math.sqrt(100)  # Sample stdev/sample size

print(stats.t.interval(0.95,                        # Confidence level
                 df = 49,                     # Degrees of freedom
                 loc = sample.mean(), # Sample mean
                 scale= sigma))

### Two Sample T-test

#Step8: Draw sample of 100
sample2 = df.sample(n=100, random_state=88).target
sample_mu2 = sample2.mean()
sample_sigma2 = sample2.std()
print("Sample Mean2:", sample_mu2,"\nSample std2:", sample_sigma2)

#Step9: Check if the mean of two independent data samples differ from one another
print(stats.ttest_ind(a= sample,
                b= sample2,
                equal_var=False))

"""
There is a 24% chance we'd see sample data this far apart 
if the two groups tested are actually identical
"""


