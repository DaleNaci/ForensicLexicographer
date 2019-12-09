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
word_diversities = []


# Returns a list containing all files in the "root" directory that end
# with .txt.
def get_file_list(root):
    lst = os.listdir(root)
    return [os.path.join(root, f) for f in lst if f.endswith(".txt")]


# Returns a list containing "Book" objects created from a "file_list",
# a list of files that all consist have the .txt ending.
def make_books(file_list):
    books = []
    for f in file_list:
        books.append(Book(f))
    return books


# Takes a given book and obtains all of the data. It then sorts the data
# into its respective lists.
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


# This finds the mean and standard deviation of the given list and adds
# a dictionary containing both of them to the author_profile dictionary
# using the "prop" key.
async def find_mean(lst, prop):
    mean = statistics.mean(lst)
    stdev = statistics.stdev(lst)
    d = {
        "mean": mean,
        "stdev": stdev
    }
    author_profile[prop] = d
    return


# Writes to a json file with the name the same as the folder. It then
# calls the find_mean() function for all pieces of data to fill
# author_profile, and then creates and writes it to "folder".json.
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


# This is the main function that connects each process of training our
# algorithm.
async def main(folder):
    files = get_file_list(folder)
    books = make_books(files)

    await asyncio.wait([
        train(book) for book in books
    ])

    await write_to_file(folder)

# This is the function that gets called by Main.py.
def run(folder):
    asyncio.run(main(folder))
