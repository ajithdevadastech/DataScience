import numpy as np
import pandas as pd

titanic = pd.read_csv('titanic.csv')
print(titanic.head())

#### Step 3: Print 2 columns, that is, Sex and Survived from the dataset

titanic = titanic[['Sex','Survived']]
#Print top 5 rows of given columns
print(titanic.head())
#Here O = not survived and 1 = survived

#### Step 4: Calculate number of people survived

num_rows = float(titanic.shape[0])
num_rows
survival_num = titanic[titanic['Survived']==1]['Survived'].count()
print("Number of people survived=",survival_num)


#### Step 5: Calculate number of people not survived

nsurvival_num = titanic[titanic['Survived']==0]['Survived'].count()
print("Number of people unsurvived=",nsurvival_num)

#### Step 6: Calculate the probability of number of female survived

print(len(titanic[(titanic['Survived']==1)&(titanic['Sex']=='female')])/len(titanic[titanic.Sex=='female']))