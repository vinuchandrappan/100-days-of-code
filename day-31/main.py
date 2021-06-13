# with open("weather_data.csv") as data_file:
#   data=data_file.readlines()
#   print(data)

# import csv

# with open("weather_data.csv") as data_file:
#   data=csv.reader(data_file)
#   temperatures=[]
#   for row in data:
#     if row[1]!="temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)


import pandas

data=pandas.read_csv("weather_data.csv")
# #print(data["temp"])

# data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)

'''taking average and mean'''
# average=sum(temp_list)/len(temp_list)
# print(average)
# same result:
# print(data["temp"].mean())

'''highest value from the list'''
# print(data["temp"].max())

'''Get data in columns'''
# print(data["condition"])
# #otherwise
# print(data.condition)

'''Get data in row'''
#print(data[data.day=="Monday"])

'''Row with max data'''
#print(data[data.temp==data.temp.max()])

'''temperature of Monday'''
#monday=data[data.day=="Monday"]
'''converting monday temp into farenheit'''
# monday_temp=int(monday.temp)
# monday_temp_F=monday_temp * 9/5 + 32
# print(monday_temp_F)

'''create dataframe from scratch'''
data_dict={
  "students":["Manu", "Tanu", "Jinu"],
  "scores":[76, 56, 65]
}

data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")