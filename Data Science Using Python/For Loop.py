### Step 1: Iterate over a list

print("List Iteration")
l = ["Tit", "for", "Tat"]
for i in l:
    print(i)

### Step 2: Iterate over a tuple

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Tit", "for", "Tat")
for i in t:
    print(i)

### Step 3: Iterate over a string

#Iterating over a string
# Taking a string from user
s = input("Enter a string: ")
# checking for palindrome using the for loop
for i in range(0,len(s)//2):
    if(s[i] != s[len(s)-i-1]):
        found = False
        break
else:
    found = True
# Checking whether the given string and reversed string is same
if found:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

### Step 4: Iterate over a dictionary

# Iterating over dictionary
statesAndCapitals = {
    'Goa': 'Panjim', 'Maharashtra': 'Mumbai',
    'Karnataka': 'Bengaluru', 'Tamil Nadu': 'Chennai'
}

print('List Of given states and their capitals:\n')

# Iterating over values
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)

### Implementation of Fibonacci series using for loop

### Step 1: Take input from user

# Fibonacci series will start at 0 and continue upto below number
Number = int(input("\nPlease Enter the Range Number for which You Want to Print the Fibonacci Series : "))

### Step 2: Initialize first and second value from the inputs

First_Value = 0
Second_Value = 1

### Step 3: Generate and display fibonacci series

for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)

