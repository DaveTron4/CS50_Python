import pytest
from seasons import calculate

def main():
    test()

def test():
    with pytest.raises(SystemExit, match="Invalid"):
        calculate("Januar 6th, 1998")



if __name__ == "__main__":
    main()