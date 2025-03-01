"""

A company manufactures a certain electronic component and each component is tested.
The probability of one electronic component being defective is 0.05. Determine the probability of the first defect being found in the eighth component tested.
Also determine the random variable’s expected value and variance.

"""

#### Step 1: Plot geometric distribution using random variates

import seaborn as sns
from scipy.stats import geom
import matplotlib.pyplot as plt

data_geom = geom.rvs(p=0.05 , size=10000)
ax = sns.distplot(data_geom,
                  bins=30,
                  kde=False,
                  color='green',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Geometric Distribution', ylabel='Frequency')
plt.show()
#### Step 2: Calculate pmf of geometric distribution

#Here parameter passed are k=8, p=0.05
print(geom.pmf(8,0.05,loc = 0))

#### Step 3: Calculate mean and variance

p=0.05
print(geom.mean(p, loc=0))

print(geom.var(p, loc=0))

