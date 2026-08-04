# Palavra
while True:	
	try:
		word = str(input('Enter a word: ')).lower()
		if word == "":
			print('You have enter one word')
		if word.isalpha():
			break
	except ValueError:
		print ("Enter a word")
  
if word == word[::-1]:
	print ('Your Word is one Palindrome!')
else: 
	print('Your word is not a palindrome!')
        