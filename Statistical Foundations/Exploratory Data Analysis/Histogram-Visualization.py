#Step1: Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt

#Step2: Enter the data
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]

#Step3: Plot the Histogram
plt.hist(values, histtype='bar')                         #values are plotted on x-axis
plt.show()

#Step4: Specify the Bins
plt.hist(values, bins=10, histtype='bar', edgecolor='k')
plt.show()

#Step5: Add title and labels to the histogram
plt.hist(values, bins=10, histtype='bar', edgecolor='k')

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.show()

#Step6: Add legend to the histogram
plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test score data')

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()

#Step7: Change the range of the histogram
plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test score data', range=[0,100])

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()

#Step8: Change the orientation of the histogram
plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test score data', orientation='horizontal')

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()

values1 = [42,36,24,40,67,62,45,58,41,32,48,49,38,57,42,72,57,56,56,43]

plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test1 score data')
plt.hist(values1, bins=10, histtype='bar', edgecolor='k', label='Test2 score data')

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()

#Step10: Change the transparencies

values1 = [42,36,24,40,67,62,45,58,41,32,48,49,38,57,42,72,57,56,56,43]

plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test1 score data', alpha=0.8)
plt.hist(values1, bins=10, histtype='bar', edgecolor='k', label='Test2 score data', alpha=0.5)

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()

#Step11: Change the colors

values1 = [42,36,24,40,67,62,45,58,41,32,48,49,38,57,42,72,57,56,56,43]

plt.hist(values, bins=10, histtype='bar', edgecolor='k', label='Test1 score data', alpha=0.8, color='c')
plt.hist(values1, bins=10, histtype='bar', edgecolor='k', label='Test2 score data', alpha=0.5, color='r')

plt.title('Histogram of Scores')
plt.xlabel('scores')
plt.ylabel('frequency')
plt.legend()
plt.show()





