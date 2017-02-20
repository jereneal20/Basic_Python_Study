# -*- coding:utf-8 -*-
import csv
import string

# csvFile = open("message.csv", 'r')
# csv.reader(csvFile, deliminator=',')

file = open("Basic_Python_Study/week6/message.csv")
csvResult = csv.reader(file, delimiter=',')
julianSayNumber = 0
graceSayNumber = 0
romiSayNumber = 0
genieSayNumber = 0
for row in csvResult:
	if 'Julian' in row[1]:
		julianSayNumber = julianSayNumber + 1
		# print (row)
	elif 'grace' in row[1]:
		graceSayNumber = graceSayNumber + 1
	elif 'Clare' in row[1]:
		print(row[2])
		romiSayNumber = romiSayNumber + 1
	elif '강성구' in row[1]:
		genieSayNumber = genieSayNumber + 1
		# print (row)
print(julianSayNumber)
print(graceSayNumber)
print(romiSayNumber)
print(genieSayNumber)
print ("Hello World")


# import numpy as np
# import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r^', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()