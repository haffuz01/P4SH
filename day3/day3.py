fields = ("name", "age", "sex", "phone number", "class")

students = [
	#["abebe", 12]
	#["chala", 21]
	#["adsfa", 12]
]

for i in range(3):
	student = []

	for field in fields:
		data = input(f"What is your {field}: ")
		student.append(data)
	
	students.append(student)
	print("----------------")

student1 = {
	fields[0]:students[0][0],
	fields[1]:students[0][1],
	fields[2]:students[0][2],
	fields[3]:students[0][3],
	fields[4]:students[0][4],
}

student2 = {
	fields[0]:students[1][0],
	fields[1]:students[1][1],
	fields[2]:students[1][2],
	fields[3]:students[1][3],
	fields[4]:students[1][4],
}
student3 = {
	fields[0]:students[2][0],
	fields[1]:students[2][1],
	fields[2]:students[2][2],
	fields[3]:students[2][3],
	fields[4]:students[2][4],
}

for i in student1:
	print(i, student1[i])

for i in student2:
	print(i, student2[i])

