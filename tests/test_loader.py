from wordle_tools.loader import get_all_answers, get_all_guesses


def test_answers():
    assert len(get_all_answers()) > 2000


def test_guesses():
    assert get_all_guesses()
