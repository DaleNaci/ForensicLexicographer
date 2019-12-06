import statistics
import pprint
import string


pp = pprint.PrettyPrinter(indent=4)

def does_end_at_period(line_list):
    word = line_list[-1].lower()
    return word not in ["sir.", "ms.", "mrs.", "mr.", "st."]

def is_chapter_heading(line):
    if "CHAPTER" in line.upper() and len(line.split()) <= 2: 
        return True
    return line.replace(" ", "").isdigit()


class Book:

    def __init__(self, filename):
        self.filename = filename
        self.sentence_lengths = []
        self.word_lengths = []
        self.dialogue_words_count = 0

    
    def parse(self):
        with open(self.filename, 'r') as book:
            # panic()
            pass
                


    def serialize(self):
        word_count = len(self.word_lengths)
        return {
            "filename": self.filename,
            "median_sentence_length": statistics.median(self.sentence_lengths),
            "median_word_length": statistics.median(self.word_lengths),
            "dialogue_ratio": self.dialogue_words_count / word_count,
        }

    def print(self):
        pp.pprint(self.serialize())
