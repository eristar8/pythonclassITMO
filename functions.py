from os import system
molecular_weight = {
	"H":1,
	"Na":22.99,
	"K":39.10,
	"Mg":24.31,
	"Ca":40.08,
	"Cr":52,
	"Mn":54.94,
	"Fe":55.85,
	"Zn":65.38,
	"Al":26.98,
	"C":12.01,
	"N":14.01,
	"O":16,
	"P":30.97,
	"I":126.9,
	"Cl":35.45,
	"S":32.07,
	"F":19
}

def add_reagent_data():
	delimiter = ""; delimiters = [":","-",";",".",","]

	system("cls")
	print("Give the name of the reagent in upper or lowercase first, not its molecular formula, yet...")
	reagent = input("Name of the reagent:")
	print("Examples on how to introduce the molecular formula:",'\n',"C3 H8 02 N2",'\n',"C3;H8;02;N2",'\n',"C3:H8:02:N2")
	print("You can use any of these delimiters:",delimiters,"or just spaces between atoms: C3 H8 02 N2")
	print("Also if you want to add for example: NaCl, you'll have to indicate the number of atoms of each element in the molecular formula")
	print("Like this: Na1Cl1")
	molecular_formula = input("Molecular formula:")

	for i in molecular_formula: #finding delimiter in string between atoms
		if i == " " or i == "," or i == "." or i == "-" or i == ":" or i == ";":
			delimiter = i
			break 
	molecular_formula = molecular_formula.replace(delimiter,"")

	with open("reagents_data.csv","a+") as reagents_data_file:
		reagents_data_file.writelines('\n')
		reagents_data_file.writelines(reagent+","+molecular_formula) #maybe aqui haya problema con la manera en la que intentas escribir las cosas
	print("Data successfully uploaded, press enter to continue")
	input(); system("cls")
	return 

def search_for_reagent(reagent):
	found = False; line1 = ""
	with open("reagents_data.csv","r") as reagents_data_file:
		for line in reagents_data_file:
			line1 = line.split(",")
			for element in line1:
				if element == reagent.capitalize() or element == reagent.lower() or element == reagent.title() or element == reagent: #crea variables para cada una en caso de que no funcione
					system("cls")
					print("Data of the reagent is already in the program")
					found = True
					break
			line1.clear()
		if found == False:
			system("cls")
			print("Data of the reagent",reagent,"isn't available. Please, upload it")
	return

def search_reagent_for_calculations(reagent):
	line1 = ""; save_the_next_element = False; molecular_formula = ""
	with open("reagents_data.csv","r") as reagents_data_file:
		for line in reagents_data_file:
			line1 = line.split(",")
			for element in line1:
				if element == reagent.capitalize() or element == reagent.lower() or element == reagent.title(): #crea variables para cada una en caso de que no funcione
					save_the_next_element = True
					continue
				if save_the_next_element == True:
					molecular_formula = element
					break
			line1.clear()
			if save_the_next_element == True:
				save_the_next_element = False
				break
	return molecular_formula

def convert_str_to_dict(molecular_formula):
	wait = False; value = ""; key = ""; dict_mol_form = {}
	for i in range(len(molecular_formula)): #filling dic_mol_formula with the molecular formula given
		if i < len(molecular_formula) - 1 and molecular_formula[i].isalpha() and molecular_formula[i+1].isalpha():
			wait = True
			key = molecular_formula[i]
		elif i < len(molecular_formula) - 1 and molecular_formula[i].isalpha() and molecular_formula[i+1].isdigit() and wait == False:
			key = molecular_formula[i]
		elif molecular_formula[i].isalpha() and wait == True:
			wait = False
			key = key + molecular_formula[i]
		elif molecular_formula[i].isalpha() and i == len(molecular_formula) - 1:
			key = key + molecular_formula[i]

		if i < len(molecular_formula) - 1 and molecular_formula[i].isdigit() and molecular_formula[i+1].isdigit():
			wait = True
			value = molecular_formula[i]
		elif i < len(molecular_formula) - 1 and molecular_formula[i].isdigit() and molecular_formula[i+1].isalpha() and wait == False:
			value = molecular_formula[i]
		elif molecular_formula[i].isdigit() and wait == True:
			wait = False
			value = value + molecular_formula[i]
		elif molecular_formula[i].isdigit() and i == len(molecular_formula) - 1:
			value = value + molecular_formula[i]
	
		if value!= "" and key != "" and wait == False:
			dict_mol_form[key] = int(value)
			value = str(value)
			value = ""; key = ""
	return dict_mol_form

def solution_preparation():
	mols_sol = 0; lts_solution = 0; molecular_formula = ""; dict_molecular_form = ""; total_mol_weight = 0; mlts_solute = 0; grms_solute = 0
	system("cls")
	print("I'll be working just with molar, p/v and v/v concentrations",'\n')
	print("Select a type of concentration:",'\n',"1. Molar[M]",'\n',"2. p/v",'\n',"3. v/v")
	concentration_type = int(input())

	if concentration_type == 1:
		system("cls"); print("------------MOLAR CONCENTRATION-----------")
		reagent_name = input("Reagent name:")
		ml_solution = float(input("How many mL of solution you need to prepare?:"));
		concentration = float(input("At which concentration will be your solution?:")); print('\n')
		lts_solution = (ml_solution)*(1/1000)

		mols_sol = concentration*lts_solution

		molecular_formula = search_reagent_for_calculations(reagent_name)
		dict_molecular_form = convert_str_to_dict(molecular_formula) #ES UN STRING EN REALIDAD
		print("Diccionario dict_molecular_form",dict_molecular_form) #viene de convert_str_to_dict
		for atom_int, mol_weight_int in dict_molecular_form.items(): #Puede que haya problemas aqui porque estas guardando el dict en una variable string
			for atom, mol_weight in molecular_weight.items():
				if atom_int == atom:
					total_mol_weight = total_mol_weight + (mol_weight_int*mol_weight)
					break

		grms_solute = round(total_mol_weight*mols_sol,3)
		print("In order to prepare this solution, you need to weigh",grms_solute,"grams of",reagent_name,"and disolve it on",ml_solution,"mL of dH2O")

	elif concentration_type == 2:
		system("cls"); print("------------P/V CONCENTRATION-----------")
		reagent_name = input("Reagent name:")
		ml_solution = float(input("How many mL of solution you need to prepare?:"))
		concentration = float(input("In what percentage you need your solution?:"))

		grms_solute = round(((concentration*ml_solution)/100),3)
		print("In order to prepare this solution, you need to weigh",grms_solute,"grams of",reagent_name,"and disolve it on",ml_solution,"mL of dH2O")

	elif concentration_type == 3:
		system("cls"); print("------------V/V CONCENTRATION-----------")
		reagent_name = input("Reagent name:")
		ml_solution = float(input("How many mL of solution you need to prepare?:"))
		concentration = float(input("In what percentage you need your solution?:"))

		mlts_solute = round(((concentration*ml_solution)/100),3)
		print("In order to prepare this solution, you need",mlts_solute,"mL of",reagent_name,"and mix it with",ml_solution,"mL of dH2O")
	return