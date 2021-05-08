import random

stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

stages.reverse()


word_list=["monkey", "vampire", "donut"]
choosen_word=random.choice(word_list)

lives=6

display=[]
word_lenth=len(choosen_word)
for _ in range(word_lenth):
  display+="_"
print(display)  

end_of_game=False
while not end_of_game:
  guess=input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"You have already guessed {guess}")

  for letter in choosen_word:
    if letter==guess:
      print("Right")
    else:
      print("Wrong")
      
  for position in range(word_lenth):
    letter=choosen_word[position]
    if letter==guess:
      display[position]=letter
  print(display)
  
  if guess not in choosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives-=1
    if lives==0:
      end_of_game=True
      print("You lose")
  
  
  if "_" not in display:
    print("You win")    
  
  print(stages[lives])  