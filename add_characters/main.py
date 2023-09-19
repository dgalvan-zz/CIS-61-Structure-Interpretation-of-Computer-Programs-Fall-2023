def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.
    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    "*** YOUR CODE HERE ***"

    if len(w1) == 0:
        # If w1 is empty, return the remaining characters from w2
        return w2
    elif len(w2) == 0:
        # If w2 is empty but w1 still has characters, return an empty string
        return ""
    elif w1[0] == w2[0]:
        # If the first characters of both words match, move to the next character
        return add_chars(w1[1:], w2[1:])
    else:
        # If they don't match, add the character from w2 to the result
        return w2[0] + add_chars(w1, w2[1:])