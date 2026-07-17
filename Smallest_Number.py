#numbers
numbers = []
for capt in range(5):
    try:
        capt = int(input('Enter a number: '))
        numbers.append(capt)
    except ValueError:
        print ('--------------------')
        print('enter whole numbers')
        print ('--------------------')

#Smallest
smallest = numbers[0]

if smallest > numbers[1]:
	smallest = numbers [1]

if smallest > numbers [2]:
    smallest = numbers[2]

if smallest > numbers [2]:
    smallest = numbers [2]

if smallest > numbers [3]:
    smallest = numbers [3]

if smallest > numbers [4]:
    smallest = numbers [4]

print (f'The largest number entered is: {smallest}')
