
def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    # Base case: If b is 0, the GCD is a (the non-zero value).
    if b == 0:
        return a
    # Recursive case: Compute the GCD of b and the remainder of a divided by b.
    return gcd(b, a % b)