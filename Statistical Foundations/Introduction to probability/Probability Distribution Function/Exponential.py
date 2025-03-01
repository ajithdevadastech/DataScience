"""
Exponential Distribution
--------------------------

The life span of an electronic component follows an exponential distribution with a mean lifetime of 120 hours.
Determine the probability of a component failing in the first 100 hours of use and also calculate mean and variance.

"""

#### Step 1: Plot the exponential distribution using random variates

import seaborn as sns
from scipy.stats import expon
import matplotlib.pyplot as plt

data_expon = expon.rvs(scale=120,loc=0,size=100)
ax = sns.distplot(data_expon,
                  kde=False,
                  bins=100,
                  color='grey',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')
plt.show()

#### Step 2: Calculate cdf of uniform distriution

#for x=100,loc=0,scale=120
print(expon.cdf(100,0,120))

#### Step 3: Calculate mean and variance

print(expon.mean(loc=0,scale=120))

print(expon.var(loc=0,scale=120))



