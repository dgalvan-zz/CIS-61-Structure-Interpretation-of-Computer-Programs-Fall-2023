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


def print_tree(t, indent=0):
    if is_leaf(t):
        print(" " * indent + str(label(t)))
    else:
        print(" " * indent + str(label(t)))
        for b in branches(t):
            print_tree(b, indent + 1)


def count_nodes(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += count_nodes(b)
    return 1 + total


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """

    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += height(b)
    return total


t = tree(3, [tree(5, [tree(1)]), tree(2)])
print(height(t))
