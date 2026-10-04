from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_tells_player_to_go_lower():
    # Regression: the hints used to be reversed
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_tells_player_to_go_higher():
    # Regression: the hints used to be reversed
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_numeric_comparison_not_string_comparison():
    # Regression: the secret used to be passed as a string on even attempts,
    # so values were compared alphabetically ("9" > "50" is True).
    assert check_guess(9, 50)[0] == "Too Low"
    assert check_guess(100, 50)[0] == "Too High"
