"""

A restaurant gets an average of 2.8 customers approaching the register every minute.
What is the probability that 4 customers approach the register in the next minute?
Also calculate mean and variance.

"""

import seaborn as sns
from scipy.stats import poisson
import matplotlib.pyplot as plt

data_poisson = poisson.rvs(mu=2.8, size=10000)
ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='green',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')
plt.show()

#### Step 2: Calculate pmf of poisson distribution

#here passed parameter are k=4, mu=2.8
print(poisson.pmf(4,2.8))




