# bmi Calculator version 2.0

print("Let's check your bmi")
height=float(input("Your height in m: "))
weight=int(input("your weight in kg: "))
bmi=round(weight / height ** 2)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi<25:
  print(f"Your BMI is {bmi}, you are normalweight")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are overweght") 
elif bmi<35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically obese")
       