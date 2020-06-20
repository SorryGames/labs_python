#!/usr/bin/env python3

from super import super_puper

class A:
    def who_am_i(self):
        print("I am a A")

class B(A):
    def who_am_i(self):
        print("I am a B")

class C(A):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
    def who_am_i(self):
        super_puper(D).who_am_i()

d1 = D()
d1.who_am_i()