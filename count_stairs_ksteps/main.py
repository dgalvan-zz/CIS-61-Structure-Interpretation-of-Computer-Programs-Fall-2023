def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    # Base case: If n is 0, there is only one way to reach it (by doing nothing).
    if n == 0:
        return 1
    else:
        total = 0
        
        for step in range(1, min(n, k) + 1):

            total += count_k(n - step, k)
        return total
