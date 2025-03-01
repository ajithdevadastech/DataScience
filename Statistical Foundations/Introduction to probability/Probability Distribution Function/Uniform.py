import seaborn as sns
from scipy.stats import uniform
import matplotlib.pyplot as plt

data_uniform = uniform.rvs(size=100,loc = 1, scale=4)
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
plt.show()

#### Step 2: Calculate cdf of uniform distriution
#Here, cdf is used to determine the probability that a observation
# that is taken will be less than, greater than, equal, or between two values.

#1)P(X<2)
print(uniform.cdf(2, loc = 1, scale=4 ))

#2)P(X>3)
print(uniform.cdf(3, loc = 1, scale=4 ))

mean, var= uniform.stats(moments='mv')
print(mean, var)

#### Step 3: Calculate mean and variance

print(uniform.mean(loc=1,scale=4))

print(uniform.var(loc=1,scale=4))



