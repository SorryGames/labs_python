#! /usr/bin/env python3

def flatten(data):
    for i in data:
        yield i

a = flatten(1)


print(next(a))


print(next(a))


print(a.__next__())