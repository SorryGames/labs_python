#!/usr/bin/env python3

import argparse
import random
from progressbar import Progressbar 
from useful_module import termcolor, open_file


class FileGenerator:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        self.symbol_store = [ chr(i) for i in range(ord('a'), ord('z')+1) ] \
                        + [ chr(i) for i in range(ord('A'), ord('Z')+1) ]
        #
        self.cout = open_file(args.output, "w", "Can't create output file!")
        try:
            generate_args = [ int(i) for i in args.word_length.split(",") ]\
                            + [ int(i) for i in args.sentence_length.split(",") ]
            if generate_args[0] > generate_args[1]\
                    or generate_args[2] > generate_args[3]:
                raise Exception
        except:
            print("{0}ERROR: Check entered options!{1}".format(
                                                            termcolor.FAIL,
                                                            termcolor.ENDC))
            exit()
        max_size = args.size * 1000 * 1000
        self.progressbar = Progressbar(description="Creating")
        self.generate_text(max_size, *generate_args)

    def generate_text(self, max_size, letter_mn, letter_mx, word_mn, word_mx):
        size = 0
        while True:
            cur_sentence = random.randint(word_mn, word_mx)
            for i in range(cur_sentence):
                cur_letters = random.randint(letter_mn, letter_mx)
                for j in range(cur_letters):
                    if size < max_size:
                        self.cout.write(random.choice(self.symbol_store))
                        size += 1
                if size < max_size:
                    self.cout.write(" ")
                    size += 1
            if size < max_size:
                self.cout.write("\n")
                size += 1
            self.progressbar.update(size, max_size)
            if size == max_size:
                return

    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="Use this module to generate "\
                            "output file with specified size. ")
        pr.add_argument("size", 
                            help="The size of output file in MB",
                            type=int)
        pr.add_argument("-k", "--word-length",
                            help="MIN,MAX length of word. Example: 10,100",
                            default="10,100",
                            type=str)
        pr.add_argument("-l", "--sentence-length", 
                            help="MIN,MAX words in sentence. Example: 3,10",
                            default="3,10",
                            type=str)
        pr.add_argument("-o", "--output", 
                            help="Specify output file.",
                            default="output.txt")
        return pr.parse_args()


if __name__ == "__main__":
    task = FileGenerator()
    task.start()