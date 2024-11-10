import sys

number = int(sys.argv[1])

for i in range(number):
	if number % (i + 1) == 0:
		print(i + 1, end = " ")


print()

