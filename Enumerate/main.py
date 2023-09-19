def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """

    "*** YOUR CODE HERE ***"
    result=[]
    for i in range (len(s)):
        lista= [start , s[i]]
        result+= [lista]
        start+=1
    return result


answer = enumerate([6, 1, 'a'])
print(answer)