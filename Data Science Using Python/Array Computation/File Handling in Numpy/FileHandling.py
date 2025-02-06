### Loading and Saving Data in Binary file

#Import the library
import numpy as np

#Creating the array using zeros() and ones()
a = np.zeros((3,3))
b = np.ones((3,3))
print('a=',a)
print('b=',b)

#SavE arrays to binary file
np.save('file1.npy',(a,b))

#Load data from binary file
c=np.load('file1.npy')
print(c)

### Loading and saving data in text and csv file

#Import the library
import numpy as np

#Create an array
a = np.arange(0,10,1)
print(a)

# Save array to text file and reading the file
b = np.savetxt('file2.txt', a, delimiter=', ')
c = open("file2.txt", 'r')  # open file in read mode

print("the file contains:")
print(c.read())

#Recover data from text file
d=np.genfromtxt('file2.txt')
print(d)

#Load a marks.csv file
data = np.loadtxt('marks.csv',delimiter=',',usecols=(5),skiprows=1)
print(data)

