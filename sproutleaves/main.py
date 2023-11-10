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


def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in vals])
    return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])


t1 = tree(1, [tree(2), tree(3)])
new1 = sprout_leaves(t1, [4, 5])
print_tree(new1)