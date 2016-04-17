####################################################################################################
#
# James Stewart and Will Taylor
# Operating Systems
# Project #4
#
# Due: Monday, April 18 11:59:59 pm
#
# This program utilizes a variety of different algorithms: FIFO, LFU, MFU, LRU, MRU, RAND, and OPT,
# by reading in an array of pages, and receiving a set frame size. Each algorithm is in its own
# file that is imported into simpager.py.
#
# Input: A string of page numbers delineated by spaces, a frame size, and a number of algorithms
#
# Output: The pages that were use, the frame size, and the number of page faults per each algorithm
#
####################################################################################################


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


####################################################################################################
#
#               Main Function
#
#           Purpose -
#           This function reads in the data from the file or standard in and puts that data into
#           global variables.
#
####################################################################################################
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

####################################################################################################
#
#               printVals Function
#
#       Purpose -
#       This function prints the output to the console and then calls the function
#       for the corresponding algorithm read in.
#
####################################################################################################

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
