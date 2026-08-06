while True:
    try:
        how_many = int(input("How many numbers do you want to enter: "))
        if how_many > 0:
            break
        print("Please, enter a positive number.")
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
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

print(numbers)
