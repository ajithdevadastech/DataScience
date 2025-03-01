#### Step 1: Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### Step 2: Create population data from uniform distribution

#Create an empty dataframes
population = pd.DataFrame()
#Create an column that is 10000 random numbers drawn from a uniform distribution
population['numbers'] = np.random.uniform(0,10000,size=10000)
#Plot the histogram
population['numbers'].hist(bins=100)

plt.show()

#### Step 3: Calculate mean of population

print(population['numbers'].mean())

#### Step 4: Take a sample mean and repeat 100 times and plot it

sampled_means = []
# For 1000  times,
for i in range(0,1000):
    # Take a random sample of 100 rows from the population, take the mean of those rows, append to sampled_means
    sampled_means.append(population.sample(n=100).mean().values[0])
pd.Series(sampled_means).hist(bins=100)

plt.show()

#Here, we can see that the population distribution was uniform and now distribution is approching normality.
# This is the key point of central limit theorem.

#### Step 5: Calculate sample mean

print(pd.Series(sampled_means).mean())

#### Step 6: Compare population and sample mean

error = population['numbers'].mean() - pd.Series(sampled_means).mean()
print('The Mean Sample Mean is only %f different the True Population mean!' % error)

#The Mean Sample Mean is only 0.803320 different the True Population mean!

#Here, we can see that population and sample mean are nearly close to each other.




