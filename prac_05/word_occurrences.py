"""
Word Occurrences
Estimate: 30 minutes
Actual: 38 minutes
"""

text = input("Text: ")
text = text.split(" ")
word_to_count = {}
for word in text:
    word_to_count[word] = word_to_count.get(word, 0) + 1

words_alphabetical = sorted(word_to_count.items())
width = 0
for word in words_alphabetical:
    if len(word[0]) > width:
        width = len(word[0])
for word in words_alphabetical:
    print(f"{word[0]:{width}} : {word[1]}")
