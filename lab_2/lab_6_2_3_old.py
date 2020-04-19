#!/usr/bin/env python3

import os
import sys
import uuid
import argparse

from modules.merge_sort import sort, merge
from modules.progressbar import Progressbar 
from modules.useful import termcolor, open_file 


class SortFile:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        #
        self.cin = open_file(args.input, "r", "Can't open input file!")
        self.cout = open_file(args.output, "w", "Can't create output file!")
        #
        input_size = os.stat(args.input).st_size
        self.divide_file(args.parts, input_size)
        self.cin.close()
        #
        self.sort_files()
        #
        self.merge_files()
        #
        os.rename(self.filenames[0], args.output)

    def divide_file(self, parts, input_size):
        self.filenames = [ str(uuid.uuid1())+"-temp" for i in range(parts) ]
        #
        self.fileobjects = [ open_file(name, "w", "Can't create temp-file!") 
                                                for name in self.filenames ]
        #
        i = 0
        progressbar_size = 0
        line = self.cin.readline()
        divide_progress = Progressbar(description="Division")
        while line:
            progressbar_size += len(line)
            line = " ".join(sort(line.strip().split(" "))) + "\n"
            self.fileobjects[i % parts].write(line)
            line = self.cin.readline()
            if i % 10000 == 0:
                divide_progress.update(progressbar_size, input_size)
            i += 1
        for file in self.fileobjects:
            file.close()
        divide_progress.update(100)

    def sort_files(self):
        progressbar_count = 0
        sort_progress = Progressbar(description="Sorting")
        for filename in self.filenames:
            infile = open_file(filename, "r", "Can't open temp-file!")
            lines = infile.readlines()
            infile.close()
            os.remove(filename)
            #
            outfile = open_file(filename, "w", "Can't create temp-file")
            outfile.writelines(sort(lines))
            outfile.close()
            progressbar_count += 1
            sort_progress.update(progressbar_count, len(self.filenames))


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
        progressbar_count = len(self.filenames)
        merge_progress = Progressbar(description="Merging")
        while len(self.filenames) > 1:
            self.filenames.append(self.merge_two_files(self.filenames[0], 
                                                        self.filenames[1]))
            [ self.filenames.pop(0) for i in range(2) ]
            merge_progress.update(progressbar_count - len(self.filenames) + 1,
                                                            progressbar_count)

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
                            help="Specify amount of temp-files. Default: 64",
                            default=64,
                            type=int)
        return pr.parse_args()


if __name__ == "__main__":
    file_manage = SortFile()
    file_manage.start()