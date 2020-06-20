#!/usr/bin/env python3

from mro import own_mro


class super_puper():

    def __init__(self, class_name):
        self.mro_order = own_mro(class_name)[1:]

    def __getattr__(self, method_name):
        for class_name in self.mro_order:
            if method_name in dir(class_name):
                return getattr(class_name(), method_name)
        return None
