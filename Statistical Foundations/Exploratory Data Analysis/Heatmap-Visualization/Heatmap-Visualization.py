#Step1: Import the required libraries
import pandas as pd
import seaborn as sns

#Step2: Read data from the uploaded csv file
df = pd.read_csv('cars.csv')

#Step3: Fetch the preview of dataset
print(df.head())

print(df.shape)

print(df.columns)

#Step4: Set up a heatmap using seaborn
import matplotlib.pyplot as plt

df1 = df.drop(columns='Unnamed: 0')

fig, ax = plt.subplots(figsize=(10,6))                        #figure size of (10,6)
sns.heatmap(df1.corr(), center=0, cmap='Reds')
ax.set_title('Multi-Collinearity of Car Attributes')
plt.show()

"""
This heatmap represents the collinearity of the multiple variables in the dataset. 
Since the model names are not numerical values, the <b>unnamed</b> column was dropped off.
Dark red represents a positive correlation, while light white is a negative correlation.
"""

#Step5: Annotate each cell with the numeric value
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df1.corr(), center=0, cmap='BrBG', annot=True)
#adjusting the color and adding annotation (actual correlation values) makes it easier to form a conclusion

plt.show()

"""
You can see that <b>disp</b> and <b>cylinder</b> are highly correlated (features with high correlation are more <b>linearly dependent</b> and hence have almost the same effect on the dependent variable <b>mpg</b>,  that is, 0.85 and 0.85).

When two features have high correlation, we can drop one of the two features and still produce a fairly accurate prediction model.
"""