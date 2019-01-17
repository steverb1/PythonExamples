def my_decorator():
    def wrapper(func):
        def wrapped(name):
            print("Something is happening before the function is called.")
            func(name)
            print("Something is happening after the function is called.")
        return wrapped
    return wrapper

@my_decorator()
def say_hello(name):
    print("Hello " + name)

say_hello("Bob")




def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello ")

say_hello()
