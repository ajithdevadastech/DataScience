#Step1: Import the required library
import pandas as pd

#Step2: Read data from the uploaded csv file
cars = pd.read_csv("mtcars.csv")

#Step3: Display the dataframe
print(cars)

#Step4: Display the first five rows
print(cars.head())

#Step5: Display the Dimensions of the data
print(cars.shape)

#Step6: Display the data type of the desired attributes
print(cars.dtypes)