#!/usr/bin/env python3

from mro import own_mro

class A: pass
class C: pass 
class B(C): pass
class D(B, A): pass
class E(D, A): pass


print(E.__mro__)
print(own_mro(E))
print(E.__mro__ == own_mro(E))