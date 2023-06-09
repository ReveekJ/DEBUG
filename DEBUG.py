from datetime import datetime


def _timer(func):
    def inner(*args):
        start = datetime.now()
        func(args)
        stop = datetime.now()
        return stop - start

    return inner


DEBUG = True
