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

#Bigger
bigger = numbers[0]
    
if bigger < numbers[1]:
    bigger = numbers [1]

if bigger < numbers [2]:
    bigger = numbers[2]

if bigger < numbers [2]:
    bigger = numbers [2]

if bigger < numbers [3]:
    bigger = numbers [3]

if bigger < numbers [4]:
    bigger = numbers [4]

print (f'The largest number entered is: {bigger}')
