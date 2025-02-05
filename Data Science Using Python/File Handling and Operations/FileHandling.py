### Step 1: Open and read from the file

file=open('DataScience.txt','r',encoding='utf-8')
for each in file:
   print(each)

### Step 2: Write the content of DataScience file to new file i.e. Data file and perform replace operation on it

ds = open("DataScience.txt", "r", encoding='utf-8')
new=open('Data.txt','w', encoding='utf-8')
for i in ds:
    i=i.replace('data','tata')
    new.write(i)
ds.close()
new.close()
sci=open('Data.txt','r', encoding='utf-8')
for i in sci:
    print(i)
sci.close()

### Step 3: Close the DataScience file

ds.close()

### Step 4: Rename the Data file as New_Science

import os
os.rename("Data.txt","New_Science.txt")

### Step 5: Append the New_Science file

file = open("New_Science.txt", "a", encoding='utf-8')
file.write("A data scientist is the adult version of the kid who can’t stop asking “Why?”.")
file.close()

