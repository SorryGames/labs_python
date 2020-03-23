#!/usr/bin/env python3

import argparse
from sqrt_structure import SqrtDecomposition
from checker import Checker


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class FirstTask:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        self.output_file = args.output
        self.input_file = args.input
        if args.auto:
            checker = Checker(args.count_test, args.size_array, args.output)
            checker.generate()
        else:
            try:
                array = [ int(i) for i in self.input("Enter array: ") ]
            except ValueError:
                print(bcolors.FAIL
                    + "ERROR: Check the entered array!"
                    + bcolors.ENDC)
                exit()
            sqrt = SqrtDecomposition(array)
            query = self.input("Queries should match the following syntax: \
                \n\t{0}assign 2 3 5{1} \tassign the value of 5 to elements [2, 3]\
                \n\t{0}add 4 6 2{1}    \tadd the value of 2 to elements [4, 6]\
                \n\t{0}get 1 3{1}      \tget the sum of elements [1, 3]\n".format(bcolors.BOLD, bcolors.ENDC))
            while query: 
                try:
                    if query[0] == "assign":
                        query.pop(0)
                        sqrt.assign(*[query])
                    elif query[0] == "add":
                        query.pop(0)
                        sqrt.add(*query)
                    elif query[0] == "get":
                        query.pop(0)
                        self.print("\t" + sqrt.get(*query))
                except None:
                    print("ERROR: Check your query ({})".format(query))
                query = self.input()
            
    def print(self, text):
        if self.output_file is None:
            print(text)
        else:
            self.cout.writeline(text)

    def input(self, text=""):
        if self.input_file is None:
            payload = str(input(text))
        else:
            payload = self.cin.readline()
        return payload.strip().split(" ")

    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="Use this module to interact with Sqrt \
                            Decomposition by [file | console | auto-checker]")
        pr.add_argument("-i", "--input", 
                            help="Specify input file.")
        pr.add_argument("-a", "--auto", 
                            help="Specify to run auto-checker.", action="store_true")
        pr.add_argument("-s", "--size-array", 
                            help="Auto-checker argument.",
                            default=10,
                            type=int)
        pr.add_argument("-c", "--count-test", 
                            help="Auto-checker argument.",
                            default=1000,
                            type=int)
        pr.add_argument("-o", "--output", 
                            help="Specify output file.")
        return pr.parse_args()


task = FirstTask()
task.start()