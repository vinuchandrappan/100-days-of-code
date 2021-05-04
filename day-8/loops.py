#Calculaing average student height

st_height=input("Enter a list of student heghts: ").split()
for n in range(0, len(st_height)):
  st_height[n]=int(st_height[n])
print(st_height)  

total_height=0
for height in st_height:
  total_height += height

#print(total_height)

total_length=0
for length in st_height:
  total_length += 1
#print(total_length) 

avg_height=round(total_height / total_length)
print(f"The average height is {avg_height}")