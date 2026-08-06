while True:
    sentence = input("Enter a sentence: ").strip()
    if sentence:
        break
    print("You need to enter something.")

while True:
    word = input("What word do you want to find: ").strip()
    if word.isalpha():
        break
    print("Please, enter one word using letters only.")

words = sentence.split()
indices = []
for index, current_word in enumerate(words):
    normalized_word = current_word.strip(".,!?;:").lower()
    if normalized_word == word.lower():
        indices.append(index)

if indices:
    print(f"The word '{word}' appears at positions: {indices}.")
else:
    print(f"The word '{word}' was not found in the sentence.")

unique_words = []
for current_word in words:
    normalized_word = current_word.strip(".,!?;:").lower()
    if normalized_word not in unique_words:
        unique_words.append(normalized_word)

print(f"Unique words: {unique_words}")
