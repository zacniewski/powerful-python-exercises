# Decorators

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("John", "Doe")
print(person.full_name)


# Ex 2
def printlog(func):
    def wrapper(*args, **kwargs):
        print(f"CALLING {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@printlog
def foo(x):
    print(x + 2)


foo(8)
