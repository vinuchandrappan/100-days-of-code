from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  '''Takes the account data and return the printable format.'''
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
  '''Take the user guess and follower counts and returns if they got it right.'''
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"


#display the art
print(logo)
#score keeping
score=0
game_should_continue=True
#making account at position B becomes the next account at position A
account_b=random.choice(data)
#make the game repeatable.
while game_should_continue:
  account_a=account_b
  account_b=random.choice(data)
  
  #generate a random account from the game data
  account_a=random.choice(data)
  account_b=random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  #ask the user for a guess
  guess=input("Who has more folowers? Type 'A' or 'B': ").lower()
  #check if user is correct
  ##get the follower count of each account
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  is_correct=check_answer(guess, a_follower_count, b_follower_count)
  
  #clear the screen between the rounds 
  clear()
  print(logo)
  #give the user a feedback on their guess
  if is_correct:
    score+=1
    print(f"You're wright. The score is {score}.")
  else:
    game_should_continue=False
    print(f"You're wrong. The final score is {score}.")  
    






