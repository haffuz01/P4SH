diary = {}

def main():
	choice = input("What would you like to do\nRead, Write or delete entries.\n").lower()
	if choice == "read":
		date = input("Which date would you like to read? ")
		read(date)
	elif choice == "write":
		ken = input("Date: ")
		entry = input("What do we have for today: ")
		write(ken, entry)
	elif choice == "delete":
		ken = input("Which date? ")
		delete(ken)
	elif choice == "end":
		exit()
	else:
		print("Incorrect input.")

def read(date):
	with open('diary.txt', 'r') as file:
		contents = file.read().split("\n")
		for content in contents:
			if content == "":
				continue
			ken, data = content.split(", ")
			diary[ken] = data
	print("----------------------------")
	print(diary[date], "\n" + "---------------------------")

def write(date, data):
	diary[date] = data
	with open('diary.txt', 'a') as file:
		file.write(date + ", " + data + "\n")

def delete(date):
	with open('diary.txt', 'r') as file:
		contents = file.read().split("\n")
		for content in contents:
			if content == "":
				continue
			ken, data = content.split(", ")
			diary[ken] = data
	diary.pop(date)
	print("Has been delted.")
	with open("diary.txt", "w") as ilaf:
		for i in diary:
			ilaf.write(i + ", " + diary[i] + "\n")

while True:
	main()


