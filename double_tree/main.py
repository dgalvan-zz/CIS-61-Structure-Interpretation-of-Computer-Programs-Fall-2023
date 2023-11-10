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


def double_tree(t):
    """Return a tree with the square of every element in t
            numbers = tree(1,
                           [tree(2,
                                 [tree(3),
                                  tree(4)]),
                           tree(5,
                                [tree(6,
                                      [tree(7)]),
                                 tree(8)])])
        >>> print_tree(double_tree(numbers))
        2
          4
            6
            8
          10
            12
              14
            16
        """

    if is_leaf(t):
        return tree(label(t) * 2)
    lst = []
    for b in branches(t):
        lst += [double_tree(b)]
    new_label = label(t) * 2
    return tree(new_label, lst)


numbers = tree(1,
               [tree(2,
                     [tree(3),
                      tree(4)]),
                tree(5,
                     [tree(6,
                           [tree(7)]),
                      tree(8)])])
print_tree(double_tree(numbers))