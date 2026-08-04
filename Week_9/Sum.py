while True:
    try:
        how_many = int(input('Enter how many numbers you want to input: '))
        if how_many > 0:
            break
        print("Please enter a positive number greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number.")
    
tot = []
total_sum = 0
for t in range (how_many):
    num = int(input(f'Enter a { t + 1}º number: '))
    tot.append(num)
    total_sum += num 

print(f"The sum of all the numbers in the list is {total_sum}.")
