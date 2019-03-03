import math

from pimontecarlo import calculate_pi


def test_calculate_pi():
    assert math.fabs(calculate_pi(100_000) - math.pi) < 0.01
