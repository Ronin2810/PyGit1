from random import *
print("Welcome To Biased Dice")
k = 1
while k<2:
    x = input("Press Enter to roll the dice....(Press 0 to Quit)")
    if x =="0":
        break
    else:
        i = 0
        while i<1:
            a = randint(1,10)
            if a>6:
                print("6")
            else:
                print(a)
            break
print("Thank you for playing the game...")
