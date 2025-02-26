import numpy as np
import pandas as pd

df = pd.read_csv('marveldata.csv')
print(df.head())

x = len(df['name'])
print(x)

#### Step 4: Display columns SEX, EYE, HAIR

marvel = df[['SEX','EYE','HAIR']]
print(marvel)

#### Step 5: Calculate total number of characters according to gender

char = df.groupby(['SEX']).count()['name']
print(char)

# Marginal Probability
### Calculate the probability of character being male
#### Step 6: Calculate the probability of character being male

print(#Probability of character being male
char['Male Characters']/x)

# Joint Probability
### Calculate the probability of character being female and has red hair
#Assume that both the events are independent of each other
#### Step 7: Calculate probability of character being female

female=char['Female Characters']/x
print(female)

#### Step 8: Calculate count of different hair color
hair=df.groupby(['HAIR']).count()['name']
print(hair)

#### Step 9: Calculate probability of character having red hair
red_hair=hair['Red Hair']/x
print(red_hair)

#### Step 10: Calculate probability of character being female and has red hair, that is, joint probability
#Probability of character being female and has red hairs
print(female*red_hair)

#### Step 11: Calculate joint probability in terms of percentage
print(female*red_hair*100)

# Conditional Probability
### Given that character is female, calculate the probability of having green eyes
#### Step 12: Calculate count of green eyes

#Count of green eyes
green_eyes = df[df=='Green Eyes'].EYE.count()
print(green_eyes)

#### Step 13: Calculate count of female characters

female_char = df[df.SEX=='Female Characters'].SEX.count()
print(female_char)

#### Step 14: Calculate count of female characters with green eyes
female_green_count = df[(df.SEX=='Female Characters') & (df.EYE=='Green Eyes')].SEX.count()
print(female_green_count)

#### Step 15: Calculate probability of female with green eyes

prob_female_green = female_green_count/x
print(prob_female_green)

#### Step 16: Probability of character being female
prob_female = female_char/x
print(prob_female)

#### Step 17: Calculate conditional probability of female with green eyes
print(prob_female_green/prob_female)

#### Conclusion: This code demonstrates how to implement types of probability.

# Odds
### Calculate the odds in favour of living characters
#### Step 1: Calculate the count of living character

living_characters=df.groupby(['ALIVE']).count()['ID'] # This statement returns a dataframe consisting of deceased and living characters
#Getting count of living characters
l=living_characters[1]
print(l)

#### Step 2: Calculate the probability of living characters
prob_liv = l/x
print(prob_liv)

#### Step 3: Calculate number of alive characters except living characters

y = 1-prob_liv
print(y)

#### Step 4: Calculate odds in favour of living characters

odds = prob_liv/y
print(odds)





