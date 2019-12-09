import os

from book import Book

d = {}

for f in os.listdir("books"):
    if not f.endswith(".txt"):
        continue

    with open("books/" + f, "r") as inF:
        text = inF.read()

    for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
        text = text.replace(c, " ")

    wordList = text.split()

    for word in wordList:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})
