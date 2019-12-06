import os
import json
import statistics
import asyncio

from book import Book


author_profile = {
    "mean_word_length": 0,
}
word_lengths = []


def get_file_list(root):
    lst = os.listdir(root)
    return [os.path.join(root, f) for f in lst if f.endswith(".txt")]


def make_books(file_list):
    books = []
    for f in file_list:
        books.append(Book(f))
    return books


async def train(book):
    book.parse()
    stats = book.serialize()
    word_lengths.append(stats['mean_word_length'])


async def find_mean(lst, prop):
    med = statistics.mean(lst)
    author_profile[prop] = med
    return


async def write_to_file(filename="author.json"):
    await asyncio.wait([
            find_mean(word_lengths, "mean_word_length")
        ])

    with open(filename, 'w+') as out:
        out.write(json.dumps(
            author_profile
        ))


async def main():
    files = get_file_list("books")
    books = make_books(files)

    await asyncio.wait([
        train(book) for book in books
    ])

    await write_to_file()


if __name__ == "__main__":
    asyncio.run(main())
