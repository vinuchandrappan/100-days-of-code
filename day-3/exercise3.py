#Tip calculator
Bill=float(input("What is the total bill? "))
percent_tip=int(input("What percentage would you like to give? 10, 12 or 15? "))
tip1=percent_tip / 100
total=Bill * tip1
split=input("How many people to split the bill? ")
individual=round(float(total) / float(split), 2)
print(f"Each should pay {individual}")           