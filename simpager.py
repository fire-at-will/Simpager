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


    print page_array
    print frames
    print algorithms

# Execute main function
if __name__ == "__main__": main()
