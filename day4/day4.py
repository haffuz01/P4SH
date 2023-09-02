def main():
	number = int(input("Give me a numebr: "))
	if is_even(number):
		print("Your number is even")
	else:
		print("Your number is odd")

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

main()