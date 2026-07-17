object = []
# loop
try:
	how_many = str(input('Enter a many Enter the number of times you want to add data: '))
except ValueError:
    print('Enter a correct number of times in numbers')
for count in range (how_many):
    ask = int(input('Type a object'))
    object = 