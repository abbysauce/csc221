from random import randint
num1=randint(1,10)
num2=randint(1,10)
right=0
print ("This quiz is timed")
import time
start_time= time.time()
question= "What is " + str(num1) + " times " + str(num2) + "?"
print (question)
answer= int(input("Enter a number: "))
if answer== (num1 * num2):
    print("That is correct!")
   right=right+1
