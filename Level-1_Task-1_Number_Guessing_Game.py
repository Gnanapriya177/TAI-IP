import random

EasyLevel = 10
HardLevel = 5
def difficulty_level(level):
  if level == "easy":
    return EasyLevel
  else:
    return HardLevel

def check_number(number_choosed, number, attempts):
  if number_choosed < number:
    print("Your guess is too low")
    return attempts-1
  elif number_choosed > number:
    print("Your guess is too high")
    return attempts-1
  else:
    print(f"Your guess is right, the answer is {number}")

def game():
  print("NUMBER GUESSING GAME")
  print("Let me think of a number between 1 to 50")
  number = random.randint(1,50)
  print(number)
  level = input("Choose the level of difficulty... type 'easy' or 'hard': ")
  attempts = difficulty_level(level)
  number_choosed = 0
  while number_choosed != number:
    print(f"You have {attempts} attempts remaining")
    number_choosed = int(input("Make a Guess:" ))
    attempts = check_number(number_choosed, number, attempts)
    if attempts == 0:
      print("You are out of guesses... you lose!!!")
      return
    elif number_choosed != number:
      print("Guess again")

game()
    












