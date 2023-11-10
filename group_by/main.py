def group_by(seq, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """

    result = {}
    for item in seq:
        key = fn(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    sorted_result = dict(sorted(result.items()))  # Sort the dictionary by keys
    return sorted_result

print (group_by([12, 23, 14, 45], lambda p: p // 10) )
'''{1: [12, 14], 2: [23], 4: [45]}'''
print (group_by(list(range(-3, 4)), lambda x: x * x))
'''{0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]} '''
