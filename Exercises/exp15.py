from sys import argv
script=argv
filename=argv
txt=open('F:\python\sagar.txt','r')
print("Here's your file %r:"%'F:\python\sagar.txt','r')
print(txt.read())
print("Type the filename again:")
file_name=input(">")
txt_again=open('F:\python\sagar.txt','r')
print(txt_again.read())
