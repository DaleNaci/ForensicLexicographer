import statistics
import string


def does_end_at_period(line_list):
    word = line_list[-1].lower()
    return word not in ["sir.", "ms.", "mrs.", "mr.", "st."]

def is_chapter_heading(line):
    if "CHAPTER" in line.upper() and len(line.split()) <= 2:
        return True
    return line.replace(" ", "").isdigit()


class Book:

    def __init__(self, filename):
        self.file_name = filename
        self.median_sentence_length = 0
        self.median_word_length = 0
        self.dialogue_ratio = 0


    def parse(self):
        sentence_lengths = []
        word_lengths = []
        word_count = 0
        quote_word_count = 0

        with open(self.file_name, 'r') as book:
            # panic()
            pass


        self.median_sentence_length = statistics.median(sentence_lengths)
        self.median_word_length = statistics.median(word_lengths)
        self.dialogue_ratio = quote_word_count / word_count


    def serialize(self):
        return {
            "filename": self.file_name,
            "median_sentence_length": self.median_sentence_length,
            "median_word_length": self.median_word_length,
            "dialogue_ratio": self.dialogue_ratio,
        }
