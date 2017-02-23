# -*- coding:utf-8 -*-
import csv

file = open("week6/message.csv")
csvResult = csv.reader(file, delimiter=',')
# array = ["Romi","Yunie"...]
# array[0] == "Romi"
# dicts = {0:"Romi",1:"Yunie"}
# dicts = {"Romi":0, "Julian":0}
# print(dicts)
# print(dicts["Glenn"])
# dicts["Glenn"] = 3 # "Glenn":3
# print(dicts)
# print(dicts["Glenn"])
# dicts = {"02-14":{"Romi":100, "Yunie": 200}, "02-15":{"Romi":130, "Yunie": 100}}
# dicts["02-14"]["Romi"] = 100

sayStatistic = {}
for row in csvResult:
	name = row[1]
	date = row[0]
	if not name in sayStatistic:
		sayStatistic[name] = 0
	sayStatistic[name] = sayStatistic[name] + 1
print(sayStatistic["박성훈 Julian"])


# import time
# date_str = "2017-02-16 10:34:39"
# date = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')