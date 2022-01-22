from typing import List

import pkg_resources


def get_all_answers() -> List[str]:
    with open(
        pkg_resources.resource_filename("wordle_tools", "data/answers.txt"), "r"
    ) as word_list:
        return word_list.readlines()


def get_all_guesses() -> List[str]:
    with open(
        pkg_resources.resource_filename("wordle_tools", "data/answers.txt"), "r"
    ) as word_list:
        answers = word_list.readlines()

    with open(
        pkg_resources.resource_filename("wordle_tools", "data/guesses.txt"), "r"
    ) as word_list:
        guesses = word_list.readlines()

    guesses.extend(answers)
    return guesses
