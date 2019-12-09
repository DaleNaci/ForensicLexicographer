import os

from book import Book

COUNT_LIMIT = 4000

# TWAIN BOOKS
d = {}

wordCount1 = 0
for f in os.listdir("austen"):
    if not f.endswith(".txt"):
        continue

    with open("austen/" + f, "r") as inF:
        text = inF.read()

    for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
        text = text.replace(c, " ")

    wordList = text.split()

    for word in wordList:
        wordCount1 += 1
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

final1 = d.copy()
for key in d:
    if final1[key] < COUNT_LIMIT:
        del final1[key]

# NON TWAIN BOOKS
d2 = {}

wordCount2 = 0
for f in os.listdir("books/not_twain_books"):
    if not f.endswith(".txt") or f=="prideandprejudice.txt" or f=="senseandsensibility.txt":
        continue

    with open("books/not_twain_books/" + f, "r") as inF:
        text = inF.read()

    for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
        text = text.replace(c, " ")

    wordList = text.split()

    for word in wordList:
        wordCount2 += 1
        if word in d2:
            d2[word] += 1
        else:
            d2[word] = 1


final2 = d2.copy()
for key in d2:
    if final2[key] < COUNT_LIMIT:
        del final2[key]

sorted1 = {k: v for k, v in sorted(final1.items(), key=lambda item: item[1])}
sorted2 = {k: v for k, v in sorted(final2.items(), key=lambda item: item[1])}

for k, v in sorted1.items():
    print(k, ":", v)
print()
print("TOTAL:", sum(final1.values()))
print("---------------")
for k, v in sorted2.items():
    print(k, ":", v)
print()
print("TOTAL:", sum(final2.values()))
