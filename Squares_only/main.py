import math
def squares(s):
    """Returns a new list containing square roots of the elements of the original list
    that are perfect squares.
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    #return [round(math.sqrt(x)) for x in s if int(math.sqrt(x))**2 == x] list comprehencion 


    "*** YOUR CODE HERE ***"
    result = []
    for x in s:
        if int(math.sqrt(x))**2 == x:
            result = result + [round(math.sqrt(x))]
    return result

seq = [500, 30]
rsult=squares(seq)
print (rsult)
