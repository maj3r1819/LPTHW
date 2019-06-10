from sys import argv
from os.path import exists
script=argv
print("Copying from %s to %s"%('F:\python\sag.txt','F:\python\pagar.txt'))

in_file=open('F:\python\sag.txt')
indata=in_file.read()
print("The input file is %d bytes long"%len(indata))
print("Does the output file exist! %r"%exists('F:\python\pagar.txt'))
print("Ready,hit RETURN to continue ,CTRL-C to abort.")
input()
out_file=open('F:\python\pagar.txt','w')
out_file.write(indata)
print("Alright,all done!")
out_file.close()
in_file.close()
      
