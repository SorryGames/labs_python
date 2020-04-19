#!/usr/bin/env python3

import os
import sys
import uuid
import argparse
import time

from modules.merge_sort import sort, merge
from modules.progressbar import Progressbar 
from modules.useful import termcolor, open_file 
from modules.tempfile import TempFile 


class SortFile:
    MAX_SYMBOLS_PER_READ = 5000000
    count_remove = 0

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        #
        cin = open_file(args.input, "r", "Can't open input file!")
        cout = open_file(args.output, "w", "Can't create output file!")
        #
        source_cin = self._read_from_file(cin, " ", "\n")
        while self._sort_line(source_cin, cout):
            pass
        #
        cin.close(); cout.close()

    def _read_from_file(self, file_in, *separators):
        symbol_count=self.MAX_SYMBOLS_PER_READ
        data = ""
        while True:
            if data == "":
                data = file_in.read(symbol_count)
            position = symbol_count
            for symbol in separators:
                temp_position = data.find(symbol)
                if temp_position >= 0:
                    position = min(position, temp_position)
            yield data[:position+1]
            data = data[position+1:]

    def _file_to_line(self, in_filename, out_file):
        pass 

    def _line_to_file(self, in_filename, out_file):
        pass

    def _sort_line(self, in_source, out_file, max_temp_files=128):
        temp = TempFile()
        filename_array = []
        while True:
            data = next(in_source)
            if data == "":
                break
            elif data[-1] == " ":
                temp.push(data.strip())
                filename_array.append(temp.reload())
            elif data[-1] == "\n":
                temp.push(data.strip())
                filename_array.append(temp.reload())
                break
            else:
                temp.push(data.strip())
            if len(filename_array) == max_temp_files:
                self._merge_files(filename_array)
        #
        if not len(filename_array):
            return False
        #
        self._merge_files(filename_array)
        self._file_to_line(filename_array[0], out_file)
        os.remove(filename_array[0])
        self.count_remove += 2
        #
        return True

    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="This module performs "\
                            "sorting of any file. ")
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
    start = int(time.perf_counter())
    
    file_manage = SortFile()
    file_manage.start()
    print(file_manage.count_remove)

    finish = int(time.perf_counter())
    print("{}:{}".format((finish - start) // 60, (finish - start) % 60))
