print("love calulator")
name1=input("Your name: \n")
name2=input("Their name: \n")
together=name1+name2

l_together=together.lower()
t=l_together.count("t")
r=l_together.count("r")
u=l_together.count("u")
e=l_together.count("e")

true=t+r+u+e

l=l_together.count("l")
o=l_together.count("o")
v=l_together.count("v")
e=l_together.count("e")

love=l+o+v+e

score=int(str(true)+str(love))

if score<10 or score>90:
  print(f"Your love score is {score}, you are going together like coke an mentos")
elif score>=40 and score<=50: 
  print(f"Your love score is {score}, you are alright")
else:
  print(f"Your love score is {score}")  