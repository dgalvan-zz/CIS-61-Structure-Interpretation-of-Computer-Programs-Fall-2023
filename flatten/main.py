def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    result = []

    for item in lst:
        if type(item) == list:
            # If it's a list, recursively call flatten.
            sub_result = flatten(item)
            # Use list concatenation to add sub-items to the result.
            result += sub_result
        else:
            # If it's not a list, add it directly to the result list.
            result += [item]

    return result