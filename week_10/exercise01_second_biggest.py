# Quantas vezes o usuário deseja incluir dados
while True:
	try:
		how_many = int(input('How many times do you want to enter numbers: '))
		if how_many > 0:
			break
	except ValueError:
		print ('Your need enter numbers only.')
		continue

# Lista de Números inseridos (A base pra execução principal)
numbers = []

# Inserir Números
for n in range (how_many):
	try:
		add = int(input(f'Enter a {n+ 1}º number: '))
		numbers.append(add)
	except ValueError:
		print("Your need enter numbers only.")
  
n = len(numbers)
for u in range (n):
    for m in range (0, n -1):
        if numbers[m + 1] > m:
            numbers[m], numbers[m + 1] = numbers[m + 1], numbers[m]
            
second_biggest = numbers[2]
            
print(f"the second biggest number entered is {second_biggest}")