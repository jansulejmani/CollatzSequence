import sys

def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
	else:
		print(3 * number + 1)
		return 3 * number + 1

print("Type in an integer: ")
num = input()

while True:
	try:
		num = collatz(int(num))
	except ValueError:
		print("Enter a goddamn integer.")
		sys.exit()
	if num == 1:
		break