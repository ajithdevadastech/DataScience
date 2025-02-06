### Step 1: Import the libraries

import numpy as np

### Step 2: Create numpy array a as first column of plain text and array b as key

a = np.array([4,3])
b = np.array([[11,9],[8,17]])

### Step 3: Perform matrix product between array a and b

c=np.dot(a,b)
print(c)

### Step 4: Perform encryption of plain text using mod function

h = np.mod(c,26)
print("h=",h)

### Step 5: Create numpy array d of second column of plain text and array b as key

d = np.array([20,11])

### Step 6: Perform matrix product between array d and b

f = np.dot(d,b)

### Step 7: Perform encyption of plain text using mod function

h1=np.mod(f,26)
print("h1=",h1)

### Step 8: Create a numpy array g of last column of plain text and array b as key

g = np.array([4,10])

### Step 9: Perform matrix product between array g and b

j =np.dot(g,b)

h2=np.mod(j,26)
print("h2",h2)

### Step 1: Import the libraries

import numpy as np

### Step 2: Load marks.csv file
data = np.loadtxt('marks.csv', delimiter=',', usecols=(5), skiprows=1)

### Step 3: Display the column on which we are going to perform different aggregate functions

print("Data:", data)

### Step 4: Calculate different aggregate function on marks.csv file

#Calculating sum of the given data
print("Sum:",data.sum())

#Calculating minimum from the given data
print("Minimum:",data.min())

#Calculating maximum from the given data
print("Maximum:",data.max())

#Calculating mean of the given data
print("Mean:",data.mean())

#Calculating standard deviation of  the given data
print("Standard Deviation:",data.std())









