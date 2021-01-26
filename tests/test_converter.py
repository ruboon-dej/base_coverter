from lib.converter import convert

def test_base_two():
    assert convert(2, 10, "101") == "5"
    assert convert(2, 10, "100110") == "38"

def test_base_sixteen():
    assert convert(10, 16, "12") == "C"