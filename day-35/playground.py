# def add(*args):
#   print(args[2])
#   sum=0
#   for n in args:
#     sum+=n
#   return sum  

# print(add(3, 2, 5, 6))

class Car:
  
  def __init__(self,  **kw):
    self.make=kw.get("model")
    self.model=kw.get("model")
    
my_car=Car(make="Nissan", model="GT-R")
print(my_car.model)    