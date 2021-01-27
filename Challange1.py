#Masi Najafizehtab
#Tamid Application
#Description: Given two sorted arrays (*arr1*, *arr2*) and a number, *k*, create a method,'sortArrays` that returns a sorted array of the first *k* elements.

def Main():			#the main function is used to call upon other function and define varibales
	Array_1 = [1, 3, 5, 8]		#I was not sure if TAMId wanted to change the array numbers within the code itself or by using the input function
	Array_2 = [1, 2, 3]
	Number_k = 5
	sortArrays(Array_1,Array_2,Number_k) 

def sortArrays(Array_1, Array_2, k):	#the sortArrays function uses the parameters to combine and sort the two arrays and print the desired amount
	combined_list = Array_1 + Array_2	#combined_list varible combines the two arrays into one
	combined_list.sort()
	sorted_list = []
	for number in range(k):
		sorted_list.append(combined_list[number])
	print(sorted_list)

Main()

	
