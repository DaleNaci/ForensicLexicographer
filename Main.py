import sys
import os

def main():

    usage = "usage: python3 Main.py\t[-t <folder>]\n\t\t\t[-c <file>]"

    if len(sys.argv) != 3:
        print()
        print("unknown option: " + " ".join(sys.argv[1:]))
        print(usage)
        print()
        exit()

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
        else:
            print("File does not exist.")

    else:
        print(usage)
        exit()



if __name__ == "__main__":
    main()
