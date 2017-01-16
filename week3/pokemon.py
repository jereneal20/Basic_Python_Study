
leesanghae = 100
picachu = 100
while leesanghae > 0:
	damage = input()
	damage = int(damage)
	print("이상해씨를 공격:",damage)
	if damage > 30:
		print("정말로 막강한 공격이었다!")
	leesanghae = leesanghae - damage
	print("이상해씨는 심각한 피해를 입었다!! 남은 체력:", leesanghae)
	picachu = picachu - 20
	print("피카츄는 이상해씨에게 20의 피해를 입었다. 남은 체력: ",picachu)
print("이상해씨는 너무 큰 피해를 입어 쉬어야 한다")

## For Julian
# import random as ran
# result = ran.random()
# if result > 0.5:
# 	print("AA ", result)
# else:
# 	print("BB ", result)
