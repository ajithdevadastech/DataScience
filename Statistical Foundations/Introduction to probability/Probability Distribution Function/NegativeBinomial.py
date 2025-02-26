#A student gets three questions right of every five questions. If X is the number of attempts until the 12th correct answer, what is the probability of the student attempting 20 questions until 12th correct answer?

#### Step 1: Plot the negative binomial distribution using random variates

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import nbinom
data_nbinom = nbinom.rvs(n=12,p=0.6,size=1000)
ax = sns.distplot(data_nbinom,
                  bins = 100,
                  kde=False,
                  color='green',
                  hist_kws={"linewidth": 5,'alpha':1})
ax.set(xlabel='Negative Binomial Distribution', ylabel='Frequency')
plt.show()

#### Step 2: Calculate pmf of negative binomial distribution

#Here parameter passed are k=8 (20-12), n=12, p=0.6
print(nbinom.pmf(8,12,0.6))

#### Step 3: Calculate mean and variance
n, p = 12, 0.6
print(nbinom.mean(n,p,loc=0))

print(nbinom.var(n,p,loc=0))
