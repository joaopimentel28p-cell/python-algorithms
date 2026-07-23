events = []

#User Enter 
try:
	how_many = int(input('Type how many times you want to enter objects: '))
	if how_many <= 0:
		print ('Please, Enter a positive Number')
	else:
		for n in range (how_many):
			receiver = input(f"Enter the {n+1}º object: ").strip()
			events.append ({receiver})
			final = []
			for item in events:
				if item not in final:
					final.append(item)
	print (final)

except ValueError:
	print ('Please, Enter a Positive Number')