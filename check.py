import json
import statistics

from scipy.stats import norm

from book import Book


"""

author.json should have these properties:
    - mean_word_length

Take a book and compute the properties above.

[]

"""


def run(book_filename, author_filename="author.json", ):

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
