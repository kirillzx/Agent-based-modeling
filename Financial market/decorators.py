import time

def timeit(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time() - t1
        print(t2)
        return f
    return wrapper
