from Evenorodd import evenorodd
def test_even():
    assert evenorodd(4) == True

def test_odd():
    assert evenorodd(3) == False

def test_zero():
 assert evenorodd(0) == True