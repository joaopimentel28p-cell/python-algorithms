try:
	while True:
		how_many = int(input('How many times do you want to enter numbers: '))
		if how_many > 0:
			break
		print ('Please, enter a positive number!')
except ValueError:
    print ('You have enter one number!')
    
numbers = []

for n in range (how_many):
	while True:
		try:
			add = int(input(f'Enter a {n+ 1}º number: '))
			numbers.append(add)
			break
		except ValueError:
			print ('Your have type a numbers')
	
n = len(numbers)
for u in range (n):
    for m in range (0, n -1):
        if numbers[m + 1] > numbers[m]:
            numbers[m], numbers[m + 1] = numbers[m + 1], numbers[m]
            
print (numbers)