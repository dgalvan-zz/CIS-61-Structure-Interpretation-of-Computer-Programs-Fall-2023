def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6"""
    total = 0
    while n > 0:
        digit = n % 10  # Extract the last digit
        total += digit  # Add the extracted digit to the total
        n //= 10  # Remove the last digit by floor division
    return total


if __name__ == '__main__':
    print(sum_digits(10))
    print(sum_digits(4224))
    print(sum_digits(1234567890))
    x = sum_digits(123)
    print(x)
