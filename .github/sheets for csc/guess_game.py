from random import randint 
number= randint(1,100)
userguess=0
print("I have thought of a number from 1 to 100")
answer=int(input("Enter a number: "))
if answer== number:
    print("Well done you have guessed my number")
while answer > number:
    print("Try a lower number")
    userguess= userguess + 1
    answer=int(input("Enter a number "))
while answer < number:
    print("Try a higher number")
    userguess= userguess + 1
    answer=int(input("Enter a number "))
print("That was " + str(userguess)+ " guesses")
print(" Would you like another game ")
