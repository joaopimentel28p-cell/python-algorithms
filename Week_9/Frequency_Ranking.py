while True:
	try:
		how_many = int(input('Enter how many numbers you want to input: '))
		if how_many > 0:
			break
		print("Please enter a positive number greater than 0.")
	except ValueError:
		print("Error: Please enter a valid number.")
		
animals = []

for a in range (how_many):
	try:
		receive = str(input(f'Enter a {a + 1}º animal: '))
		while True:
			if receive.isalpha():
				break
			print('Enter a name of Animal')
			continue
		animals.append(receive)
	except ValueError:
		print('Type a animal')
		continue

frequencias = {}

for receive in animals:
    if receive in frequencias:
        frequencias[receive] += 1
    else:
        frequencias[receive] = 1
        
print(frequencias)
        
    