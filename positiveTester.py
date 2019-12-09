import json
import statistics
import os

from scipy.stats import norm

from book import Book

percentageList = []

for f in os.listdir("books"):
    if not f.endswith(".txt"):
        continue

    book_filename = f
    author_filename = "author.json"

    try:
        with open(author_filename, 'r') as source:
            author_profile = json.loads(source.read())
    except:
        exit()

    b = Book("books/" + book_filename)
    b.parse()
    book = b.serialize()

    z_scores = []
    for k in book.keys():
        if k == 'filename':
            continue

        z = (book[k] - author_profile[k]["mean"]) / author_profile[k]["stdev"]
        z_scores.append(abs(z))

    mean = statistics.mean(z_scores)

    # This basically looks at a normal curve
    percentage = 100 * (norm.cdf(mean) - norm.cdf(-mean))
    percentageList.append(100 - percentage)

    if percentage < 50:
        print("I am", str(round(100 - percentage, 2))+"%", "sure that", f, "is written by your author")
    else:
        print("I am", str(round(percentage, 2))+"%", "sure that", f, "is NOT written by your author")

print("Average positive percentages:", str(statistics.mean(percentageList))+"%")
