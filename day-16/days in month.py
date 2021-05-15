def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      return False 
    return True
  return False

def days_in_month(year, month):
  month_days=[31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
  if is_leap_year(year) and month ==2:
    return 29
  return month_days[month-1]
    
 
year=int(input("Enter a year: "))
month=int(input("Enter a month: ")) 
days=days_in_month(year, month)
print(days)
       