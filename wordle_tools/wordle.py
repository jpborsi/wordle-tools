import argparse
import random

from wordle_tools.filter_words import get_possible_words
from wordle_tools.guess_result import get_result_string, get_result
from wordle_tools.loader import get_all_answers, get_all_guesses


def adversarial_main(hard: bool = False, stats: bool = False) -> None:
    pass  # TODO


def main(
    hard: bool = False,
    adversarial: bool = False,
    answer: str = None,
    stats: bool = False,
) -> None:
    if adversarial:
        adversarial_main(hard=hard, stats=stats)
        return

    if answer is not None:
        target_word = answer
    else:
        target_word = random.choice(get_all_answers())

    conditions = []
    while True:
        guess = input("Enter guess:")
        if hard:
            pass  # TODO
        if guess.upper()[:5] == target_word.upper()[:5]:
            print("Success!")
            break
        result = get_result_string(answer=target_word, guess=guess)
        print(result)
        conditions.extend(get_result(answer=target_word, guess=guess))
        if stats:
            print(
                f"{len(get_possible_words(get_all_guesses(), *conditions))} words remaining"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Wordle")
    parser.add_argument(
        "--hard",
        dest="hard_mode",
        action="store_true",
        default=False,
        help="Turns on hard mode, where you must include any previously revealed letters in each subsequent guess.",
    )
    parser.add_argument(
        "--adversarial",
        dest="adversarial",
        action="store_true",
        default=False,
        help="Turns on adversarial mode, where we can change the chosen word based on your guesses in order to make "
        "the game maximally challenging.",
    )
    parser.add_argument(
        "--stats",
        dest="stats",
        action="store_true",
        default=False,
        help="Provides information about how many words are remaining.",
    )
    parser.add_argument(
        "--answer", dest="answer", help="Sets the answer to the provided string"
    )

    args = parser.parse_args()
    main(
        hard=args.hard_mode,
        adversarial=args.adversarial,
        stats=args.stats,
        answer=args.answer,
    )
