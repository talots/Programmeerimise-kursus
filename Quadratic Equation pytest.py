import math

def inc(a, b, c):
    radican = (b ** 2) - (4 * a * c)
    x1 = (-1 * b - math.sqrt(radican)) / (2 * a)
    return x1

def test_answer():
    assert inc(1, 2, 1) == -1.0