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
        self.divide_file(args.parts)
        self.cin.close()
        #
        self.sort_files()
        #
        self.merge_files()
        #
        os.rename(self.filenames[0], args.output)

    def divide_file(self, parts):
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
            lines = infile.readlines()
            infile.close()
            os.remove(filename)
            #
            outfile = open_file(filename, "w", "Can't create temp-file")
            outfile.writelines(sort(lines))
            outfile.close()

    def merge_two_files(self, filename_a, filename_b):
        filename = str(uuid.uuid1()) + "-temp"
        # 
        file_a = open_file(filename_a, "r", "Can't open temp-file!")
        file_b = open_file(filename_b, "r", "Can't open temp-file!")
        #
        outfile = open_file(filename, "w", "Can't create temp-file!")
        #
        line_a, line_b = file_a.readline(), file_b.readline()
        while line_a and line_b:
            if line_a < line_b:
                outfile.write(line_a)
                line_a = file_a.readline()
            else:
                outfile.write(line_b)
                line_b = file_b.readline()
        #
        outfile.writelines([line_a, line_b])
        outfile.writelines(file_a.readlines())
        outfile.writelines(file_b.readlines())
        #
        outfile.close(); file_a.close(); file_b.close()
        os.remove(filename_a); os.remove(filename_b)
        #
        return filename


    def merge_files(self):
        while len(self.filenames) > 1:
            self.filenames.append(self.merge_two_files(self.filenames[0], self.filenames[1]))
            [ self.filenames.pop(0) for i in range(2) ]

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
        pr.add_argument("-p", "--parts", 
                            help="Specify amount of temp-files. Default: 16",
                            default=16,
                            type=int)
        return pr.parse_args()


if __name__ == "__main__":
    file_manage = SortFile()
    file_manage.start()