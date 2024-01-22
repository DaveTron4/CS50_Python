from numb3rs import validate

def test_false():
    assert validate(r"255.255.255.275") == False
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.255.275.255") == False
    assert validate(r"255.275.255.255") == False
    assert validate(r"275.255.255.255") == False
    assert validate(r"1.275.275.275") == False
    assert validate(r"2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate(r"64.128.256.512") == False
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False

def test_true():
    assert validate(r"255.255.255.255") == True
    assert validate(r"127.0.0.1") == True
    assert validate(r"140.247.235.144") == True
