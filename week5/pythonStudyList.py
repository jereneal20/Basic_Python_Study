import string

hothotRoom = []
romiRoomParty = ["Romi","Aria","Suzy","Yunie","Grace"]
pythonStudy = ["Julian","Yunie", "Eunice", "Romi", "Suzy", "Grace", "Demon"]
pythonAbsent = ["Grace","Demon","Suzy"]
# print(pythonStudy[3])

def notInPythonStudy():
	print("하태하태 방에 있는데 python 스터디는 안하는 싸람들!!!!")

def roomPartyAndPython():
	print ("Python 스터디도 오고 룸파티에도 가는 사람들! ^^^")
	for name in pythonStudy:
		if not name in pythonAbsent and name in romiRoomParty:
			print(name)

def presentCheck():
	print ("Python 스터디 출석한 사람 ^^^")
	for name in pythonStudy:
		if not name in pythonAbsent:
			print(name)
			
def absentCheck():
	print ("Python 스터디 결석한 사람 - _-")
	for name in pythonStudy:
		if name in pythonAbsent:
			print(name)			

# number = 0
# while number < len(array):
# 	print(array[number])
# 	number = number + 1

# print(string.ascii_lowercase)
roomPartyAndPython()
# presentCheck()
# absentCheck()
# notInPythonStudy()
# print ("Genie")
