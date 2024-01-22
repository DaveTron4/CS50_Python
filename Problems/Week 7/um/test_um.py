from um import count
import pytest


def test_with_spaces():
    assert count("Hello, um , world") == 1

def test_case_insensitive():
    assert count("Um, hello, um, world.") == 2

def test_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
