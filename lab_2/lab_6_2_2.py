#!/usr/bin/env python3

import argparse
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class FileGenerator:

    def __init__(self):
        pass

    def start(self):
        args = self.init_parser()
        symbol_store = [ chr(i) for i in range(ord('a'), ord('z')+1) ] \
                        + [ chr(i) for i in range(ord('A'), ord('Z')+1) ]
        try:
            cout = open(args.output, "w")
        except:
            print("{0}ERROR: Can't create output file!{1}".format(
                                                            bcolors.FAIL,
                                                            bcolors.ENDC))
        try:
            letter_mn, letter_mx = [ int(i) for i in word_length.split(",") ]
            word_mn, word_mx = [ int(i) for i in sentence_length.split(",") ]
        except:
            print("{0}ERROR: Check entered options!{1}".format(
                                                            bcolors.FAIL,
                                                            bcolors.ENDC))

        size = 0
        max_size = args.size * 1000 * 1000
        while True:
            cur_sentence = random.randint(word_mn, word_mx)
            for i 


    def init_parser(self):
        pr = argparse.ArgumentParser(
                            description="Use this module to generate "\
                            "output file with specified size. ")
        pr.add_argument("size", 
                            help="The size of output file in MB",
                            type=int)
        pr.add_argument("-k", "--word-length",
                            help="MIN | MAX length of word. Example: 10,100",
                            default="10,100",
                            type=str)
        pr.add_argument("-l", "--sentence-length", 
                            help="MIN | MAX words in sentence. Example: 3,10",
                            default="3,10",
                            type=str)
        pr.add_argument("-o", "--output", 
                            help="Specify output file.",
                            default="output.txt")
        return pr.parse_args()


task = FileGenerator()
task.start()