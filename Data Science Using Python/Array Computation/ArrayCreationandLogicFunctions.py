### Question 1: Create the ndarray and swap first two rows of the array

#Import libraries
import numpy as np

#Creation of an array using arange() and rehsape()
A = np.arange(25).reshape(5,5)
print('Before Swapping',A)

#Swap first two column of an array
A[[0,1]] = A[[1,0]]
print('After Swapping',A)

### Question 2: Create 1-D array of 20 evenly spaced element between 1 and 100

#Create an array using linspace()
x = np.linspace(1, 100, 20)

#Print an array
print(x)

"""
### Question 3: Create two random arrays A and B
a] check whether both the arrays are equal
b] Test the type of array element-wise
c] Compare two arrays element-wise
   So here random array is generated using numpy.random.randint(low, high, size)
   It is one of the function for generating random elements in array
   It returns an array of specified shape and fills it with random integers from low to high (exclusive), i.e. in the interval    of(low, high)

"""

#Create two random array between 0 to 100 with 5 elements each
A = np.random.randint(0,100,5)
B = np.random.randint(0,100,5)

#Check whether both the elements are equal
x = np.equal(A,B)
print(x)

#Test the type of array element-wise for real number
print(np.isreal(A))

#Test the type of array element-wise for complex number
print(np.iscomplex(B))

#Compare if A is greater than B element-wise
print(np.greater(A,B))

#Compare if A is lesser than B element-wise
print(np.less(A,B))