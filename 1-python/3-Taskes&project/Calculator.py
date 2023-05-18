print("\t\t\t\t\t\tSimple Calculator")
print("\t\t\t\t\t\t********************")
while True:
	ModeSelect = input("To select Scientific mode press 1, To select Programming mode press 2: ");
	ModeSelect = int(ModeSelect)
	if ModeSelect == 1:
		sum=0
		while True:
			x = input("To do the Scientific operation press 1, to print the result press 2: ")
			x = int(x)
			if x == 1:
				num1 = input("Please enter the First number: ")
				num1 = int(num1)
				num2 = input("Please enter the Second number: ")
				num2 = int(num2)
				ScientificOperations = {
                      "Add": num1+num2,
					  "Sub": num1-num2,
					  "Div": num1/num2,
					  "Mul": num1*num2,
					  "Mod": num1%num2,
					  "Exp": num1**num2,
					}
				SelectOperation = input("Please select Scientific operation: ")
				if SelectOperation == "Add":
					sum = sum+ScientificOperations["Add"]
				elif SelectOperation == "Sub":
					sum = sum+ScientificOperations["Sub"]
				elif SelectOperation == "Div":
					sum = sum+ScientificOperations["Div"]
				elif SelectOperation == "Mul":
					sum = sum+ScientificOperations["Mul"]
				elif ScientificOperations == "Mod":
					sum = sum+ScientificOperations["Mod"]
				elif ScientificOperations == "Exp":
					sum = sum+ScientificOperations["Exp"]
				else:
					print("Error, Try again")
			elif x == 2:
				print("The result = ",sum)
				print("--------------------------------------------"*2)
			else:
				print("Exit")
				print("--------------------------------------------"*2)
				break
	elif ModeSelect == 2:
		while True:
			print("")
			select = input("To Convert Decimal number to Binary, Hex, remain it as decimal, Oct press 1, To Exit press 2: ")
			select = int(select)
			if select == 1:
				y = input("To Print result of Binary press 1, To Print result of Hex press 2, To Print result of Decimal press 3, To Print result of Oct press 4: ")
				y = int(y)
				num = input("Please enter the number in Decimal: ")
				num = int(num)
				if y == 1:
					print("Result Decimal -> Binary = ",bin(num))
					print("--------------------------------------------"*2)
				elif y == 2: 
					print("Result Decimal -> Hexadecimal = ",hex(num))
					print("--------------------------------------------"*2)
				elif y == 3:
					print("Result Decimal -> Decimal = ",num)
					print("--------------------------------------------"*2)
				elif y == 4:
					print("Result Decimal -> Octal = ",oct(num))
					print("--------------------------------------------"*2)
				else:
					print("Exit")
					break
			elif select == 2:
				print("Exit")
				print("--------------------------------------------"*2)
				break
	else:
		print("Incorrect Mode")
		print("--------------------------------------------"*2)