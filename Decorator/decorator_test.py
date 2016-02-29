#!/usr/bin/env python3
import functools

#test1
def log(func):
    def wrapper(*args, **kw):
        print('Call begin')
        a = func(*args, **kw)
        print('Call end')
        return a
    return wrapper

# @log
# def now():
    # print('Time is b')
# now()




def log_d(test):
    def decorator(func):
        def wrapper(*args, **kw):
            print('Call begin')
            print('%s  %s' % (test, func.__name__))
            a = func(*args, **kw)
            print('Call end')
            return a
        return wrapper
    if (isinstance(test, str)):
        return decorator
    func = test
    test = "Hello"
    return decorator(func)

            

########
@log_d('test')
def now():
    print('Time is')
now()
print('\n')
@log_d
def now():
    print('Time')
now()


