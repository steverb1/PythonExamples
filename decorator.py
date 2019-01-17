def my_decorator(text):
    def wrapper(func):
        def wrapped(firstName, lastName):
            print("Something is happening before the function is called. " + text)
            func(firstName, lastName)
            print("Something is happening after the function is called. " + text)
        return wrapped
    return wrapper

@my_decorator("parameter")
def say_hello(firstName, lastName):
    print("Hello " + firstName, lastName)

say_hello("Bob", "Bobber")



def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
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
