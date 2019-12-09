import json
import statistics

from scipy.stats import norm

from book import Book

# Takes the book and saves its information using the serialize()
# function. It then uses z-score statistics to create a distribution
# graph. The equation used for this is z = (x - (mean)) / (stdev), where
# x is the data point for the book, mean is the average data point from
# the json file, and stdev is the standard deviation from the json file.
def run(book_filename, author_filename):
    try:
        with open(author_filename, 'r') as source:
            author_profile = json.loads(source.read())
    except:
        exit()

    b = Book(book_filename)
    b.parse()
    book = b.serialize()

    z_scores = []
    for k in book.keys():
        if k == 'filename':
            continue

        z = (book[k] - author_profile[k]["mean"]) / author_profile[k]["stdev"]
        z_scores.append(abs(z))
    if max(z_scores) > 2.5:
        z_scores.remove(max(z_scores))

    mean = statistics.mean(z_scores)

    # This basically looks at a normal curve
    percentage = 100 * (norm.cdf(mean) - norm.cdf(-mean))

    if percentage < 50:
        print("I am", str(round(100 - percentage, 2))+"%", "sure that this is written by your author")
    else:
        print("I am", str(round(percentage, 2))+"%", "sure that this is NOT written by your author")
