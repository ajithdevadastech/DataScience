"""

<h2><u>Statistical Foundations</u></h2>

# Module 5: Inferential Statistics - 1
<h2> Demo 1: Working with Population and Sample </h2>

In this demo, you will be shown how to calculate population and sample mean and standard deviation.

"""

#Step1: Import the required library
import pandas as pd
import numpy as np

#Step2: Read data from the uploaded csv file
cars = pd.read_csv("mtcars.csv")
print(cars.head())

### Calculate population mean and population standard deviation for <b>mpg</b> column.

#Step3: Calculate population mean and population standard deviation
population_mpg = cars.mpg
mu = population_mpg.mean()
sigma = population_mpg.std()
print(mu, sigma)

### Draw samples from the population and calculate their mean and standard deviation values using Pandas.

#Step4: Draw sample of 20 using pandas
sample_size = 20
sample = cars.sample(n=sample_size, random_state=1).mpg

#Step5: Calculate sample mean and sample standard deviation using pandas
sample_mu_p = sample.mean()
sample_sigma_p = sample.std()
print("Sample mean is %.2f compared with population mean of %.2f" %(sample_mu_p, mu))
print("Diff betweeen sample and population mean:", sample_mu_p - mu)

print("\nSample std. deviation is %.2f compared with population mean of %.2f" %(sample_sigma_p, sigma))
print("Diff betweeen sample and population std. deviation:", sample_sigma_p - sigma)

### Draw samples from the population and calculate their mean and standard deviation values using NumPy.

#Step6: Draw sample of 20 using numpy
sample_size = 20
np.random.seed(1)
sample_mpg = np.random.choice(a = cars["mpg"], size = sample_size)

#Step7: Calculate sample mean and sample standard deviation using numpy
sample_mu_n = sample_mpg.mean()
sample_sigma_n = sample_mpg.std()
print("Sample mean is %.2f compared with population mean of %.2f" %(sample_mu_n, mu))
print("Diff betweeen sample and population mean:", sample_mu_n - mu)

print("\nSample std. deviation is %.2f compared with population mean of %.2f" %(sample_sigma_n, sigma))
print("Diff betweeen sample and population std. deviation:", sample_sigma_n - sigma)

