from typing import List

from wordle_tools.filter_words import (
    Condition,
    LetterInPosition,
    LetterNotInPosition,
    LetterNotPresent,
)


def get_result(answer: str, guess: str) -> List[Condition]:
    result = []
    for pos in range(5):
        if answer[pos] == guess[pos]:
            result += [LetterInPosition(answer[pos], pos + 1)]
        elif guess[pos] in answer:
            result += [LetterNotInPosition(guess[pos], pos + 1)]
        elif guess[pos] not in guess[:pos]:
            result += [LetterNotPresent(guess[pos])]
    return result


def get_result_string(answer: str, guess: str) -> str:
    result = ""
    for pos in range(5):
        if answer.upper()[pos] == guess.upper()[pos]:
            result += answer[pos]
        elif guess.upper()[pos] in answer.upper():
            result += "?"
        else:
            result += "_"
    return result.upper()
