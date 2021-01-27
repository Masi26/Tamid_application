#Masi Najafizehtab
#Tamid Application Challange 3
#Description: a function that takes a list of strings an prints them, one per line,
#in a rectangular frame.

#the main function is used to call upon other functions
def main():
	Execution()

def Execution():
#in this section the desired list is creaeted
	text = []				
	number = int(input("Please enter the number of words in list: "))
	for i in range(number):
		word = input("Please enter the word: ")
		text.append(word)
#in this section the longest word is determined
	length_list = len(text)
	Maximum_word = text[0]
	for i in range(length_list):
		if len(text[i]) > len(Maximum_word):
			Maximum_word = text[i]
	print(Maximum_word)
#in this section the desired shape is printed
	print("*"* (len(Maximum_word)+4))	#4 stars is added to account for the one star on each side & for the space on each side
	for l in range(length_list):
		print("*", text[l]+ " " * (len(Maximum_word) - len(text[l])), "*")
	print("*"* (len(Maximum_word)+4))


main()
