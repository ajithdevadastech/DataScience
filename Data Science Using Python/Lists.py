# Initializing list
lst=["zero",1,2,3,4,5,'six']
print('List: ',lst)

# Nested list
my_list = ["cat", [1,2,3], ['a','b','c']]

#Indexing in list
print('First item of list:',my_list[0])
print('Second item of list:',my_list[1])
print('Third item of list:',my_list[2])
print('Third item of list and second item of list inside it:',my_list[2][1])

# length of list
length_of_list=len(my_list) # len() is a built-in function can be used with any iterable
print('Length of a list:',length_of_list)

# Proper indexing
print('Element at index -%d:'%(length_of_list),my_list[-length_of_list]) # will print first element of list

# It will give error
#print('Element at index %d:'%(length_of_list),my_list[length_of_list]) # It will give 'Index out range' error, because it is not a valid index

# **Wilson wants to input his sales of the week in list**

sales=map(int,input('Sales data(seperated by comma): ').split(',')) # Enter data only in integer and add comma to seprate them, For exmple. we have entered 123 at second index
print('Sales of the week:',sales)

# Map return an iterable, so wilson will have to convert it to a list
sales=list(sales)
print('Sales of the week:',sales)

# To just print the sales of first 5 days
print('Sales of first 5 days:',sales[:5])

# Apparently wilson made a mistake in entering data

index=sales.index(123)
sales.remove(123)
sales.insert(index,112) # entering new value at a index where '123' was located
print('Sales after correction: {}'.format(sales))


#**He wants to sort the sales in ascending order**
sales.sort()
print('Sorted sales in ascending order:',sales)
# To print in reverse order, :: means nothing for first argument and second argument.
# :: works as-> [start:stop(exclusive):step]
# Third parameter is required number of steps to take
print('Sorted sales in descending order:',sales[::-1])

# More about the ::

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print('Odd numbers:',numbers[::2])  # To print odd only
print('Even numbers:',numbers[1::2]) # To print even only

# **Now Wilson wants to add data for second week to sales**

second_week=[651,752,673,85,567,750]
sales.extend(second_week)
print('Sales in last two weeks:',sales)

# Well second_week does not have data for last day
last_day=int(input('Last day sales:')) # Take value for last day
sales.append(last_day)
print('Sales in last two weeks(appended last day sales):',sales)

# Total sales
print('Total sales:',sum(sales))

# Maximum Sales
print('Maximum Sales:',max(sales))

# Minimum Sales
print('Minimum Sales:',min(sales))

# printing list the elegant way
print('Sales: ',end='') # 'end' argument appends a string after the last value, default is a newline.
print(*sales,sep='|')   # 'sep' argument inserts a string between multiple values





