import statistics
import string
import re

class Book:
    """A class with numerical data about a book"""

    def __init__(self, filename):
        self.file_name = filename
        self.mean_word_length = 0.0
        self.mean_sentence_length = 0.0
        self.the_percentage = 0.0



    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        bookText1 = bookText
        for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText1 = bookText1.replace(c, "")
        wordList1 = bookText1.split()
        self.mean_word_length = statistics.mean(map(len, wordList1))


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

        sentenceList1 = bookText2.split(".")
        wordList2 = [s.split() for s in sentenceList1]
        self.mean_sentence_length = statistics.mean(map(len, wordList2))




        theCount = 0
        indices = [m.start() for m in re.finditer("the", bookText1.lower())]
        for i in indices:
            cond1 = i > 0
            cond2 = i < len(bookText1) - 1
            cond3 = not bookText1[i - 1] in string.ascii_letters
            if cond1 and cond2 and cond3:
                theCount += 1

        self.the_percentage = theCount / len(wordList1)


    def serialize(self):
        return {
            "filename": self.file_name,
            "mean_word_length": self.mean_word_length,
            "mean_sentence_length": self.mean_sentence_length,
            "the_percentage": self.the_percentage
        }
