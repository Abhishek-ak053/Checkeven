from Evenorodd import evenorodd
def test_even():
    assert evenorodd(4) == "Even"

def test_odd():
    assert evenorodd(3) == "Odd"

def test_zero():
 assert evenorodd(0) == "Even"