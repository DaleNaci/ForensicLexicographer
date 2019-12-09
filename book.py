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
        self.and_percentage = 0.0
        self.her_percentage = 0.0
        self.his_percentage = 0.0
        self.great_percentage = 0.0
        self.word_diversity = 0.0

    def wordCount(self, word, text):
        count = 0
        indices = [m.start() for m in re.finditer(word, text)]
        for i in indices:
            cond1 = i > 0
            cond2 = i < len(text) - len(word)
            cond3 = text[i - 1] not in string.ascii_letters
            cond4 = text[i + len(word)] not in string.ascii_letters
            if cond1 and cond2 and cond3 and cond4:
                count += 1

        return count


    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        bookText1 = bookText
        for c in "!#$%&()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText1 = bookText1.replace(c, " ")
        bookText1 = bookText1.replace("'", "")

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

        lowered = bookText1.lower()
        self.the_percentage = self.wordCount("the", lowered) / len(wordList1)
        self.and_percentage = self.wordCount("and", lowered) / len(wordList1)
        self.her_percentage = self.wordCount("her", lowered) / len(wordList1)
        self.his_percentage = self.wordCount("his", lowered) / len(wordList1)
        self.great_percentage = self.wordCount("great", lowered) / len(wordList1)

        self.word_diversity = len(set(wordList1)) / len(wordList1)


    def serialize(self):
        return {
            "filename": self.file_name,
            "mean_word_length": self.mean_word_length,
            "mean_sentence_length": self.mean_sentence_length,
            "the_percentage": self.the_percentage,
            "and_percentage": self.and_percentage,
            "her_percentage": self.her_percentage,
            "his_percentage": self.his_percentage,
            "great_percentage": self.great_percentage,
            "word_diversity": self.word_diversity,
        }
