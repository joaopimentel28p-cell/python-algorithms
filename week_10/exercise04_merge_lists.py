while True:
	try:
		how_many = int(input('How many times do you want to enter objects: '))
		if how_many > 0:
			break 
		print ('You need enter a positive number!')
	except ValueError:
		print ("You need enter one número!")
  
objct = []

for o in range (how_many):
	while True:
		obj = input("Enter one object (letters only): ").strip()
		if not obj:
			print("You need to enter something!")
			continue

		if obj.isnumeric():
			print("You need to enter only strings (no numbers).")
			continue

		if not obj.isalpha():
			print("You need to enter only alphabetic characters (A-Z).")
			continue

		objct.append(obj)
		break

print (f'The first list is: {objct}')
print ('----------------------------------------')

numbers = []

for n in range (how_many):
	while True:
		number = input("Enter one number (numbers only): ").strip()
		if not number:
			print("You need to enter something!")
			continue

		if not number.isnumeric():
			print("You need to enter only numbers (no strings).")
			continue

		numbers.append(int(number))
		break

print (f'The second list is: {numbers}')
print ('----------------------------------------')

new_list = [*objct, *numbers]

print (f"The concatenation of the lists results in: {new_list}")
