#!/usr/bin/env python3

import argparse
from checker import Checker
from sqrt_structure import SqrtDecomposition
from useful_module import termcolor, open_file


class FirstTask:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        self.output_file = args.output
        self.input_file = args.input
        if args.auto:
            try:
                checker = Checker(args.count_test,
                                    args.size_array,
                                    args.output)
                checker.generate()
            except:
                print("{0}ERROR: Parameters for auto-checker "\
                                            "are wrong!{1}".format(
                                                            termcolor.FAIL,
                                                            termcolor.ENDC))
        else:
            self.sqrt_manage()

    def sqrt_manage(self):
        # input file if presented
        if self.input_file is not None:
            self.cin = open_file(self.input_file, "r", 
                                            "Can't open input file!")
        # output file if presented
        if self.output_file is not None:
            self.cout = open_file(self.output_file, "w", 
                                            "Can't create output file!")
        # enter array
        try:
            array = [ int(i) for i in self.input("Enter array: ") ]
        except:
            print(termcolor.FAIL
                + "ERROR: Check the entered array!"
                + termcolor.ENDC)
            exit()
        # create sqrt structure
        sqrt = SqrtDecomposition(array)
        query = self.input("[INFO] "\
            "{0}1 <= L <= R <= {2}{1}"\
            "\nQueries should match the following syntax : "\
            "\n\t{0}assign L R X{1}\tassign the value of X to elements [L, R]"\
            "\n\t{0}add L R X{1}   \tadd the value of X to elements [L, R]"\
            "\n\t{0}get L R{1}     \tget the sum of elements [L, R]"\
            "\n\t{0}exit{1}        \tstop the program\n\n".format(
                                                            termcolor.BOLD,
                                                            termcolor.ENDC,
                                                            len(array)))
        # processing queries
        count = 1
        while True:
            if query[0] == "exit":
                if self.output_file is not None:
                    self.cout.close()
                if self.input_file is not None:
                    self.cin.close()
                exit()
            if query[0] == "":
                query = self.input()
                continue
            # else let's find the instructions
            try:
                query[1:3] = [ int(i)-1 for i in query[1:3] ]
                query[3:] = [ int(i) for i in query[3:] ]
                if query[1] < 0 or query[2] >= len(array)\
                                or query[1] > query[2]:
                    raise Exception
                if query[0] == "assign":
                    query.pop(0)
                    sqrt.assign(*query)
                elif query[0] == "add":
                    query.pop(0)
                    sqrt.add(*query)
                elif query[0] == "get":
                    query.pop(0)
                    self.print(str(sqrt.get(*query)))
                else:
                    raise Exception
            except:
                print("{0}ERROR: Check your query (#{1}){2}\n".format(
                                                                termcolor.FAIL,
                                                                count, 
                                                                termcolor.ENDC))
            query = self.input()
            count += 1

    def print(self, text):
        if self.output_file is None:
            print(text)
        else:
            self.cout.write(text + "\n")

    def input(self, text=""):
        if self.input_file is None:
            payload = str(input(text))
        else:
            payload = self.cin.readline()
        return payload.strip().split(" ")

    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="Use this module to interact with "\
                            "Sqrt Decomposition by "\
                            "[file | console | auto-checker]")
        pr.add_argument("-i", "--input", 
                            help="Specify input file.")
        pr.add_argument("-a", "--auto", 
                            help="Specify to run auto-checker.", 
                            action="store_true")
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


if __name__ == "__main__":
    task = FirstTask()
    task.start()