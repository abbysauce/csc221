from random import randint
right=0
numquestion= 0
print ("This quiz is timed and you need to atleast get ten questions right")
import time
start_time= time.time()

num1= randint(1,10)
num2= randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"

while right<10:
  print(question)
  numquestion= numquestion + 1
  answer=int(input("Enter a number: "))
if answer== (num1 * num2):
  print("That is correct!")
  right=right+1
if answer!= (num1 * num2):
  print("Sorry that isnt correct")
num1, num2 =randint(1,10), randint(1,10)
question= "What is " + str(num1) + " times " + str(num2) + "?"

end_time= time.time()
total_time=end_time-start_time
print("Your total time was " + str(total_time))
print(" I asked you" + str(numquestion) + "question's. You got " + str(right) + " of them right.")