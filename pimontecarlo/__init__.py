import random


def calculate_pi(n):
    r = 1
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= r * r:
            count += 1
    return 4 * count / n
