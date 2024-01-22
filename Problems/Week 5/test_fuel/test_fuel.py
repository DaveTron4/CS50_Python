from fuel import convert, gauge
import pytest

def test_fuel():
    assert convert("1/4") == 25
    assert gauge(25) == "25%"
    assert convert("4/4") == 100
    assert gauge(99) == "F"
    assert convert("0/4") == 0
    assert gauge(1) == "E"
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("H/D")