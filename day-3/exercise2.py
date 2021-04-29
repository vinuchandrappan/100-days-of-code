age=input("Your age: ")
age_in=int(age)
years_left=90-age_in
days_left=years_left * 365
weeks_left=years_left * 52
months_left=years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")