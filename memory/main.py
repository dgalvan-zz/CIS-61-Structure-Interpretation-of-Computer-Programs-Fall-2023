def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def inner(update_fn):
        nonlocal n  # Use nonlocal to modify the outer variable n
        n = update_fn(n)
        return n

    return inner


f = memory(10)
print(f(lambda x: x * 2))
print (f(lambda x: x - 7))
print (f(lambda x: x > 5))