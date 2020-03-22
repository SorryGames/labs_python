import argparse
from sqrt import SqrtDecomposition
from checker import Checker


def init_parser():
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

def main():
    args = init_parser()
    
    print(args)
    if args.auto:
        checker = Checker(args.count_test, args.size_array, args.output)
        checker.generate()


main()

