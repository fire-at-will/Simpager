##################################################
#
#                  Imports
#
##################################################
import sys
import os
import fileinput

from fifo import *
from lru import *
from lfu import *
from opt import *
from rand import *
from mfu import *
from mru import *
from constants import *

##################################################
#
#               Global Variables
#
##################################################

# global variables
algorithms = []
frames = 0
page_array = []


##################################################
#
#               Main Function
#
##################################################
def main():
    algorithms = []

    count = 0

    while True:
        try:
            line = raw_input("")
        except EOFError:
            break;
        else:
            if line == "":
                break;
            # Process input
            if count == 0:
                page_array = line.split(' ')
            elif count == 1:
                frames = int(line)
            else:
                algorithms.append(line)
            count = count + 1

    printVals(page_array, frames, algorithms)


def printVals(page_array, frames, algorithms):
    page_string = "Page Reference String:\n"
    for page in page_array:
        page_string = page_string + page + " "
    print page_string
    print "Number of Frames: " + str(frames)

    for alg in algorithms:
        if alg == "FIFO":
            fifo(page_array, frames)
        elif alg == "LRU":
            lru(page_array, frames)
        elif alg == "LFU":
            lfu(page_array, frames)
        elif alg == "OPT":
            opt(page_array, frames)
        elif alg == "RAND":
            rand(page_array, frames)
        elif alg == "MFU":
            mfu(page_array, frames)
        elif alg == "MRU":
            mru(page_array, frames)



# Execute main function
if __name__ == "__main__": main()
