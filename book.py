import string

class Book:

    def __init__(self, filename):
        self.file_name = filename
        self.median_word_length = 0
        parse()


    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText = bookText.replace(c, "")
        wordList = bookText.split()

        self.median_word_length = sum(map(len, wordList)) / len(wordList)


    def serialize(self):
        return {
            "filename": self.file_name,
            "median_sentence_length": self.median_sentence_length,
            "median_word_length": self.median_word_length,
            "dialogue_ratio": self.dialogue_ratio,
        }
