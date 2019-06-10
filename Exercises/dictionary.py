"""
dictionary
print(dict[' '])
dict.copy()
dict.update('':)
del dict[' ']
dict.items()
dict.keys()
dict.sort()
len(dict)
type(dict)
dict.popitem()
dict.pop()
dict.values()
dict.get()

"""

d = {'Tim': 18,'Charlie':12,'Tiffany':21,'Robert':25}
print(d['Tiffany'])


#copying keys and values in a new dictionary
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
boys={'Tim': 18,'Charlie':12,'Robert':25}
girls={'Tiffany':22}
studentX=boys.copy()
studentY=girls.copy()
print(studentX)
print(studentY)


#updates the dictionary by adding new elements
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
s.update({'Sarah':19})
print(s)

#deleting an element in the dictionary
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
del s['Charlie']
print(s)


#when code was executed, it returns a list of items(key and value) from dict
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Lists: %s"%(s.items()))
print("only names of students: %s"%(s.keys()))

#checks if a given key already exits
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
boys={'Tim': 18,'Charlie':12,'Robert':25}
girls={'Tiffany':22}
for key in (s.keys()):
    if key in (boys.keys()):
        print(True)
    else:
        print(False)
"""
#Sorting the dictionary in alphabetical order
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}        
boys={'Tim': 18,'Charlie':12,'Robert':25}
girls={'Tiffany':22}
students=s.keys()
students.sort()
for S in students:
    print(":",join((S,str(s[S]))))
"""

#lenght of the dictionary
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}        
print("Length : %d"%len(s))



#variable type
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}        
print("Variable Type : %s"%type(s))


#Dictionary Str(dict)
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}        
print("printable string :%s"%str(s))
v=str(s)
print("Length of the string is : %d"%len(v))


#pop
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
s.popitem()
print(s)
s.pop('Tim')
print(s)

#values
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Values are: %s"%s.values())


#get
s={'Tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("element on 'Tim' is",s.get('Tim'))



