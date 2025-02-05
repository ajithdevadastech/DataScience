#**Payal is working on Strings**

# Different ways to initialize strings in python
A="Good"
B="Morning"
C="""Students"""
D='''From 
    Edureka''' #can be multiline
print(A,B,C,D)

# **She learns that there are various escape sequences provided in python
# that can be used to display quotes, newline.**

# Backslash
A='Hello!\nEdurekan'
print(A)
B=input('Cat goes?') # Taking input from user
print('Cats \'%s\''%B)

print("C:\\Python32\\Lib") # Simple text

# **Payal now takes names and surnames of
# all her friends as input, seperated by  ','**

Names=input('Names:').split(',') # Enter two name and seprate them by comma.
print(Names)

# capitalise the initial letter of second name.
print(Names[1].capitalize())

Surnames=input('Surnames: ').split(',') # Enter surnames for above namea and seprate them by comma.
print(Surnames)

# The the full name of second friend will be
print(Names[1].capitalize()+' '+Surnames[1].capitalize())

# Let us see some more functions on strings
quote1='''Happiness can be defined, in part at least, 
        as the fruit of the desire and ability to sacrifice 
        what we want now for what we want eventually
     '''
quote2='Sadness is but a wall between two gardens'

print('Quote 1 Startswith \'Happiness\': %s'%quote1.startswith('Happiness'))
print('Quote 2 Startswith \'Happiness\': %s'%quote2.startswith('Happiness'))
print('Quote 1 Endstwith \'gardens\': %s'%quote1.endswith('gardens'))
print('Quote 2 Endsswith \'gardens\': %s'%quote2.endswith('gardens'))

print('index of \'fruit\': %d'%quote1.index('fruit'))
print(quote1[60:65]) #slicing the strings for 60th to 64th index.
print(quote1[60:])
print(quote1[:60])
print(quote1[::-1]) # reverse of string
print(quote1[60:-16])

quote1.replace('fruit','result')
print(quote1) #no change why? Strings are immutable we need to assign to new one
quote3=quote1.replace('fruit','result')
print(quote3)

#**Payal wants to find out whether the given string is a number or text**

# if its text, she wants to change the case of string.
text=input('String:')
print(text.isnumeric())
print(text.isalpha())

print(text.isupper())
print(text.islower())

print(text.upper())

text=input('String:')
print(text.isnumeric()) # It will check if input is numeric or not.
print(text.isalpha())

print(dir(str)) # Returns valid attributes and methods of the parent class


