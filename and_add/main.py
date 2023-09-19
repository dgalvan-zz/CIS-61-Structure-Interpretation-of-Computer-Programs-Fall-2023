def and_add(f, n):
    """
    Return a new function. This new function takes an argument x
    and returns f(x) + n.

    :param f: A one-argument function.
    :param n: A number to be added to the result of f(x).

    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4)  # 4 * 4 + 3
    19
    """
    def new_function(x):
        return f(x) + n

    return new_function

# Test the function with the provided example
def square(x):
    return x * x

new_square = and_add(square, 3)
print (new_square(4))
