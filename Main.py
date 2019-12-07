import sys
import os

import train
import check


def main():

    if len(sys.argv) < 3:
        error_message()

    mode = sys.argv[1]

    if mode == '-t':
        if len(sys.argv) != 3:
            error_message()

        folder_name = sys.argv[2]

        if os.path.isdir(folder_name):
            train.run(folder_name)
            print("author.json created")
        else:
            print("Folder does not exist.")

    elif mode == '-c':
        if len(sys.argv) != 4:
            error_message()

        book_filename = sys.argv[2]
        author_profile_filename = sys.argv[3]

        if not book_filename.endswith(".txt"):
            print("book must be .txt file")
            exit()

        if not author_profile_filename.endswith(".json"):
            print("author profile must be .json file")
            exit()

        check.run(book_filename, author_profile_filename)

    else:
        error_message()


def error_message():
    print()
    print("unknown option: " + " ".join(sys.argv[1:]))
    print("usage: python3 Main.py\t[-t <folder>]\n\t\t\t[-c <file> <author_file>]")
    print()
    exit()


if __name__ == "__main__":
    main()
