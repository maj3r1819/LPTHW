from sys import argv
script=argv
user_name='Sagar'
prompt='>'
print("Hi %s, Im the %s script"%(user_name,script))
print("Id like to ask you a few questions.")
print("Do you likeme %s?"%user_name)
likes=input(prompt)
print("Where do you live %s?"%user_name)
lives=input(prompt)
print("what kind of computer do u have?")
computer=input(prompt)
print("""
Alright, so you said %r about liking me.
You live in %r .Not sure where that is.
And you have a %r computer. Nice.
"""%(likes,lives,computer))
