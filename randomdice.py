from random import randint
repeat = True
while repeat:
    print("You rolled dice A:",randint(1,6))
    print("You rolled dice B:",randint(1,6))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()