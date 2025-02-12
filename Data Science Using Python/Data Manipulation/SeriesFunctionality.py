# Import the required libraries

import pandas as pd
import numpy as np

# 1.1 Create a pandas Series from a list  x = [13, -5, 7, 19]
x = [13, -5, 7, 19]
s1 = pd.Series(x)

# Print the series and observe the default indices created
print(s1)

# 1.2 Create a series using a numpy array

y = np.array([23, 3., 7, 11])
s2 = pd.Series(y, index=['a', 'b', 'c', 'd'])

print(s2)

# Note that indices are specifies at the time of creation.

# Check the data type of the series
print(s2.dtype)

# 1.3 Get the values and index of the series

print("Values:", s2.values)

print("Index:", s2.index)

# 1.4 Access the elements of Series

print("Third element: ", s2.iloc[2])

print("First two elements:\n")
print(s2[0:2])

print("Element having index 'd':")
print(s2['d'])

# 1.5 Assign new values to the elements

s2['a'] = 10

s2.iloc[1] = 11
print(s2)

##### Question 2:

"""
From the raw data below create a pandas Series

'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'

    1) Print all elements in lower case
    2) Print all the elements in upper case	
    3) Print the length of all the elements
"""

# 2.1
s = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.lower())

# 2.2

print(s.str.upper())

# 2.3

print(s.str.len())

##### Question 3:

"""
From the raw data below create a pandas Series

' Arya', 'John ', ' jack ', 'Sam'

    1) Print all elements after stripping spaces from the left and right
    2) Print all the elements after removing spaces from the left only
    3) Print all the elements after removing spaces from the right only
"""

# 3.1
s = pd.Series([' Arya', 'John ', ' jack ', 'Sam'])

print(s)
print(s.str.strip())

# 3.2

print(s.str.lstrip())

# 3.3

print(s.str.rstrip())

