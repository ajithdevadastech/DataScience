#Step1: Import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Step2: Read data from the uploaded csv file
df = pd.read_csv('cancer.csv')

#Step3: Fetch the preview of dataset
print(df.head())

#This data is sourced from <b>Breast Cancer Wisconsin (Diagnostic) Data Set</b>.

#Step4: Look at all the columns in the dataframe
print(df.columns)

#Step5: Graph a boxplot for a specific numerical column
plt.boxplot(df.radius_mean)
plt.show()

#Step6: boxplot parameters
plt.boxplot(df.radius_mean, showmeans=True, vert=False, sym='b+')
plt.show()

"""
- <b>showmeans</b> parameter shows the mean line. In this case, it is overlapping with the median (you can confirm it using <b>meanline</b> parameter).
- <b>vert</b> parameter is true by default. You can change the orientation of the boxplot to horizontal by making it false.
- <b>sym</b> parameter changed the outlier symbol to (+). <b>b</b> changed the color to blue. If you specify it to <b>none</b>, it will remove the outliers.

You can check out all the paramters for plotting the boxplot by pressing <b>shift+tab+tab</b>.
"""

#Now, let us use this boxplot to analyze the relationship between a categorical feature (diagnosis: malignant or benign tumor)
# and a continuous feature (area_mean). We will be using three ways to graph the boxplot:

#Step7: Graph the boxplot using pandas
df.boxplot(column = 'area_mean', by = 'diagnosis')
plt.title('')
plt.show()

#Step8: Graph the boxplot using seaborn
sns.boxplot(x='diagnosis', y='area_mean', data=df)
plt.show()

#Step9: Graph the boxplot using matplotlib
malignant = df[df['diagnosis']=='M']['area_mean']
benign = df[df['diagnosis']=='B']['area_mean']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot([malignant,benign], labels=['M', 'B'])
plt.show()






