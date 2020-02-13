
#gess the number 
import random
num= random.choice(range(90))
for chance in range(5,-1,-1):
    z=int(input("gess the number"))
    if z>num:
        print("you gess is too high")
    elif z<num:
        print("your gess is too low")
    else:
        print(f"well done the number is {num}")
        print(f"\nyou complete game in {5-chance} attempt")
        break
    print(f"\nnow you have only {chance} attempt left.")
    if chance==0:
        print ("\n game over!")
        break
