import random

print("Welcome to Zach's guessing game!!")

#DEFINE CONSTANTS
MIN_VALUE = 1
MAX_VALUE = 10
MAX_TRIES = 3

number = random.randint(MIN_VALUE, MAX_VALUE)
tries = 0

print("I am thinking of a number between {mini} and {maxi}\nCan you guess it?".format(mini=MIN_VALUE, maxi=MAX_VALUE))

#GAME LOOP
while tries < MAX_TRIES:

  #PROMPT USER FOR GUESS
  guess = int(input())

  #GIVE APPROPRIATE RESPONSE
  if guess == number:
    print("You guessed my number. YOU WIN!!")
    break

  elif guess > number:
    print("Your guess is too large.")

  else:
    print("Your guess is too small.")
  
  #INCREMENT TRIES
  tries += 1

#TOO MANY UNSUCCESSFUL TRIES
if (tries >= MAX_TRIES):
  print("You have used all of your tries. YOU LOSE.")
