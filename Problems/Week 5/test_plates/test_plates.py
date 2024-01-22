from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("CS200407") == False
    assert is_valid("HELLO") == True
    assert is_valid("D") == False
    assert is_valid("CS50D") == False
    assert is_valid("CS05") == False
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("CS50!")== False