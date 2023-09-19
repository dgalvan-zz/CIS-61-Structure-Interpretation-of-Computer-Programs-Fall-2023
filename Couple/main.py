def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2)

    "*** YOUR CODE HERE ***"
    result = []  # Initialize an empty list to store the coupled lists

    for i in range(len(s1)):
        coupled_element = [s1[i], s2[i]]  # Create a coupled list [s1[i], s2[i]]
        result = result + [coupled_element]  # Combine the result list with the new coupled list

    return (result)
s1 = [1, 2, 3]
s2 = [4, 5, 6]

result= couple(s1, s2)
print (result)
