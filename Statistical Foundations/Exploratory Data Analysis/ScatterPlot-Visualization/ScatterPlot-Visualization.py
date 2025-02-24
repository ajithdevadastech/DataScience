#Step1: Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#Step2: Load the built-in dataset
tips = sns.load_dataset("tips")

#Step3: Fetch the preview of dataset
print(tips.head(10))

#Step4: Obtain generic mathematical details
print(tips.describe())

#Step5: Visualize basic scatter plot
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()

"""
- The linear line across the plot shows the <b>trend of the tip</b> given by the customers as per the total bill. 

- The data points farther away from the line (top-right) are the <b>outliers</b> or exceptions in the dataset.

- The <b>convergent point</b> is the <b>statistical mean</b> or the generalized prediction of the tip value on a daily basis.

For <b>sns.lmplot()</b>, there are three mandatory parameters as illustrated above. There is also an optional <b>hue</b> 
parameter that takes in categorical columns and helps group the data plot as per <b>hue</b> parameter values. 

"""

#Step6: Visualize basic scatter plot with hue parameter
sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.show()

"""
From the above plot, we can concur that while females are mostly sticking to the convergent point and tip the usual amount, quite a few males tip (exceptionally) more or less. 
So, hue helped us visualize this difference in separate color plotting.
"""

#Step7: Visualize basic scatter plot with marker parameter
sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, markers=["o","x"])
plt.show()

#Step8: Visualization on separate facets
sns.lmplot(x="total_bill", y="tip", col="sex", data=tips)
plt.show()

sns.lmplot(x="total_bill", y="tip", row="smoker", col="sex", data=tips)
plt.show()

#This way, you can drill deeper into your data, where tip is still given against total bill but is now
# also segmented into whether a smoker or not along with dependency on gender.




