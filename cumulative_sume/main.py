class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def print_tree(t, indent=0):
    print(" " * indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent + 1)


"""Write a function cumulative_sum that mutates the Tree t so that each node
's label becomes the sum of all labels in the subtree rooted at the node."""


def cumulative_sum(t):
    if t.is_leaf():
        return t.label

    total = t.label
    for b in t.branches:
        total += cumulative_sum(b)

    t.label = total
    return total


t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
cumulative_sum(t)
print_tree(t)