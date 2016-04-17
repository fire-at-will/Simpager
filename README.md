# Simpager
A simulator of various page replacement algorithms written by Will Taylor and James Stewart.

## Getting Started

Just download or clone this repository to your local machine!

### Prerequisities
All you need is a Python 2.7 installed on your system.

## Usage

You may use simpager with no extra arguments, like so: `python simpager.py`.

The program will then wait for user input. Input should be entered in this order:  


1. The page reference string. This string must be a series of integers separated by spaces.
2. The number of frames allocated to a process.
3. The mnemonics of the algorithms you want to test. Each algorithm is placed on its own line.

   Available mnemonics include:
      * FIFO: First in, first out  
      * LRU:  Least recently used  
      * LFU:  Least frequently used  
      * OPT:  Optimal  
      * RAND: Random  
      * MFU:  Most frequently used  
      * MRU:  Most recently used  
      
4. A blank line, used to denote the end of user input.

You may also redirect input from a text file, like so: `python simpager.py < sampleInput.txt`. In this case no other user input is necessary.


## Authors

* **Will Taylor** - [Will Taylor](https://github.com/fire-at-will)
* **James Stewart** - [James Stewart](https://github.com/stewratking)
