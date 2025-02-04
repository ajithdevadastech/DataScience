# Creating a dictionary
# James wants to insert Employee Data
emp_data={'Name':'James','Age':21,'Band':'C'}
print(emp_data)

# keys() method will return keys of dictionary
keys=emp_data.keys()
print(keys)

# values() method will return values of dictionary
print(emp_data.values())

# So now he wants to insert data of his team
team_data=dict.fromkeys(keys)
print('Team Data:',team_data)

# Team data
names=['Smith','Manali','Kabir']
ages=[21,28,22]
bands=['C','B','D']

# Inserting data
team_data['Name']=names
team_data['Age']=ages
team_data['Band']=bands

print('Team Data after inserting data:',team_data)

# Printing data from dictionary
print(team_data['Name'][1])

# He no longer requires Age attribute
team_data.pop('Age') # removing Age attribute
print('Updatad Team Data:',team_data)

# **James wants to create a dictionary that return country name if the code is provided**

country_name=['Hungary','Iceland','India','Indonesia',\
              'Iran, Islamic Republic of','Iraq','Ireland','Isle of Man',\
              'Israel','Italy','Jamaica','Japan','Jersey','Jordan']
country_code=['HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO']

country_dict=dict(zip(country_code,country_name)) # returns iterable in form of tuples

# Printing the Dictionary
print(country_dict)

# Let's try for country 'India' if we provide 'IN'

print(country_dict['IN'])


