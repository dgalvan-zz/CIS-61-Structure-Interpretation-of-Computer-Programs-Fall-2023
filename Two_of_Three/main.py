def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a, b, c) ** 2 + (a + b + c - max(a, b, c) - min(a, b, c)) ** 2


if __name__ == '__main__':
    print(two_of_three(1, 2, 3))
    print(two_of_three(5, 3, 1))
    print(two_of_three(10, 2, 8))
    print(two_of_three(5, 5, 5))
