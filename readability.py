from typing import List
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import cmudict

nltk.download("cmudict")
nltk.download("punkt")

phoneme_dict = cmudict.dict()

# Code adapted from https://github.com/ypeels/nltk-book/blob/master/exercises/2.21-syllable-count.py
def syllables_in_word(word):
    """Attempts to count the number of syllables in the string argument 'word'.

    Limitation: word must be in the CMU dictionary
    "Algorithm": no. syllables == no. (0,1,2) digits in the dictionary entry, right??
    """
    word = word.lower()
    if word in phoneme_dict:
        return sum(c.isdigit() for c in "".join(phoneme_dict[word][0]))
    else:
        return 0


def avg_words_per_sentence(sentences: List[List[str]]):
    word_count = 0
    sentence_count = 0
    for sentence in sentences:
        word_count += len(sentence)
        sentence_count += 1

    return word_count / sentence_count


def avg_syllables_per_word(words: List[str]):
    syllable_count = 0
    word_count = 0

    for word in words:
        syllable_count += syllables_in_word(word)
        word_count += 1

    return syllable_count / word_count


def flesch_kincaid_grade_level(file_text: str):
    sentences = sent_tokenize(file_text)
    words = [word for word in word_tokenize(file_text) if word.isalpha()]

    return (
        (len(words) / len(sentences)) * 0.39
        + avg_syllables_per_word(words) * 11.8
        - 15.59
    )
