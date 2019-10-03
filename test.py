def hello():
    print("hello")


def hi():
    print("hi")


def mixed():
    g = [hello, hi]
    for i in g:
        i()
        print('__--__')


mixed()