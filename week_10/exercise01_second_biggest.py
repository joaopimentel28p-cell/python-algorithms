while True:
    try:
        how_many = int(input("How many numbers do you want to enter (at least 2): "))
        if how_many >= 2:
            break
        print("Please, enter at least two numbers.")
    except ValueError:
        print("You need to enter a whole number.")

numbers = []
for index in range(how_many):
    while True:
        try:
            numbers.append(int(input(f"Enter the {index + 1}º number: ")))
            break
        except ValueError:
            print("You need to enter numbers only.")

for _ in range(len(numbers)):
    for index in range(len(numbers) - 1):
        if numbers[index] < numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

second_biggest = numbers[1]
print(f"The second biggest number entered is {second_biggest}.")
