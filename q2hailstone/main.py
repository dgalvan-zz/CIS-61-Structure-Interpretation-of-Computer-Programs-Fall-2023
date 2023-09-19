def hailstone(n, sume=0):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """


    print(n)
    if n == 1:
        return sume  # Base case: n has reached 1, return the number of steps
    elif n % 2 == 0:
        return hailstone(n // 2, sume + 1)  # If n is even, divide it by 2
    else:
        return hailstone((n * 3) + 1, sume + 1)  # If n is odd, multiply by 3 and add 1

a = hailstone(10)
print(a)