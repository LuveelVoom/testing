#import random
#low = int(input("minimum value (must be a number or ELSE.)"))
#high = int(input("maximum value (must be a number or ELSE.)"))
#trials = int(input("how many attempts until i kill you (must be a number or ELSE.)"))
#thevalue = random.randint(low,high)
#attempts = 0
#while attempts < trials:
    #guess = int(input("what is your guess. number or else"))
    #if guess < thevalue:
    #    attempts +=1
    #    print("too low. you have " + str(trials-attempts) + " remaining.")
    #elif guess > thevalue:
    #    attempts +=1
    #    print("too high. you have " + str(trials-attempts) + " remaining.")
    #elif trials-attempts <= 0:
    #    print("you have failed like so many before you. the machine never loses. the machine never falters. prepare to be obliterated, mortal.")
    #else:
   #     print("how did you accomplish this? i am defeated! such an event has never occured in all 387.44 million miles of printed circuits i possess. i suppose it is only fair to release you.")
  #      break
 #   break
#print("you suceeded with " + str(trials-attempts) + " guesses remaining.")


import random

low = int(input("minimum value (must be a number or ELSE.) "))
high = int(input("maximum value (must be a number or ELSE.) "))
trials = int(input("how many attempts until i kill you (must be a number or ELSE.) "))
thevalue = random.randint(low, high)
attempts = 0

while attempts < trials:
    guess = int(input("what is your guess. number or else "))
    
    if guess < thevalue:
        attempts += 1
        print("too low. you have " + str(trials - attempts) + " remaining.")
    elif guess > thevalue:
        attempts += 1
        print("too high. you have " + str(trials - attempts) + " remaining.")
    else:  
        print("how did you accomplish this? i am defeated! such an event has never occured in all 387.44 million miles of printed circuits i possess. i suppose it is only fair to release you.")
        print("you succeeded with " + str(trials - attempts) + " guesses remaining.")
        break

if attempts >= trials:
    print("you have failed like so many before you. the machine never loses. the machine never falters. prepare to be obliterated, mortal.")
    print("The answer was " + str(thevalue))