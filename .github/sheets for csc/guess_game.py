from random import randint 
from gasp.utils import read_number
number= randint(1,100)
userguess=0
print("I have thought of a number from 1 to 100")
number= randint(1,100)
answer= int(input("Enter a NUMBER: "))
while True:
   if answer > number:
      print("Try a lower number")
      userguess= userguess + 1
      answer= int(input("Make another guess: "))
   if answer < number:
      print("Try a higher number")
      userguess= userguess + 1
      answer= int(input("Make another guess: "))
   if answer == number:
      break
print("Well done that was my number! It was " + str(number))
print("That was " + str(userguess)+ " guesses")
from gasp.utils import read_yesorno
print (read_yesorno + ('Would you like another game? '))
