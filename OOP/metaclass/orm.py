#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Fount mappings  %s ====> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self):
        self[key] = value

    def save():
        pass


class User(Model):
    id1       = IntegerField('id')
    name     = StringField('name')
    email    = StringField('email')
    password = StringField('password')

#创建一个实例:
u = User(id = 123, name = 'Heikki', email = 'Heikki-hz@gmail.com', password = '123')

u.save()
