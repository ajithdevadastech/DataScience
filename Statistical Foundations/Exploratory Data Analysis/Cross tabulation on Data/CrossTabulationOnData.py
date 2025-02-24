#Step1: Import the required library
import pandas as pd

#Step2: Read data from the uploaded csv file
bank = pd.read_csv("bank.csv", sep = ';')

#This is a <b>Bank Marketing Data Set</b> available from the UCI Machine Learning Repository.

#Step3: Fetch the dataframe preview
print(bank.head())

"""
You can observe from the above table, each potential customer of the bank and whether or not 
they subscribed to a new term deposit <b>( y )</b>.

Now, to perform EDA on this data, you have to decide which variables to include in the model. 

For example, to decide if you want to use the <b>job information</b> in your model, 
you have to determine if the job that a person has is correlated with an increased likelihood to subscribe to the deposit. 
For that, we need to figure out the percentages of people who subscribe for each job type:

"""

#Step4: Group the observations by job type, and count the occurences of "y" for each job type
print(bank.groupby('job').y.value_counts())

"""
This displays our required information but isn't quite easy to read.

So, we turn the values of <b>y</b> into a table: 

"""

#Step5: Perform cross-tabulation on the above data
print(pd.crosstab(bank.job, bank.y))

"""
Now, you can clearly figure out the number of people who subscribe to the deposit for each job type.

You can also find out the percentages of subscription for each job type using the <b>normalize</b> parameter:
"""

#Step6: Cross-tabulation using the "normalize" parameter
print(pd.crosstab(bank.job, bank.y, normalize='index'))

"""
From the above table, it is clear to us that blue-collared peeps, housemaids, and service workers are among the lowest subscribers to the deposit. And a much higher percentage of retired people and students subscribe to it. 

Now you know that the job type is probably a relevant information for your model.
"""


