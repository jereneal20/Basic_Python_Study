number = 0
while number < 100:
	number = number + 1
	if number / 10 == 3:
		print("짝!!!")
	elif number / 10 == 6:
		print("짝!!!")
	elif number / 10 == 9:	
		print("짝!!!")
	elif number % 10 == 3:
		print("짝!!")
	elif number % 10 == 6:
		print("짝!!")
	elif number % 10 == 9:
		print("짝!!")
	else:
		print(number)
