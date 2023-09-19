def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n % 2 != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_prime(10))
    print(is_prime(7))
