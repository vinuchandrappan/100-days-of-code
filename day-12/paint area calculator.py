import math
def paint_calc(height, width, cover):
  area=height*width
  n_cans=math.ceil(area/cover)
  print(f"You will need {n_cans} cans of paint")


p_height=int(input("Height of the wall: "))
p_width=int(input("Width of the wall: "))
coverage=5
paint_calc(height=p_height, width=p_width, cover=coverage)




 