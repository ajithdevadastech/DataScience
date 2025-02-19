#Step1: Import the required libraries
import pandas as pd
import numpy as np         #for calculating range, std. deviation, variance
import scipy.stats         #for calculating IQR, skewness, kurtosis

#Step2: Read data from the uploaded csv file
cars = pd.read_csv("mtcars.csv")

#Step3: Display the dataframe
print(cars)

#Step4: Calculate the range
print("Range of miles per gallon (mpg): ", np.ptp(cars.mpg, axis=0))    #using ptp method from numpy library
print("Range of displacement (disp): ", np.ptp(cars.disp, axis=0))     #using ptp method from numpy library

#Step5: Calculate the IQR
print(scipy.stats.iqr(cars[['mpg','disp','wt']], axis=0, interpolation='lower'))       #using iqr method from scipy.stats library. Interquartile range (IQR) is a measure of how spread out the middle half of a data set is.

#Step6: Calculate the standard deviation
print(np.std(cars[['mpg','disp','wt']], axis=0))   #using std method from numpy library

#Step7: Calculate the variance
print(np.var(cars[['mpg','disp','wt']], axis=0))       #using var method from numpy library

#Step8: Calculate the skew
from scipy.stats import skew
print(skew(cars[['mpg','disp','wt']], axis=0))     #using skew method from scipy.stats library. Skew is a measure of how asymmetrical a distribution is. A distribution is asymmetrical when its left and right sides are not mirror images.

#Step9: Calculate the kurtosis
"""
"kurtosis" refers to a measure that describes how "heavy" the tails of a data distribution are, essentially indicating whether a distribution has a high concentration of extreme values (outliers) in its tails 
compared to a normal distribution; a high kurtosis signifies "heavy tails" with more outliers, while a low kurtosis indicates "light tails" with fewer extreme values. 
"""
from scipy.stats import kurtosis
print("Pearson Kurtosis: ", kurtosis(cars[['mpg','disp','wt']], fisher=False))  #using kurtosis method from scipy.stats library
print("Fisher's Kurtosis: ", kurtosis(cars[['mpg','disp','wt']], fisher=True))  #using kurtosis method from scipy.stats library


