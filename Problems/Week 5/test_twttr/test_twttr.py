from twttr import shorten
import pytest

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Twitter1") == "Twttr1"
    assert shorten("Twitter!") == "Twttr!"
