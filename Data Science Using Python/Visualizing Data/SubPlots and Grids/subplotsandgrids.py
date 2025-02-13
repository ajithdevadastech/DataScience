import pandas as pd
import matplotlib.pyplot as plt

stats=pd.read_csv('top50.csv')
print(stats.head())
print(stats.shape)

### 1. Barplot

#Matplotlib also supports hex colors
for group,data in stats.groupby('Genre'):
    plt.barh(group,data['Energy'].mean(),color='#3E5D57')
    plt.barh(group,data.Danceability.mean(),color='#4CCAB1',left=data['Energy'])
plt.xlabel('Value')
plt.ylabel('Genre')
plt.title('Energy and Danceability per Genre')
plt.show()

### 2. Subplots

# total number of columns persent in dataset
len(stats.columns)

#First 3 columns are caegorical we don't need those
indx=1 #Index for subplots starts from 1
plt.figure(figsize=(20,18))
for col in stats.columns[3:]:
    plt.subplot(5,2,indx)
    plt.hist(stats[col],color='c')
    plt.title(col)
    indx+=1
plt.show()

### 3. Boxplot
plt.boxplot(stats.Liveness)
plt.show()

### 4. GridSpec

plt.style.use('ggplot')
stats_grid=plt.GridSpec(4,5)
stats_fig=plt.figure(figsize=(15,12))
stats_fig.add_subplot(stats_grid[:2,:3])  # row: 1,2 and column: 1,2
# Using custom colors
for group,data in stats.groupby('Genre'):
    plt.barh(group,data['Energy'].mean(),color='#3E5D57')
    plt.barh(group,data.Danceability.mean(),color='#4CCAB1',left=data['Energy'])
plt.xlabel('Value')
plt.ylabel('Genre')
plt.title('Energy and Danceability per Genre')


stats_fig.add_subplot(stats_grid[:2,3:]) # row:1,2 and col: 3,4,5
#Some sytles do not display outliers
plt.title('Boxplot - Liveness')
plt.boxplot(stats.Liveness)

stats_fig.add_subplot(stats_grid[2:,:]) # row:3,4 and col:1-5
plt.title('Histogram - Popularity')
plt.hist(stats.Popularity)
plt.ylabel('Frequency')
plt.xlabel('Popularity')
plt.savefig('GridSpec.png')
plt.show()

