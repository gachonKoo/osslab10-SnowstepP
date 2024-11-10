import sys

number = int(sys.argv[1])

for i in range(number + 1):
	if range % i == 0:
		print(i, end = " ")


print()

