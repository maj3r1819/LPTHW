people=30
cars=40
buses=15
if(cars>people):
    print("we should take the cars")
elif(cars<people):
    print("we should not take the cars")
else:
    print("we cant decide")

if(buses>cars):
    print("thats too many buses")
elif(buses<cars):
    print("maybe we could take the buses")
else:
    print("we still cant decide")

if(people>buses):
    print("Alright,lets just take the buses")
else:
    print("Fine , lets stay home then")
