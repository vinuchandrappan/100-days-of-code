import random

choose=int(input("What do you chose? 0 for rock, 1 for paper and 2 for scissors: "))

computer= random.randint(0, 2)
print(f"computer_choice is {computer}")
if choose>=3 or choose<0:
  print("Invalid number") 
elif choose==0 and coomputer==2:
  print("You win")
elif computer>choose:
  print("You loose")
elif computer==choose:
  print("It's a draw") 
elif choose>computer:
  print("You wins")  
else:
  print("Invalid number")     