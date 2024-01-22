from bank import value

def test_bank():
    assert value("Hey") == 20
    assert value("Hello, world!") == 0