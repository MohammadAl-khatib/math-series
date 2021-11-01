from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_fibonacci_0() :
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fibonacci_1() :
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fibonacci_5() :
    expected = 5
    actual = fibonacci(5)
    assert expected == actual

def test_fibonacci_6() :
    expected = 8
    actual = fibonacci(6)
    assert expected == actual
    
def test_lucas_7() :
    expected = 29
    actual = lucas(7)
    assert expected == actual

def test_lucas_1() :
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_sum_series_0():
    expected = 0
    actual = sum_series(0)
    assert expected == actual

def test_sum_series_1():
    expected = 1
    actual = sum_series(1)
    assert expected == actual

def test_sum_series_6():
    expected = 8
    actual = sum_series(6)
    assert expected == actual

def test_sum_series_0_2_1():
    expected = 2
    actual = sum_series(0,2,1)
    assert expected == actual

def test_sum_series_1_2_1():
    expected = 1
    actual = sum_series(1,2,1)
    assert expected == actual

def test_sum_series_0_2_5():
    expected = 2
    actual = sum_series(0,2,5)
    assert expected == actual

def test_sum_series_1_2_5():
    expected = 5
    actual = sum_series(1,2,5)
    assert expected == actual

def test_sum_series_4_2_5():
    expected = 19
    actual = sum_series(4,2,5)
    assert expected == actual