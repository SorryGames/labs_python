#!/usr/bin/env python3


def _decorator_try_except(*args, **kwargs):
    def _inner_decorator():
        pass
    return _inner_decorator


def _merge_function(list_of_classes):
    index = 0
    merge_result = []
    while True:
        #
        while index < len(list_of_classes) and len(list_of_classes[index]) == 0:
            index += 1
        #
        if index >= len(list_of_classes):
            break
        #
        cur_head = list_of_classes[index][0]
        skip_index = False 
        #
        for el in list_of_classes:
            if not (el.count(cur_head) == 0 or (el.count(cur_head) == 1 and el.index(cur_head) == 0)):
                skip_index = True;
                index += 1
                break
        #
        if skip_index:
            continue
        #
        for el in list_of_classes:
            if el.count(cur_head) > 0: 
                el.remove(cur_head)
        #
        merge_result.append(cur_head)
        index = 0
    #
    for el in list_of_classes:
        if len(el) > 0:
            raise TypeError
    #
    return merge_result


def _linear_function(class_name):
    if len(class_name.__bases__) == 0:
        return [ class_name ]
    #
    parents = [ [el] for el in class_name.__bases__ ]
    parents_linear = [ _linear_function(el) for el in class_name.__bases__ ]
    #
    linear_result = [ class_name ] + _merge_function(parents_linear + parents)
    #
    return linear_result



def own_mro(class_name):
    #
    mro_order = _linear_function(class_name)
    #
    return tuple(mro_order)
    