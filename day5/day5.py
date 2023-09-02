word = input("Give me a word: ")
word = word.replace(" ", "")

if word == word[::-1]:
	print("Your word is a palindrome.")
else:
	print("It is not.")
	
#without list

