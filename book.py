import statistics
import string

class Book:
    """A class with numerical data about a book"""

    def __init__(self, filename):
        self.file_name = filename
        self.mean_word_length = 0.0
        self.mean_sentence_length = 0.0
        


    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        bookText1 = bookText
        for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText1 = bookText1.replace(c, "")
        wordList = bookText1.split()
        self.mean_word_length = statistics.mean(map(len, wordList))


        bookText2 = bookText
        try:
            for i in range(len(bookText2)):
                if bookText2 == ".":
                    cond1 = bookText[i-2:i] != ".."
                    cond2 = bookText[i-1] != "." and bookText[i+1] != "."
                    cond3 = bookText[i+1:i+3] != ".."
                    cond4 = bookText[i-3:i].lower() not in prefixes
                    if not(cond1 and cond2 and cond3 and cond4):
                        bookText2 = bookText[:i] + bookText[i+1:]
                        i -= 1
        except:
            pass

        wordList = bookText2.split(".")
        self.mean_sentence_length = statistics.mean(map(len, wordList))


    def serialize(self):
        return {
            "filename": self.file_name,
            "mean_word_length": self.mean_word_length,
            "mean_sentence_length": self.mean_sentence_length,
        }
