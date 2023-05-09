from datetime import datetime


def _timer(func):
    def inner():
        start = datetime.now()
        func()
        stop = datetime.now()
        return stop - start

    return inner


DEBUG = True
