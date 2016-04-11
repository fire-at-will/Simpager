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

    if len(sys.argv) == 2:
        count = 0

        #read file specs into variables
        for line in sys.stdin:
            #store variables
            if count == 0:
                page_array = line.split(' ')
            elif count == 1:
                frames = int(line)
            else:
                algorithms[count-2] = line
            count = count + 1
    else:
        count = 0
        while(True):
            line = raw_input()

            #check for last input
            if line == "":
                break

            #store variables
            if count == 0:
                page_array = line.split(' ')
            elif count == 1:
                frames = int(line)
            else:
                algorithms.append(line) #IndexError: list assignment index out of range
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
            # Not sure about this yet
            rand(page_array, frames)
        elif alg == "MFU":
            mfu(page_array, frames)
        elif alg == "MRU":
            mru(page_array, frames)



# Execute main function
if __name__ == "__main__": main()
