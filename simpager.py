##################################################
#
#                  Imports
#
##################################################
import sys
import os

from fifo import *
from lru import *
from lfu import *
from opt import *
from rand import *
from mfu import *
#from mru import *


##################################################
#
#               Main Function
#
##################################################
def main():

    r = os.pipe()
    r = os.fdopen(r)
    str = r.read()
    print str

    # for line in sys.stdin:
    #     sys.stdout.write(line)

    # for arg in sys.argv[1:]:
    #     print arg

# Execute main function
if __name__ == "__main__": main()
