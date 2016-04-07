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

    # r = os.pipe()
    # r = os.fdopen(r)
    # str = r.read()
    # print str
    if len(sys.argv) == 2:
        print "FILE"
        for line in sys.stdin:
            sys.stdout.write(line)
    else:
        print "READ IN"
        while(True):
            line = raw_input()
            if line == "":
                break
            print line

    # for arg in sys.argv[1:]:
    #     print arg

# Execute main function
if __name__ == "__main__": main()
