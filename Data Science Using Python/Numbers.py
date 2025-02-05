# Different types of numbers supported by python
A=10 # Integer
B=20.1 # float
c=10+5j # complex
print(A,B,c)
print(type(A),type(B),type(c))


# **Payal is beginner in Python. She is just sitting outside and studying Python.
# Let us see how she applies Python here.**

chickens=input('Number of chickens:') # By default it will take input in string
eggs=input('Eggs per day:')
#print('Number of eggs each chicken will lay?',eggs/chickens) # Why? Type error. We cannot divide two strings.

# Note: Consider the following example, On the farm, there are 25 chickens, and they collectively lay 120 eggs.

# **She tries to rectify the error by converting type to integer**
print('Number of eggs each chicken will lay?',int(eggs)/int(chickens))

#**It is not possible to lay half egg right?**
each_chicken_egg=int(eggs)//int(chickens)
print('Number of eggs each chicken will lay?',each_chicken_egg)

#**Every chicken will give at least 4 eggs. That makes sense.
#But there is one more problem: Which chickens are laying more eggs or vice versa.**

# How many eggs all the chickens should lay? tuff...
eggs_presumed=int(each_chicken_egg)*int(chickens)
print('Total eggs all the chickens should lay:',eggs_presumed)
print('Total eggs laid originally:',eggs)
more_eggs=int(eggs)-eggs_presumed
print('number of chickens laying more eggs:',more_eggs)

print('Means %i chickens are laying more eggs than average eggs'%(more_eggs)) # This is basic formatting in python

#**Now, Payal wants to measure the area of the farm. She asks her dad to enter length and breadth of the farm.**
# %i represents an integer value
length, breadth=input('Enter length and breadth of the farm (separated by comma):').split(',')
area=float(length)*float(breadth)
print('Area of field:',area)

# Some of the land is used as grazing land. So, the usable area should be-
grazing_land = 200 # in square meters
total_area = 500
area = total_area - grazing_land
print('Usable area: %i meter square'%area)

# Rest of the area is evenly divided into 7 parts
print('Area for each section:',area/7)

#**The precision level is so high, Payal needs just 4 decimal places**

print('Area for each section %0.4f'%(area/7))

# Formatting can also be done using format() function
print('Area for each section {:.3f}'.format(area/7))

#**Later she learnt how to use complex number in python**
A=10+3j
B=5-10j

# Operations on complex numbers
print('Addition of two complex numbers:',A+B)
print('Mulitplication of a complex number and an integer:',A*2)
print('Real part of a complex number:',A.real)
print('Conjugate of complex number:',A.conjugate())
print('Imaginary part of a complex number:',A.imag)

# comparison of real part to an integer
print(A.real == 10)

# left shift and right shift
# binary of 5= 00000101 so left shifting by two places
# 101(5) << 2 => 10100 which is 20 in decimal

print(5<<2) #20
print(5>>2) #1

# To represent a number in various number systems
test=int(input('Enter a number:')) # enter any input in integer
print('octal %s:'%oct(test))
print('binary %s:'%bin(test))
print('hexadecimal %s:'%hex(test))
# Why %s? These functions return specific value in string for representation

# Exponents and powers
print('2 to 5th power: %d'%2**5)
print('three times ten to the fifth power: %d'%3e5) # Python supports E-notation(is lso queal to 3*pow(10,5))

# While playing with numbers she noticed something unsual
print(1.1+2.2==3.3)

# How can that be possible?
x=1.1+2.20
y=3.3
print(x==y)

#  It due to machine error. Machines cannot store decimals precisely
print(x)
print(y)

F=float(input('Enter the temperature in fahrenheit: '))
C=5/9*(F-32)
print('Celcuis: %0.1f'%C)




