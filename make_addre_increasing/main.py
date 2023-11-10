def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    """ YOUR CODE HERE """

    def adder(x):
        nonlocal n
        result = n + x
        n += 1
        return result
    return adder

# Test cases
adder1 = make_adder_inc(5)
adder2 = make_adder_inc(6)

print(adder1(2))  # Output: 7
print(adder1(2))  # Output: 8
print(adder1(10))  # Output: 17
print([adder1(x) for x in [1, 2, 3]])  # Output: [9, 11, 13]
print(adder2(5))  # Output: 11
