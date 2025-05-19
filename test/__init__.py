class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        self.bool = 1 <> 2 # Noncompliant: the operator "<>" is deprecated.
        return self  # Noncompliant: a TypeError will be raised - AGAIN

    def __iter__(self):
        return None  # Noncompliant: Not a valid iterator
