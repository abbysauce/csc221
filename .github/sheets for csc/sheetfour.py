from random import randint 
number= randint(1,100)
print("I have thought of a number from 1 to 100")
answer=int(input("Enter a number: "))
if answer== number:
    print("Well done you have guessed my number")
if answer>number:
    print("Try a lower number")
if answer<number:
    print("Try a higher number")

