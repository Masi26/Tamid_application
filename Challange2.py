#Masi Najafizehtab
#Tamid Application Challange 2
#Description: a program that acts as a calculator

#the main function is used to call upon other functions and define variables
def Main():
	Response = input("Welcome to the TAMID Calculator! \nWould you like to calculate something (y/n): ")
	Calculator(Response)

#the calculator function will do the calculations to solve the challange
def Calculator(Response):
	while Response == "y":	#allows the calculator to keep going until asked to stop
		Number_1 = int(input("Please enter the first number: "))
		Number_2 = int(input("Please enter the second number: "))
		method = input("Please enter your function: ")
		if method == "+":
			Result = Number_1 + Number_2
		if method == "-":
			Result = Number_1 - Number_2
		if method == "*":
			Result = Number_1 * Number_2
		if method == "/":
			Result = Number_1 / Number_2
		if method =="%":
			Result = Number_1 % Number_2
		print("Your result was:", Result, "!")
		Response = input("Would you like to calculate something (y/n): ")
	if Response == "n":
		print("Thanks for coming!")

Main()
