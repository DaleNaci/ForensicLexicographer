import os
import statistics 
import asyncio

from Book import Book


profile = {
    "median_sentence_length": 0,
    "median_word_length": 0,
    "median_dialogue_ratio": 0,
}


def get_file_list(root):
    lst = os.listdir(root)
    return [os.path.join(root, f) for f in lst if f.endswith(".txt")]


def make_books(file_list):
    books = []
    for f in file_list:
        books.append(Book(f))
    return books


def train(book):
    stats = book.parse()
    


def main():
    print("hi")
    print(get_file_list("books"))



if __name__ == "__main__":
    main()