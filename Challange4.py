#Masi Najafizehtab
#Tamid Challange 4
#Description: a function, `isPalindrome?` that tests whether a string is a palindrome.
#main function is used to call upon other functions
def main():
	isPalindrome()

def isPalindrome():
	word = str(input("Please enter a String: "))
	string = word.lower()			#must have the string all in lower-case so that it will find palindrome regardless of capitalization
	
	n = len(string)					# n shows the length of string
	
	if n == 1:						#if string is only one letter, it will automatically be a palindrome
		print("True")
	else:
		for i in range(n//2):			#the range is in half because, first half must equal second half
			if string[i] == string[n-1 -i]:		#this will compare first letter to last, second letter to second to last and so on
				x = True
			if string[i] != string[n-1 -i]:
				x = False
		if x == False:
			print(word, "is not a palindrome!")
		if x == True: 
			print(word, "is a palindrome!")

			

main()
