"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

text = input("Text: ")
text = text.split(" ")
word_to_count = {}
for word in text:
    word_to_count[word] = word_to_count.get(word, 0) + 1

words_alphabetical = sorted(word_to_count.items())
for word in words_alphabetical:
    print(f"{word[0]} : {word[1]}")
