from random import *
k = 1
while k<2:
    x = input("Press Enter to roll the dice...(Press 0 to Quit)")
    if x =="0":
        break
    else:
        i = 0
        while i<1:
            a = randint(1,6)
            print(a)
            break
print("Thank you for playing the game...")