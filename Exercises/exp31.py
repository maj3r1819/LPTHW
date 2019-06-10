while(1):
    print("You enter a dark room with two doors, Do you go through door #1 ir door #2")
    door=input(">")
    if(door=="1"):
        print("Theres a giant bear here eating a cheesecake. what do you do?")
        print("1.Take the cake")
        print("2.Scream at the bear")

        bear=input(">")

        if(bear=="1"):
            print("The bear eats your face off. Good job!")
        elif(bear=="2"):
            print("The bear eats your leggs off.Good job!")
        else:
            print("well,doing %s is probably better. Bear runs away."%bear)
        
    elif(door=="2"):
        print("you stare into the endless abyss at Cthulhu's retina")
        print("1.Blueberries.")
        print("2.Yellow jacket clothespins.")
        print("3. Understanding revolvers yelling melodies.")
        insanity=input(">")
        if(insanity =="1" or insanity =="2"):
            print("Your body survives powered by a mind of jello. Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck.Good job!")
    else:
        print("You stumble around and fall on a knife and die. Good job!")

