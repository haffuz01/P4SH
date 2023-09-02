import math

def square(num):
	print(num*num)

def root(num):
	print(math.sqrt(num))

user = input("square or root? ")
number = int(input("What's the number? "))

if user == "square":
	square(number)
elif user== "root":
	root(number)
else:
	print("Incorrect input")
