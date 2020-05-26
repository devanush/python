import random
a=1
while a:
    n=int(input("Enter the random number between 0 to 20: "))
    r=random.randint(0,20)
    if n>r:
        print("Your guessing is high")
        a=int(input("1.continue\n2.Quit\n"))
        if(a==2):
            exit()
    elif n<r:
        print("your guessing is low")
        a=int(input("1.continue\n2.Quit\n"))
        if(a==2):
            exit()
    elif n==r:
        print("Your guessing is correct")
        a=int(input("1.continue\n2.Quit\n"))
        if(a==2):
            exit()
    else:
        print("Invalid number")
"""
                    # (or) Dice rolling simulator
            
import random
print("Dice rolling simulator")
a=1
while a:
    n=int(input("Enter your number min=1, max=6: "))
    r=random.randint(0,20)
    if n>r:
        print("Your guessing is high")
        a=int(input("1.Roll Again\n2.Quit\n"))
        if(a==2):
            exit()
    elif n<r:
        print("your guessing is low")
        a=int(input("1.Roll Again\n2.Quit\n"))
        if(a==2):
            exit()
    elif n==r:
        print("Your guessing is correct")
        a=int(input("1.Roll Again\n2.Quit\n"))
        if(a==2):
            exit()
    else:
        print("Invalid number")


"""
