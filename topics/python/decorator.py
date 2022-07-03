def decorator(func):
    def inner(*args, **kwargs):
        print("In decorator")
        func(*args, **kwargs)
    inner()


@decorator
def f():
    print("In method")