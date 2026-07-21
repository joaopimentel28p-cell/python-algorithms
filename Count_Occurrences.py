while True:
    try:
        how_many = int(input('Enter the number of times you want to add data: '))
        if how_many > 0:
            break
        print('Please enter a number greater than 0.')
    except ValueError:
        print('Error: Enter a valid whole number.')

objects = []

for i in range(how_many):
    ask = input(f'Type object #{i + 1}: ').strip()
    objects.append(ask)

print('\nCollected objects list:', objects)

counts = {}

for item in objects:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print('Final count:', counts)