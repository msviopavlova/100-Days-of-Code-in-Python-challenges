#with open("weather_data.csv") as data_file:#
 #   data = data_file.readlines()
  #  print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dictionary = data.to_dict()
#
# print(data_dictionary)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# sumof = 0
# for i in temp_list:
#     sumof += i
# average_of_temperatures = sumof/len(temp_list)
# print(average_of_temperatures)
#
# print(data["temp"].max())

#print(data[data.temp == data.temp.max()])

# create a dataframe from scratch

# data_dictionary_example  = {
#     "students": ["Amy","Jack","Angela"],
#     "scores": [76,54,65]
#     }
#
# data = pandas.DataFrame(data_dictionary_example)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrels = len(data[data["Primary Fur Color"]=="Cinnamon"])
blacl_squirels = len(data[data["Primary Fur Color"]=="Black"])
gray_squirrels = len(data[data["Primary Fur Color"]=="Gray"])

new_squirrel_count = {
    "Fur color" : ["red", "black", "gray"],
    "Count" : [red_squirrels, blacl_squirels, gray_squirrels]
    }

count = pandas.DataFrame(new_squirrel_count)

count.to_csv("squirrels_count.csv")