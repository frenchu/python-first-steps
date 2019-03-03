from fibonacci import fibonacci_iterative
from fibonacci import fibonacci_recursive


def test_fibonacci_iterative():
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(3) == 2
    assert fibonacci_iterative(4) == 3
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(6) == 8
    assert fibonacci_iterative(7) == 13
    assert fibonacci_iterative(8) == 21


def test_fibonacci_recursive():
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8
    assert fibonacci_recursive(7) == 13
    assert fibonacci_recursive(8) == 21
