def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers

    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7)
    13

    """

    prev1 = 0
    prev2 = 1
    i = 2
    while i <= n:
        current = prev1 + prev2
        prev1, prev2 = prev2, current
        i += 1
    return prev2


if __name__ == '__main__':
    print(fibonacciN(5))
    print(fibonacciN(7))
