while True:
    word = input("Enter a word: ").strip().lower()
    if word.isalpha():
        break
    print("Please, enter one word using letters only.")

if word == word[::-1]:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome.")
