def fib():
    x = 1
    y = 1
    while True:
        yield x
        x,y = y, x + y

import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break