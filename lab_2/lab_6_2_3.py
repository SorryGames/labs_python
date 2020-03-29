#!/usr/bin/env python3

import os
import uuid
import argparse
from progressbar import Progressbar 
from useful_module import termcolor, open_file 
from merge_sort import sort, merge


class SortFile:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        #
        self.cin = open_file(args.input, "r", "Can't open input file!")
        self.cout = open_file(args.output, "w", "Can't create output file!")
        #
        self.divide_file()
        self.cin.close()
        #
        self.sort_files()
        self.merge_files()
        #
        # for filename in self.filenames:
        #     if os.path.exists(filename):
        #         os.remove(filename)


    def divide_file(self, parts=128):
        self.filenames = [ str(uuid.uuid1())+"-temp" for i in range(parts) ]
        #
        self.fileobjects = [ open_file(name, "w", "Can't create temp-file!") 
                                                for name in self.filenames ]
        #
        i = 0
        line = self.cin.readline()
        while line:
            line = " ".join(sort(line.strip().split(" "))) + "\n"
            self.fileobjects[i % parts].write(line)
            line = self.cin.readline()
            i += 1
        for file in self.fileobjects:
            file.close()

    def sort_files(self):
        for filename in self.filenames:
            infile = open_file(filename, "r", "Can't open temp-file!")
            lines = []
            line = infile.readline()
            while line:
                lines.append(line)
                line = infile.readline()
            infile.close()
            os.remove(filename)
            #
            outfile = open_file(filename, "w", "Can't create temp-file")
            for line in sort(lines):
                outfile.write(line)
            outfile.close()

    def merge_files(self):
        pass

    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="Use this module implements "\
                            "external mergesort. ")
        pr.add_argument("-i", "--input",
                            help="Specify input file. Default: input.txt",
                            default="input.txt",
                            type=str)
        pr.add_argument("-o", "--output", 
                            help="Specify output file. Default: output.txt",
                            default="output.txt")
        return pr.parse_args()


if __name__ == "__main__":
    file_manage = SortFile()
    file_manage.start()