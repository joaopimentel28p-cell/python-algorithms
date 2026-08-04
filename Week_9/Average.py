while True:
    try:
        how_many = int(input('Enter how many numbers you want to input: '))
        if how_many > 0:
            break
        print("Please enter a positive number greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number.")

total = []       
total_sum = 0   

for a in range(how_many):
    try:
        num = int(input(f"Digite o {a + 1}º número: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        exit()
    
    total.append(num)
    total_sum += num


average = total_sum / how_many


print(f"A média dos números digitados é {average:.2f}")