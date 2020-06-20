#!/usr/bin/env python3

from mro import own_mro

class A: pass
class C: pass 
class B(C): pass
class D(B, A): pass
class E(D, A): pass
class F(E, B, A): pass
class G(F, E, D, B): pass
class K(G, F, E, D, B): pass


print(K.__mro__)
print(own_mro(K))

print()
print(K.__mro__ == own_mro(K))