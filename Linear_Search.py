while True:
    try:
        how_many = int(input("Enter how many school supplies you have already bought: "))
        if how_many > 0:
            break
        print("Please enter a positive number greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number.")

objects = []

for s in range(how_many):
    add = input(f"Type {s + 1}º school object: ").strip()
    objects.append(add)

print("\n--- Lista de Materiais Cadastrados ---")
print(objects)

while True:
    print("\n-------------------------------------------")
    search = input("Type the school supply you want to check: ").strip()
    
    # Busca direta na lista de objetos
    if search in objects:
        print(f"-> You've already bought '{search}'!")
    else:
        print(f"-> You still haven't bought '{search}'!")

    try:
        user_exit = int(input("\nDo you want to exit? (Press 0 to exit, or 1 to continue searching): "))
        if user_exit == 0:
            print("Exiting program... Goodbye!")
            break  # Encerra o loop com segurança
    except ValueError:
        print("Continuing search mode...")