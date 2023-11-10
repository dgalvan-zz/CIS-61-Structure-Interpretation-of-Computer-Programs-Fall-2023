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
        print("  " * indent + str(label(t)))
    else:
        print("  " * indent + str(label(t)))
        for b in branches(t):
            print_tree(b, indent + 1)


def count_nodes(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += count_nodes(b)
    return 1 + total


def prune_leaves(t, values):
    """Return a modified copy of t with all leaves that have a label that appears
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"

    if is_leaf(t) and (label(t) in values):
        return None
    new_branches = []
    for b in branches(t):
        new_branch = prune_leaves(b, values)
        if new_branch:
            new_branches += [new_branch]
    return tree(label(t), new_branches)





t = tree(2)
print(prune_leaves(t, (1, 2)))
# None
numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
print_tree(numbers)
''' 1
      2
      3
        4
        5
      6
        7'''
print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
'''
    1
      2
      3
        5
      6
    '''