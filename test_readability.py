from readability import (
    avg_syllables_per_word,
    flesch_kincaid_grade_level,
    syllables_in_word,
    avg_words_per_sentence,
)
from pytest import approx


def test_syllable_count():
    words = [
        "karate",
        "sausage",
        "hi",
        "rolf",
        "jose",
        "python",
        "education",
        "programming",
        "algorithm",
    ]
    expected_syllables = [3, 2, 1, 1, 2, 2, 4, 3, 4]

    for i, word in enumerate(words):
        syllables = syllables_in_word(word)
        assert syllables == expected_syllables[i]


def test_words_per_sentence():
    sentences = [
        ["The", "fox", "jumped", "over", "the", "lazy", "dog"],
        ["Hello", "world"],
        ["This", "is", "a", "test"],
    ]
    expected = 4.333
    assert avg_words_per_sentence(sentences) == approx(expected, rel=1e-3)


def test_syllables_per_word():
    words = ["fox", "algorithm", "element", "rolf", "programming"]
    expected_average = 2.4
    assert avg_syllables_per_word(words) == expected_average


def test_flesch_kincaid():
    text = """A REST API is an application that accepts data from clients and returns data back. For example, a REST API could accept text data from the client, such as a username and password, and return whether that is a valid user in the database."""
    expected_grade = 9.3
    assert flesch_kincaid_grade_level(text) == approx(expected_grade, 0.1)
