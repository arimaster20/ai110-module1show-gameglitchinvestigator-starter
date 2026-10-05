from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_says_go_lower():
    # Regression: hints used to be swapped
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_hint_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_numeric_comparison_not_string():
    # Regression: the secret was cast to str on even attempts, so "9" > "50"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"


def test_parse_guess_valid_and_invalid():
    assert parse_guess(" 42 ") == (True, 42, None)
    assert parse_guess("")[0] is False
    assert parse_guess(None)[0] is False
    assert parse_guess("abc")[0] is False
    assert parse_guess("inf")[0] is False


def test_wrong_guess_always_costs_points():
    # Regression: Too High on an even attempt used to add 5
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too High", 3) == -5
    assert update_score(0, "Too Low", 2) == -5


def test_win_score_and_floor():
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Win", 20) == 10


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    low, high = get_range_for_difficulty("Hard")
    assert high > get_range_for_difficulty("Normal")[1]
