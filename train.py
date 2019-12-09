import os
import json
import statistics
import asyncio

from book import Book


author_profile = {
    "mean_word_length": {},
    "mean_sentence_length": {},
}
word_lengths = []
sentence_lengths = []


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
    sentence_lengths.append(stats['mean_sentence_length'])


async def find_mean(lst, prop):
    mean = statistics.mean(lst)
    stdev = statistics.stdev(lst)
    d = {
        "mean": mean,
        "stdev": stdev
    }
    author_profile[prop] = d
    return


async def write_to_file(filename="author.json"):
    await asyncio.wait([
        find_mean(word_lengths, "mean_word_length"),
        find_mean(sentence_lengths, "mean_sentence_length"),
    ])

    with open(filename, 'w+') as out:
        out.write(json.dumps(
            author_profile
        ))


async def main(folder):
    files = get_file_list(folder)
    books = make_books(files)

    await asyncio.wait([
        train(book) for book in books
    ])

    await write_to_file()


def run(folder):
    asyncio.run(main(folder))


if __name__ == "__main__":
    run("books")
