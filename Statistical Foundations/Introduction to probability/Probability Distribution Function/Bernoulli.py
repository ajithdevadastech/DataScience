"""
The final match of basketball is going to be between teams A and B. Random variable X represents the team that will win the Cup.
The probability of team A winning is 0.60. Determine the distribution of X, in addition to X’s expected value and variance.
"""

##### Solution:
#### Step 1: Plot Bernoulli distribution using random variants

import numpy as np
import seaborn as sns
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

data_bern = bernoulli.rvs(size=10000,p=0.6)
ax= sns.distplot(data_bern,
                 kde=False,
                 color="green",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
plt.show()

#### Step 2: Calculate pmf of Bernoullli distribution

#Here, parameter passed are x=0, p=0.6
#for x=0
print(bernoulli.pmf(0,0.6))

#for x=1
print(bernoulli.pmf(1,0.6))

#### Step 3: Calculate mean and variance
p=0.6
print(bernoulli.mean(p,loc=0))

print(bernoulli.var(p,loc=0))

#### Conclusion: This code demonstrates how to implement Bernoulli distribution.

#mean = p, variance = p(1-p)



