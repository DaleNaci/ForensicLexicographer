import sys
import os

def main():
    if len(sys.argv) != 3:
        error_message()

    arg1, arg2 = sys.argv[1:]

    if arg1 == "-t":
        if os.path.isdir(arg2):
            # TRAINING DATA
            pass
        else:
            print("Folder does not exist.")

    elif arg1 == "-c":
        if os.path.isfile(arg2):
            # CHECKING DATA
            pass
        elif not arg2.endswith(".txt"):
            print("File must end with '.txt'.")
        else:
            print("File does not exist.")
    else:
        error_message()


def error_message():
    print()
    print("unknown option: " + " ".join(sys.argv[1:]))
    print("usage: python3 Main.py\t[-t <folder>]\n\t\t\t[-c <file>]")
    print()


if __name__ == "__main__":
    main()
