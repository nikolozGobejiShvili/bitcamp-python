from twttr import shorten

def test_vowels():
    assert shorten("A") == ""
    assert shorten("E") == ""
    assert shorten("I") == ""
    assert shorten("O") == ""
    assert shorten("U") == ""

def empty():
    assert shorten("") == ""

def number():
    assert shorten("1234567890") == ""


