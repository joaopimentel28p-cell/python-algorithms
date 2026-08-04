while True:
	try:
		how_many = int(input('Enter how many numbers you want to input:'))
		if how_many <= 0:
			print('Your NEED enter a positive Number')
		if how_many > 0:
			break
		print("Please enter a positive number greater than 0.")
	except ValueError:
		print("Error: Please enter a valid number.")

pair = []

for p in range (how_many):
	add = int(input(f"Enter a {p + 1}º number: "))
	if add %2 == 0:
		pair.append(add)
	print("This number isn't pair")
 
	try:
		user_exit = int(input("\nDo you want to exit? (Press 0 to exit, or 1 to continue searching): "))
		if user_exit == 0:
			print("Exiting program... Goodbye!")
			break  
	except ValueError:
		print("Continuing search mode...")
	
		 
        