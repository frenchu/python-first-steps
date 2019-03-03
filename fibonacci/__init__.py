def fibonacci_iterative(n):
    a = 1
    b = 1
    for i in range(3, n + 1):
        a = a + b
        b = a - b
    return a


def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
