temp = 40

if temp >= 100:
	print("Very hot")
elif temp > 60:
	print("Hot")
elif temp <= 60 and temp >= 50:
	print("Not hot")
elif temp < 50 and temp > 32:
	print("Cold")
elif temp <= 32 and temp > 0:
	print("Freezing")
else:
	print("Sub-zero")

raining = temp <= 30
sunny = temp >= 60 and raining == False

if sunny:
	print("Sunny")
elif raining:
	print("Raining")
else:
	print("Cloudy")

num = 0
while True:
	if num == 5:
		break
	else:
		num += 1
	print(num)

for rain in range(3):
	while raining:
		print("Raining")
		break
	else:
		print("Not raining")

for i in range(3):
	print("hello world")

