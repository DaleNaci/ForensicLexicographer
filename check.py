import json
import statistics

from book import Book


"""

author.json should have these properties:
    - mean_word_length
    
Take a book and compute the properties above.

The book's properties are compared to the properties in author.json
The distance between each quantity is computed. Then these values are averaged.

The average is reported as the score. Smaller scores mean higher confidence

For ex:

author.json:
    - mean_word_length: 4
    
book:
    - mean_word_length: 3
    

4 - 3 = 1

1 / 1 = 1
score is 1, the book is most probably written by the author

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


    difs = []
    for k in book.keys():
        if k == 'filename':
            continue
        difs.append(abs(book[k] - author_profile[k]))

    mean = statistics.mean(difs)


    print(f"Score: {mean}")
    # print what score means here
