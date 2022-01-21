from wordle_tools.list_possible_words import (
    LetterNotPresent,
    LetterInPosition,
    LetterNotInPosition,
)


def test_no_letter():
    assert LetterNotPresent("a").applies("STERN")
    assert LetterNotPresent("A").applies("STERN")
    assert LetterNotPresent("a").applies("stern")
    assert LetterNotPresent("A").applies("stern")

    assert not LetterNotPresent("b").applies("BRIDE")
    assert not LetterNotPresent("B").applies("BRIDE")
    assert not LetterNotPresent("b").applies("bride")
    assert not LetterNotPresent("B").applies("bride")


def test_letter_in_pos():
    assert LetterInPosition("a", 1).applies("APPLE")
    assert LetterInPosition("A", 1).applies("APPLE")
    assert LetterInPosition("a", 1).applies("apple")
    assert LetterInPosition("A", 1).applies("apple")

    assert not LetterInPosition("b", 1).applies("CRABS")
    assert not LetterInPosition("B", 1).applies("CRABS")
    assert not LetterInPosition("b", 1).applies("crabs")
    assert not LetterInPosition("B", 1).applies("crabs")


def test_letter_not_in_pos():
    assert LetterNotInPosition("a", 1).applies("TABLE")
    assert LetterNotInPosition("A", 1).applies("TABLE")
    assert LetterNotInPosition("a", 1).applies("table")
    assert LetterNotInPosition("A", 1).applies("table")

    assert not LetterNotInPosition("b", 1).applies("BRIDE")
    assert not LetterNotInPosition("B", 1).applies("BRIDE")
    assert not LetterNotInPosition("b", 1).applies("bride")
    assert not LetterNotInPosition("B", 1).applies("bride")

    assert not LetterNotInPosition("b", 1).applies("TRADE")
    assert not LetterNotInPosition("B", 1).applies("TRADE")
    assert not LetterNotInPosition("b", 1).applies("trade")
    assert not LetterNotInPosition("B", 1).applies("trade")
