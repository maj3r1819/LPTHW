from sys import argv

script = argv
input_file = argv

def print_all(f):
    print(f.read())

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file=open('F:/python/sagar.txt','r')
print("First let's print the whole file:\n")
print_all(current_file)

line_no=1
with current_file as x:
    for line in x:
        print(line_no, line)
        line_no+=1
