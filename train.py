import os
import json
import statistics
import asyncio

from Book import Book


word_lengths = []

author_profile = {
    "median_word_length": 0,
}

def get_file_list(root):
    lst = os.listdir(root)
    return [os.path.join(root, f) for f in lst if f.endswith(".txt")]


def make_books(file_list):
    books = []
    for f in file_list:
        books.append(Book(f))
    return books


async def train(book):
    stats = book.parse()

    word_lengths.append(['median_word_length'])


async def find_median(lst, prop):
    med = statistics.median(lst)
    author_profile[prop] = med
    return


def write_to_file(filename="author.json"):
    with open(filename, 'w+') as out:

        await asyncio.gather([
            find_median(word_lengths, "median_word_length")
        ])

        out.write(json.dumps({
            author_profile
        }))


async def main():
    files = get_file_list("books")
    books = make_books(files)

    await asyncio.gather([
        train(book) for book in books
    ])


if __name__ == "__main__":
    asyncio.run(main())
