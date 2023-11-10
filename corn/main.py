# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


# Selectors
def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True


def is_leaf(tree):
    return not branches(tree)


# Function to find 'acorn' in a tree
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
        >>> scrat = tree('acorn')
        >>> acorn_finder(scrat)
        True
        >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
        >>> acorn_finder(sproul)
        True
        >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
        >>> acorn_finder(numbers)
        False
        """
    "*** YOUR CODE HERE ***"

    # Base case: if the tree is empty, return False
    if not is_tree(t):
        return False

    # Check if the current node has the value 'acorn'
    if label(t) == 'acorn':
        return True

    # Recursively check the subtrees
    for subtree in branches(t):
        if acorn_finder(subtree):
            return True

    # If 'acorn' is not found in the current node or any subtree, return False
    return False


# Test Trees
scrat = tree('acorn')
print(acorn_finder(scrat))  # True

sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
print(acorn_finder(sproul))  # True

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
print(acorn_finder(numbers))  # False