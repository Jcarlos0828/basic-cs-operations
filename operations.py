def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def factorial_recursive(n):
    if n > 0:
        return fibonacci_recursive(n - 1) * n
    return 1


print("fibonacci of 10:", fibonacci_recursive(10))
