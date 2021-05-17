from random import randint

easy_level=10
hard_level=5

def check_answer(guess, answer, turns):
  if guess>answer:
    print("Too high.")
    return turns-1
  elif guess<answer:
    print("Too low.")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}.")    

def set_difficulty():
  level=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level=="easy":
    return easy_level
  else:
    return hard_level
def game():
  print("Welcome to the number guessing game...")
  print("I'm guessing a number between 1 and 100 ")
  answer=randint(1, 100)
  print(f"The correct answer is {answer}")
  
    
  turns=set_difficulty()
  

  guess=0
  while guess!=answer:
    print(f"You have {turns} attempts to guess the number.")
    guess=int(input("Make a guess: "))
    turns=check_answer(guess, answer, turns)
    if turns==0:
      print("You have run out of turns, you lose.")
      return
    elif guess!=answer:
      print("Guess again.")      
game()         

