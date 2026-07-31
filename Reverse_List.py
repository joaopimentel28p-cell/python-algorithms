original_list = []

try:
    how_many = int(input('Type how many times you want to enter numbers: '))
    if how_many <= 0:
        print("Enter a Positive Number")
    else: 
        for count in range (how_many):
            number = int(input(f'Enter a {count+1}º number: '))
            original_list.append ({number})
        for n in range(len(original_list)-1, -1, -1):
            print(f"Índice {n} -> Valor {original_list[n]}")
except ValueError:
    print ('Enter a Positive Number or option')
    
            