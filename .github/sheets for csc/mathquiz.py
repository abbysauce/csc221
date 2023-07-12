from random import randint
right=0
print ("This quiz is timed")
import time
start_time= time.time()
num1= randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
  num1=randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!=(num1 * num2):
  print("sorry that is incorrect")
num1= randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
  num1=randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("sorry that is incorrect")
num1= randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
  num1=randint(1,10)
num2= randint(7,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("sorry that is incorrect")
num1= randint(5,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
  num1=randint(4,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("sorry that is incorrect")
num1= randint(1,10)
num2= randint(3,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
  num1=randint(1,10)
num2= randint(2,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer=int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("sorry that is incorrect")
end_time= time.time()
total_time=end_time-start_time
print("Your total time was " + str(total_time))
print(" I asked you 10 question. You got " + str(right) + " of them right.")
if right<6:
  print("You got less than six question right, you did not pass the quiz")
if right>6:
  print("Well done, you have passed the quiz")