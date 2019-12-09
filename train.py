import os
import json
import statistics
import asyncio

from scipy import stats

from book import Book


author_profile = {
    "mean_word_length": {},
    "mean_sentence_length": {},
    "the_percentage": {},
    "and_percentage": {},
    "her_percentage": {},
    "his_percentage": {},
    "great_percentage": {},
    "to_percentage": {},
    "not_percentage": {},
    "word_diversity": {}
}
word_lengths = []
sentence_lengths = []
the_percentages = []
and_percentages = []
her_percentages = []
his_percentages = []
great_percentages = []
to_percentages = []
not_percentages = []
# be_percentages = []
word_diversities = []


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
    the_percentages.append(stats['the_percentage'])
    and_percentages.append(stats['and_percentage'])
    her_percentages.append(stats['her_percentage'])
    his_percentages.append(stats['his_percentage'])
    great_percentages.append(stats['great_percentage'])
    to_percentages.append(stats['to_percentage'])
    not_percentages.append(stats['not_percentage'])
    word_diversities.append(stats['word_diversity'])


async def find_mean(lst, prop):
    mean = statistics.mean(lst)
    stdev = statistics.stdev(lst)
    d = {
        "mean": mean,
        "stdev": stdev
    }
    author_profile[prop] = d
    return


async def write_to_file(folder):
    filename = folder + ".json"
    await asyncio.wait([
        find_mean(word_lengths, "mean_word_length"),
        find_mean(sentence_lengths, "mean_sentence_length"),
        find_mean(the_percentages, "the_percentage"),
        find_mean(and_percentages, "and_percentage"),
        find_mean(her_percentages, "her_percentage"),
        find_mean(his_percentages, "his_percentage"),
        find_mean(great_percentages, "great_percentage"),
        find_mean(to_percentages, "to_percentage"),
        find_mean(not_percentages, "not_percentage"),
        find_mean(word_diversities, "word_diversity")
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

    await write_to_file(folder)


def run(folder):
    asyncio.run(main(folder))


if __name__ == "__main__":
    run("books")
