#!/usr/bin/env python3

import sys
import argparse

from modules.useful import termcolor


def _flatten_it(data, history):
    history.append(id(data))
    #
    for element in data:
        if id(element) in history:
            yield None
        elif isinstance(data, dict):
            if isinstance(data[element], dict):
                yield from _flatten_it(data[element], history)
            else:
                yield {element: data[element]}
        elif isinstance(element, (list, dict, tuple)):
            try:
                yield from _flatten_it(element, history)
            except:
                yield None
        else:
            yield element
    history.pop()


def flatten_it(data):
    return _flatten_it(data, [])


if __name__ == "__main__":
    pr = argparse.ArgumentParser(
                        description="Module flattens "\
                            "[ list | tuple | dict ]")
    pr.parse_args()
    #
    #
    #
    cycle_1 = [1, 2, [4, 5]]
    cycle_1[2].append(cycle_1)
    cycle_1.append(cycle_1)
    #
    cycle_2 = [3, [4]]
    cycle_2[1].append(cycle_2)
    cycle_2[1][1].append(cycle_1)
    #
    tests = [
        {1: {2: 4, 3: {3: 6, 4: 8}}, 5: 10},
        [1, 2, [[3, 4], 5], [6]], 
        (1, 2, (3, 4), (5, ), (6, (7, 8, (9, )))),
        cycle_1, 
        cycle_2
    ]
    #
    print()
    for data in tests:
        print(termcolor.WARNING, "test:", termcolor.ENDC,
                                    data)
        #
        answer = list(flatten_it(data))
        print(termcolor.OKGREEN, "answer:", termcolor.ENDC,
                                    answer, end="\n\n")