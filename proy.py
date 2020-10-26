import functions
from os import system
username = input("Username:")
system("cls")
option = 0
while option != 4:
	print(f'Hello!, {username}.')
	print("Select any of these options (type the number):",'\n',"1. Solution preparation",'\n',"2. Add reagent data",'\n',"3. Search reagent data",'\n',"4. Exit",'\n',"If you don't know if the reagent's data is in the program, search for it")
	option = int(input())
	system("cls")
	if option == 1:
		repeat = 1
		while repeat == 1:
			functions.solution_preparation()
			print("Do you want to prepare another solution? (type the number):",'\n','1. Yes','\n',"2. No")
			repeat = int(input())
			system("cls")

	if option == 2:
		repeat = 1
		while repeat == 1:
			functions.add_reagent_data()
			print("Do you want to add another reagent's data? (type the number):",'\n','1. Yes','\n',"2. No")
			repeat = int(input())
			system("cls")

	if option == 3:
		repeat = 1
		while repeat == 1:
			reagent = input("Name of the reagent:")
			functions.search_for_reagent(reagent)
			print("Do you want to search for another reagent's data? (type the number):",'\n','1. Yes','\n',"2. No")
			repeat = int(input())
			system("cls")
