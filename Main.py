import sys
import os
import subprocess

# Pip installs scipy if not already on the machine
try:
    import scipy
except:
    print("Scipy not detected on this computer. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])

try:
    import scipy
except:
    print("Installation of scipy failed. Please install manually.")
    exit()

import train
import check

# This runs through different processes, depending on sys.argv[1]. If
# sys.argv[1] is "-t", it will "train" an algorithm (aka create a json
# file). If sys.argv[1] is "-c", it will compare a given .txt file
# against a given .json file, and print out whether the percentage
# chance of the .txt file being written by the author that the .json
# file refers to.
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
            print(folder_name + ".json created")
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

# Prints the correct way to call Main.py
def error_message():
    print()
    print("unknown option: " + " ".join(sys.argv[1:]))
    print("usage: py/python/python3 Main.py\t[-t <folder>]\n\t\t\t[-c <file> <author_file>]")
    print()
    exit()


if __name__ == "__main__":
    main()
