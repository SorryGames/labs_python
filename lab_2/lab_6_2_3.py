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
    ERROR_READ = "Can't open file to read!"
    ERROR_WRITE = "Can't open file to write!"

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        self._sort_file(args.input, args.output)

    def _read_from_file(self, in_filename, *separators):
        in_file = open_file(in_filename, "r", self.ERROR_READ)
        MAX_SYMBOLS_PER_READ = 1000000  # 1mb 
        data = ""
        while True:
            if data == "":
                data = in_file.read(MAX_SYMBOLS_PER_READ)
            position = MAX_SYMBOLS_PER_READ
            #
            temp = [ data.find(char) for char in separators ]
            temp = [ i for i in temp if i >= 0] + [ position ]
            position = min(temp)
            #
            yield (data[:position], data[position:position+1])    
            data = data[position+1:]

    def _divide_file(self, in_filename):
        # =========================================================
        # 
        progressbar_cur = 0
        progressbar_max = os.stat(in_filename).st_size
        progressbar_process = Progressbar(description="Division")
        #
        # =========================================================
        MAX_SYMBOLS_PER_FILE = 1000000  # 1mb
        in_file = self._read_from_file(in_filename, "\n")
        #
        temp_array = [ TempFile(), TempFile() ]  # [ small, big ]
        filename_array = [ [], [] ]  # [ small, big ]
        key = 0  # (0: small, 1: big)
        #
        while True:
            data, wall = next(in_file)
            # =========================================================
            #
            progressbar_cur += len(data)
            #
            # =========================================================
            if not data and not wall:
                [ filename_array[key].append(temp_array[key].free()) 
                                                        for key in range(2) ]
                break
            #
            key = max(key, int(len(data) >= MAX_SYMBOLS_PER_FILE))
            #
            temp_array[key].push(data + wall)
            if wall and temp_array[key].sizeof() >= MAX_SYMBOLS_PER_FILE:
                filename_array[key].append(temp_array[key].free())
                key = 0
                # =========================================================
                #
                progressbar_process.update(progressbar_cur, progressbar_max)
                #
                # =========================================================
        #
        filename_array = [ [ i for i in filename_array[key] if i ] 
                                                    for key in range(2) ]
        # =========================================================
        #
        progressbar_process.update(100)
        #
        # =========================================================
        return filename_array

    def _sort_small_files(self, in_filenames):
        # =========================================================
        # 
        progressbar_cur = 0
        progressbar_max = len(in_filenames)
        progressbar_process = Progressbar(description="Sorting")
        #
        # =========================================================
        for filename in in_filenames:
            with open_file(filename, "r", self.ERROR_READ) as in_file:
                data = in_file.readlines()
            data = [ (i.replace("\n", "") + "\n") for i in data ]
            with open_file(filename, "w", self.ERROR_WRITE) as out_file:
                out_file.writelines(sort(data))
                # =========================================================
                # 
                progressbar_cur += 1
                progressbar_process.update(progressbar_cur, progressbar_max)
                #
                # =========================================================
        # =========================================================
        # 
        progressbar_process.update(100)
        #
        # =========================================================
        return in_filenames

    def _buffer_less_or_equal_than(self, filename_a, filename_b):
        source_a = self._read_from_file(filename_a)
        source_b = self._read_from_file(filename_b) 
        while True:     
            [data_a, _], [data_b, _] = next(source_a), next(source_b)  
            if data_a != data_b or not data_a or not data_b:
                break
        #
        return data_a <= data_b

    def _line_from_buffer_to_flow(self, in_filename, out_file):
        source = self._read_from_file(in_filename)
        data = ":)"
        while data:
            data, _ = next(source)
            data = data.strip()
            out_file.write(data)
        out_file.write("\n")

    def _line_from_flow_to_buffer(self, in_source, out_filename):
        out_file = open_file(out_filename, "w", self.ERROR_WRITE)
        flow_empty = True
        #
        while True:
            data, wall = next(in_source)
            if data:
                out_file.write(data)
                flow_empty = False
            if wall == "\n" or (not data and not wall):
                break
        #
        out_file.close()
        return not flow_empty

    def _merge_two_files_by_buffer(self, filename_a, filename_b):
        a_source = self._read_from_file(filename_a, "\n")
        b_source = self._read_from_file(filename_b, "\n")
        #
        temp = TempFile()
        a_buffer, b_buffer, result_buffer = [ temp.create_empty() 
                                                        for i in range(3) ]
        result_file = open_file(result_buffer, "w", self.ERROR_WRITE)
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
        result_file.close()
        for filename in [filename_a, filename_b, a_buffer, b_buffer]:
            os.remove(filename)
        #
        return result_buffer

    def _merge_two_files_by_line(self, filename_a, filename_b):
        filename = str(uuid.uuid1()) + "-temp"
        # 
        file_a = open_file(filename_a, "r", self.ERROR_READ)
        file_b = open_file(filename_b, "r", self.ERROR_READ)
        #
        outfile = open_file(filename, "w", self.ERROR_WRITE)
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

    def _merge_two_files(self, filename_a, filename_b, compare_by_pieces):
        if compare_by_pieces:
            return self._merge_two_files_by_buffer(filename_a, filename_b)
        else:
            return self._merge_two_files_by_line(filename_a, filename_b)

    def _merge_files(self, filename_array, compare_by_pieces=True): 
        # =========================================================
        # 
        progressbar_cur = 0
        progressbar_max = len(filename_array)
        progressbar_process = Progressbar(
                                description="Merge (buffering: {})".format(
                                                        compare_by_pieces))
        #
        # =========================================================
        while len(filename_array) > 1:
            filename_array.append(self._merge_two_files(filename_array[0],
                                                        filename_array[1],
                                                        compare_by_pieces))
            filename_array.pop(0); filename_array.pop(0)
            # =========================================================
            # 
            progressbar_cur += 1
            progressbar_process.update(progressbar_cur, progressbar_max)
            #
            # =========================================================
        # =========================================================
        # 
        progressbar_process.update(100)
        #
        # =========================================================
        if len(filename_array):
            return filename_array[0]
        return ""

    def _sort_file(self, in_filename, out_filename):
        #
        # divide
        filename_array = self._divide_file(in_filename)
        #
        # sort
        filename_array[0] = self._sort_small_files(filename_array[0])
        #
        # merge
        filename_array = [ self._merge_files(filename_array[key], bool(key))
                                                        for key in range(2) ]
        filename_array = [ i for i in filename_array if i ]
        filename_array = self._merge_files(filename_array)
        #
        if filename_array:
            os.rename(filename_array, out_filename)

    def _file_to_line(self, in_filename, out_file):
        in_file = self._read_from_file(in_filename, "\n")
        while True:
            data, wall = next(in_file)
            if not data and not wall:
                out_file.write("\n")
                return
            out_file.write(data)
            if data and wall == "\n":
                out_file.write(" ")

    def _line_to_file(self, in_file):
        temp_file = TempFile()
        #
        while True:
            data, wall = next(in_file)
            if not data and not wall:
                return temp_file.free()
            temp_file.push(data)
            if wall == " ":
                temp_file.push("\n")
            elif wall == "\n":
                return temp_file.free()

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
    
    finish = int(time.perf_counter())
    print("{}:{}".format((finish - start) // 60, (finish - start) % 60))
