"""

The average thickness of the hose storage units produced in a factory (X) follows a normal distribution with a
mean of 3 mm and a standard deviation of 0.4 mm. Determine (1) P(X > 4.1) (2) P(X ≤ 3) (3) P(X < 2.3).

"""

import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

# generate random numbers from N(0,1)
data_normal = norm.rvs(size=1000,loc=3,scale=0.4)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='grey',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()

#### Step 2: Calculate cdf of normal distriution

#calculate z-score
z=(4.1-3)/0.4
print(1-(norm.cdf(z)))

z=(3-3)/0.4
print(1-(norm.cdf(z)))

z=(2.5-3)/0.4
print(1-(norm.cdf(z)))
