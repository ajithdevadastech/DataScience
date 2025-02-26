#Consider a coin is flipped two times, so the four possible outcomes are HH, HT, TH, and TT. What is the probability that head will occur? Also calculate mean and variance.
"""

So, let the variable X represent the number of Heads that result from this experiment.
The variable X can take on the values 0, 1, or 2.
Here, x = 0, 1, 2; P = 0.5; n = 2

"""

#### Step 1: Plot binomial distribution using random variates

import seaborn as sns
from scipy.stats import binom
import matplotlib.pyplot as plt

data_binom = binom.rvs(n=2,p=0.5,size=10000)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='green',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')

plt.show()

#### Step 2: Calculate pmf of binomial distribution

#Here passed parameter are k=0, n=2, p=0.5
#for k=0
print(binom.pmf(0,2,0.5,loc=0))

#for k=1
print(binom.pmf(1,2,0.5,loc=0))

#for k=2
print(binom.pmf(2,2,0.5,loc=0))

#### Step 3: Calculate mean and variance

n,p = 2,0.5
print(binom.mean(n,p,loc=0))

print(binom.var(n,p,loc=0))

#### Conclusion: This code demonstrates how to implement binomial distribution.
# mean = np, variance = np(i-p)



