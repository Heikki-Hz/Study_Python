#!/usr/bin/env python3

import functools

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log_d(test):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (test, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def log_complete(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

######## test ############
@log
def now():
    print('2016-2-22')
now()
print('\n')


@log_complete
def now():
    print('2016-2-22')
now()
print('\n')

@log_d('test1111')
def now():
    print('2016-2-22')
now()
