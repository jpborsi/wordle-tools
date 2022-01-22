from wordle_tools.loader import get_all_answers, get_all_guesses


def test_answers():
    assert get_all_answers()


def test_guesses():
    assert get_all_guesses()
