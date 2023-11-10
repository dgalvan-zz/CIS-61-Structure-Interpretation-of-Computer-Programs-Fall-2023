def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"

    incorrect_passwords = []
    attempts = 0
    locked = False

    def withdraw(amount, entered_password):
        nonlocal balance, attempts, locked

        if locked:
            return f"Your account is locked. Attempts: {incorrect_passwords}"

        if entered_password != password:
            incorrect_passwords.append(entered_password)
            if len(incorrect_passwords) >= 3:
                locked = True
            return 'Incorrect password'

        if amount > balance:
            return 'Insufficient funds'

        balance -= amount
        return balance

    return withdraw


w = make_withdraw(100, 'hax0r')
print(w(25, 'hax0r'))
error = w(90, 'hax0r')
print(error)
error = w(25, 'hwat')
print(error)
new_bal = w(25, 'hax0r')
print(new_bal)
print(w(75, 'a'))
print(w(10, 'hax0r'))
print(w(20, 'n00b'))
print(w(10, 'hax0r'))
print(w(10, 'l33t'))
print(type(w(10, 'l33t')) == str)