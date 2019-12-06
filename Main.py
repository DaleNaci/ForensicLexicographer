import sys

def main():
    file_name = ""
    if len(sys.argv) == 1:
        file_name = input("What is the name of the file? ")
    else:
        file_name = sys.argv[1]


if __name__ == "__main__":
    main()
