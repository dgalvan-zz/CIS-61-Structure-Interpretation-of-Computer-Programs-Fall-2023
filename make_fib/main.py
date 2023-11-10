def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
        # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    def fib():
        nonlocal a, b
        # Calculate the next Fibonacci number
        result = a
        a, b = b, a + b
        return result

    return fib


fib = make_fib()
print(fib())

print(fib())

print(fib())

print(fib())

print(fib())

fib2 = make_fib()
print(fib() + sum([fib2() for _ in range(5)]))