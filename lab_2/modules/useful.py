# terminal special characters
class termcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Safety file opening
def open_file(filename, filemod, error_log=""): 
    try:
        return open(filename, filemod)
    except:
        print("{0}ERROR: {2}{1}".format(
                                    termcolor.FAIL,
                                    termcolor.ENDC,
                                    error_log))
        exit()