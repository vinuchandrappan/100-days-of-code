
import random
letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",]
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the password generator")
pletter=int(input("How many lettrs do you want?\n"))
pnumber=int(input("How many numbers do you want?\n"))
psymbol=int(input("How many symbols do you want?\n"))

password1=[]
for char in range(1, pletter+1):
  password1.append(random.choice(letters))
for char in range(1, pnumber+1):
  password1+=random.choice(numbers)
for char in range(1, psymbol+1):
  password1+=random.choice(symbols)

random.shuffle(password1)
 

password=""
for char in password1:
  password+=char
  
print(f"Your password is {password}")  
  
  
    