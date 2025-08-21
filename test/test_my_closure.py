from python.my_closure import create_multiply

def test_double():
    double = create_multiply(2)
    assert double(5) == 10

def test_triple():
    triple = create_multiply(3)
    assert triple(4) == 12

def test_custom_factor():
    multiply_by_7 = create_multiply(7)
    assert multiply_by_7(3) == 21
