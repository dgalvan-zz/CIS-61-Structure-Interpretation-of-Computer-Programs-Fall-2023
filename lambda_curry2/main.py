"""from operator import add
def curry2(func):
    def curried(x):
        def inner(y):
            return func(x, y)
        return inner
    return curried

curried_add = curry2(add)
add_three = curried_add(3)
add_three(5)"""
from operator import add

lambda_curry2 = lambda func: lambda x: lambda y: func(x, y)


if __name__ == '__main__':
    curried_add = lambda_curry2(add)
    add_three = curried_add(3)
    result = add_three(5)
    print(result)
