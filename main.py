start=input("What's Your Name: ")
print("Hello " + start + "!")

while True:
    g = int(input("Guess a number from 0-100: "))
    if g==50:
        print("Correct! Good Job!!!\n")
        break
    elif g>= 51:
        print("Wrong! Guess Lower!!!\n")
    elif g<=49:
      print("Wrong! Guess Higher!!!\n")

import random
n = random.randint(0,100)

second=input("Would You like do try again? Enter Yes or No:\n ")
if second == "Yes":
  while True:
    f = int(input("Guess a number from 0-100: "))
    if f==n:
      print("Good Job!!! Have a good day!!!\n")
      break
    elif f>= n:
        print("Wrong! Guess Lower!!!\n")
    elif f<=n:
      print("Wrong! Guess Higher!!!\n")
if second == "No":
  print("Aww you're no fun. Have a good day")
