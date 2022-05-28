def foo(a, b, x=2, y=3):
    return (a+b) / (x+y)


def takes_any_args(*args):
    print(f"The args are: {args}")
    print(f"Type of args is: {type(args)}")


some_foo = foo(b=4, x=3, a=5)
print(f"{some_foo=}")

print(takes_any_args(1, 2))
print(takes_any_args([1, 2]))


def normal_function(a, b, c):
    print(f"{a=}, {b=}, {c=}")


some_numbers = (3, 6, 7)
normal_function(*some_numbers)
