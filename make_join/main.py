def make_withdraw(balance, password):
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
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    attempts = []
    def joint_withdraw(amount, password):
        if password == new_password:
            return withdraw(amount, old_password)
        result = withdraw(amount, password)
        if type(result) == int:
            return result
        elif type(result) == str and result == 'Incorrect password':
            attempts.append(password)
            if len(attempts) >= 3:
                return f"Your account is locked. Attempts: {attempts}"
            return result
        else:
            return result

    initial_result = withdraw(0, old_password)
    if type(initial_result) == int:
        return joint_withdraw
    else:
        return initial_result