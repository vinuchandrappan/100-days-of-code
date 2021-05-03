print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to the Treasue hunt!!!")
print("Your mission is to find the treasure")
road=input('You are at a crossroad where you want to go? "left" or "right" ?')
if road=="left":
  lake=input("You came to a lake. There is an island on the middle of the lake. Type 'wait' for the boat or 'swim' to swim: ")
  if lake=="wait":
    island=input("You arrived at the island unharmed. There is a house with 3 doors. One red, one blue and one yello. Which colour do you choose? ")
    if island=="red":
      print("You entered a room of beasts. GAME OVER.")
    elif island=="blue":
      print("The room leaded to a cliff. GAME OVER.")
    elif island=="yellow":
      print("You got the treasue. You Win ")
    else:
      print("wrong instruction") 
  else:
    print("You were caught by Crocodiles. GAME OVER. ") 
else:
  print("Wrong direction. GAME OVER.")           
  