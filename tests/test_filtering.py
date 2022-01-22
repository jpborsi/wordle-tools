from wordle_tools.filter_words import (
    get_possible_words,
    LetterNotPresent,
    LetterInPosition,
    LetterNotInPosition,
)


def test_simple_word_list():
    words = ["XXXXX", "YYYYY", "ABCDE"]
    assert get_possible_words(words, LetterNotPresent("X")) == ["YYYYY", "ABCDE"]
    assert get_possible_words(words, LetterInPosition("A", 1)) == ["ABCDE"]
    assert get_possible_words(words, LetterNotInPosition("A", 1)) == []
    assert get_possible_words(words, LetterNotPresent("X"), LetterNotPresent("Y")) == [
        "ABCDE"
    ]
