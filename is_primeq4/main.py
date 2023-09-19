def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # Define a helper function to check for divisibility.
    def is_divisible(x, divisor):
        if divisor == 1:
            return False
        elif x % divisor == 0:
            return True
        else:
            return is_divisible(x, divisor - 1)
    # Base case: 1 is not a prime number.
    if n == 1:
        return False
    # Base case: 2 is a prime number.
    elif n == 2:
        return True
    else:
        # Start checking for divisibility from 2 to the square root of n.
        return not is_divisible(n, int(n**0.5) + 1)

