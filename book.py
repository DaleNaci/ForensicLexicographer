import statistics
import string

class Book:
    """A class with numerical data about a book"""

    def __init__(self, filename):
        self.file_name = filename
        self.mean_word_length = 0.0
        self.period_percentage = 0.0
        self.exclamation_percentage = 0.0
        self.question_percentage = 0.0


    def parse(self):
        with open(self.file_name, 'r') as inF:
            bookText = inF.read()

        bookText1 = bookText
        for c in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~”“\"":
            bookText1 = bookText1.replace(c, "")
        wordList = bookText1.split()
        self.mean_word_length = statistics.mean(map(len, wordList))

        prefixes = ["sir", " ms", " mrs", " mr", " st", "ave", " rd"]
        periodCount = 0
        exclamationCount = 0
        questionCount = 0
        for i in range(len(bookText)):
            try:
                if bookText[i] == ".":
                    cond1 = bookText[i-2:i] != ".."
                    cond2 = bookText[i-1] != "." and bookText[i+1] != "."
                    cond3 = bookText[i+1:i+3] != ".."
                    cond4 = bookText[i-3:i].lower() not in prefixes
                    if cond1 and cond2 and cond3 and cond4:
                        periodCount += 1
                if bookText[i] == "!":
                    exclamationCount += 1
                if bookText[i] == "?":
                    questionCount += 1
            except:
                pass

        total = periodCount + exclamationCount + questionCount
        self.period_percentage = (periodCount / total) * 100
        self.exclamation_percentage = (exclamationCount / total) * 100
        self.question_percentage = (questionCount / total) * 100


    def serialize(self):
        return {
            "filename": self.file_name,
            "mean_word_length": self.mean_word_length,
            "period_percentage": self.period_percentage,
            "exclamation_percentage": self.exclamation_percentage,
            "question_percentage": self.question_percentage
        }
