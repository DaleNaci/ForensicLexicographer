import statistics
import string


class Book:
    """A class with numerical data about a book"""

    def __init__(self, filename):
        self.file_name = filename
        self.mean_word_length = 0.0
        self.parse()


    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText = bookText.replace(c, "")
        wordList = bookText.split()

        self.mean_word_length = statistics.mean(map(len, wordList))


    def serialize(self):
        return {
            "filename": self.file_name,
            "median_sentence_length": self.mean_sentence_length,
        }
