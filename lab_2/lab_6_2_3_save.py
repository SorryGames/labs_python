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

    def _buffer_less_or_equal_than(self, filename_a, filename_b):
        a_file = open_file(filename_a, "r", "Can't open temp-file!")
        b_file = open_file(filename_b, "r", "Can't open temp-file!")
        #
        source_a = self._read_from_file(a_file)
        source_b = self._read_from_file(b_file) 
        while True:     
            data_a, data_b = next(source_a), next(source_b)  
            if data_a != data_b or not data_a or not data_b:
                break
        a_file.close(); b_file.close()
        return data_a <= data_b

    def _line_from_buffer_to_flow(self, in_filename, out_file):
        in_file = open_file(in_filename, "r", "Can't open temp-file!")
        source = self._read_from_file(in_file)
        data = ":)"
        while data:
            data = next(source)
            data = data.strip()
            out_file.write(data)
        out_file.write("\n")
        in_file.close()

    def _line_from_flow_to_buffer(self, in_source, out_filename):
        out_file = open_file(out_filename, "w", "Can't create temp-file!")
        flow_empty = True
        #
        while True:
            data = next(in_source)
            if data == "":
                break
            else:
                out_file.write(data.strip())
                flow_empty = False
            if data[-1] == "\n":
                break
        #
        out_file.close()
        return not flow_empty

    def _merge_two_files(self, filename_a, filename_b):
        a_file = open_file(filename_a, "r", "Can't open temp-file!")
        b_file = open_file(filename_b, "r", "Can't open temp-file!")
        #
        a_source = self._read_from_file(a_file, "\n")
        b_source = self._read_from_file(b_file, "\n")
        #
        temp = TempFile()
        a_buffer, b_buffer, result_buffer = [ temp.reload() for i in range(3) ]
        result_file = open_file(result_buffer, "w", "Can't create temp-file!")
        #
        a_not_empty = self._line_from_flow_to_buffer(a_source, a_buffer)
        b_not_empty = self._line_from_flow_to_buffer(b_source, b_buffer)
        #
        #
        while a_not_empty and b_not_empty:
            if self._buffer_less_or_equal_than(a_buffer, b_buffer):
                self._line_from_buffer_to_flow(a_buffer, result_file)
                a_not_empty = self._line_from_flow_to_buffer(a_source, a_buffer)
            else:
                self._line_from_buffer_to_flow(b_buffer, result_file)
                b_not_empty = self._line_from_flow_to_buffer(b_source, b_buffer)
        #
        #
        while a_not_empty:
            self._line_from_buffer_to_flow(a_buffer, result_file)
            a_not_empty = self._line_from_flow_to_buffer(a_source, a_buffer)
        while b_not_empty:
            self._line_from_buffer_to_flow(b_buffer, result_file)
            b_not_empty = self._line_from_flow_to_buffer(b_source, b_buffer)
        #
        a_file.close(); b_file.close(); result_file.close()
        for filename in [filename_a, filename_b, a_buffer, b_buffer]:
            os.remove(filename)
            self.count_remove += 1
        self.count_remove += 1
        #
        return result_buffer

    def _merge_files(self, filename_array): 
        while len(filename_array) > 1:
            filename_array.append(self._merge_two_files(filename_array[0],
                                                        filename_array[1]))
            filename_array.pop(0); filename_array.pop(0)

    def _file_to_line(self, in_filename, out_file):
        in_file = open_file(in_filename, "r", "Can't open temp-file!")
        in_source = self._read_from_file(in_file, "\n")
        data = ":)"
        while data:
            data = next(in_source)
            out_file.write(data.strip() + " ")
        out_file.write("\n")
        in_file.close()

    def _line_to_file(self, in_filename, out_file):
        in_file = open_file(in_filename, "r", "Can't open temp-file!")
        in_source = self._read_from_file(in_file, "\n")
        data = ":)"
        while data:
            data = next(in_source)
            out_file.write(data.strip() + " ")
        out_file.write("\n")
        in_file.close()

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
