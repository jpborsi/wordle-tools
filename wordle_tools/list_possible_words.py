from abc import ABC, abstractmethod
from typing import List


class Condition(ABC):
    """Base class for logic to check if a word meets a given criteria"""

    @abstractmethod
    def applies(self, word: str) -> bool:
        """Returns true if a word has the specified criteria, false otherwise"""
        raise NotImplementedError


class LetterNotPresent(Condition):
    def __init__(self, letter: str):
        assert len(letter) == 1
        self.letter = letter.upper()

    def applies(self, word: str) -> bool:
        return not self.letter in word.upper()


class LetterInPosition(Condition):
    def __init__(self, letter: str, pos: int):  # pos is 1-indexed
        assert len(letter) == 1
        assert 1 <= pos <= 5
        self.letter = letter.upper()
        self.pos = pos

    def applies(self, word: str) -> bool:
        return word.upper()[self.pos - 1] == self.letter


class LetterNotInPosition(Condition):
    def __init__(self, letter: str, pos: int):  # pos is 1-indexed
        assert len(letter) == 1
        assert 1 <= pos <= 5
        self.letter = letter.upper()
        self.pos = pos

    def applies(self, word: str) -> bool:
        return self.letter in word.upper() and word.upper()[self.pos - 1] != self.letter


def get_possible_words(words: List[str], conditions: List[Condition]) -> List[str]:
    return [w for w in words if all([c.applies(w) for c in conditions])]
