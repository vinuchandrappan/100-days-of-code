numbers=[1, 2, 3]
new_numbers=[n+1 for n in numbers]
#print(new_numbers)

n_ame="ganesha"
letter_list=[letter for letter in n_ame]
#print(letter_list)

range_list=[num*1 for num in range(1, 5)]
#print(range_list)

names=["Anandu", "Vinu", "Ponnu", "Devgan", "thaarika"]
short_names=[name for name in names if len(name)<6]
#print(short_names)
long_names=[name.upper() for name in names if len(name)>5]
#print(long_names)

