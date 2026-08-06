while True:
    try:
        how_many = int(input("How many items do you want in each list: "))
        if how_many > 0:
            break
        print("Please, enter a positive number.")
    except ValueError:
        print("You need to enter a whole number.")

words = []
for index in range(how_many):
    while True:
        word = input("Enter one word (letters only): ").strip()
        if word.isalpha():
            words.append(word)
            break
        print("Please, enter one word using letters only.")

numbers = []
for index in range(how_many):
    while True:
        try:
            numbers.append(int(input("Enter one number: ")))
            break
        except ValueError:
            print("Please, enter a whole number.")

new_list = [*words, *numbers]
print(f"The first list is: {words}")
print(f"The second list is: {numbers}")
print(f"The concatenation of the lists results in: {new_list}")
