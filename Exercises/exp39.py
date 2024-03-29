# create a mapping of state to abbreviation 
states={'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}

# create a basic set of states and some cities in them
cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities 
print('-'*25)
print("NY state has :",cities['NY'])
print("OR state has :",cities['OR'])

#print some states
print('-'*25)
print("Michigans's abbreviation is :",states['Michigan'])
print("Florida's abbreviation is :",states['Florida'])

# print every state abbreviation
print('-'*25)
for state,abbrev in states.items():
    print("%s is abbreviatied %s"%(state,abbrev))


#print every city in state
print('-'*25)
for abbrev, city in cities.items():
    print("%s has the city %s"%(abbrev,city))

# now do both at the same time                             
print('-'*25)
for state,abbrev in states.items():
    print("%s state is abbreviated %s and has city %s"%(state,abbrev,cities[abbrev]))

#safely get an abbreviation by state that might not be there
print('-'*25)
state=states.get('Texas',None)
if not state:
    print("Sorry ,no Texas")

#get a city with a default value
city=cities.get('TX','Does Not Exist')
print("The city for the state 'TX' is :%s"%city)
