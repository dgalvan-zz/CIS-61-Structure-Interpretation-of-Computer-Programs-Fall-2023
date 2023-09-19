def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    digit_counts = [0] * 10
    total_pairs = 0

    while n > 0:
        last_digit = n % 10
        complement = 10 - last_digit


        if 0 <= complement <= 9:
            total_pairs += digit_counts[complement]

        digit_counts[last_digit] += 1
        n //= 10

    return total_pairs
# Test cases
print(ten_pairs(7823952))
print(ten_pairs(55055))
print(ten_pairs(9641469))
