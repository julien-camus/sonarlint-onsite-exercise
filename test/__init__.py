class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant: a TypeError will be raised

    def __iter__(self):
        return None  # Noncompliant: Not a valid iterator
