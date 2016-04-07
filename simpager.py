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


##################################################
#
#               Main Function
#
##################################################
def main():
    print "hello"

    if len(sys.argv) == 2:
        for line in sys.stdin:
            #store variables
    else:
        print "READ IN"
        while(True):
            line = raw_input()
            if line == "":
                break
            print line


# Execute main function
if __name__ == "__main__": main()
