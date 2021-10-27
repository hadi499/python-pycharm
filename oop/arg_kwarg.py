def myfun(*argv):
    for arg in argv:
        print(arg)


myfun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print('--------------------')


def myfunc(**kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))


# Driver code
myfunc(first='Geeks', mid='for', last='Geeks')
