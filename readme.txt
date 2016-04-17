//********************************************************************
//
// Will Taylor & James Stewart
// Operating Systems
// Project 4: Simulation of Page Replacement Strategies
// Due: April 18, 2016
// Language: Python
// Instructor: Dr. Michael C. Scherger
//
//********************************************************************

--- Description
Simpager simulates various page replacement algorithms that an OS might use.
The program allows you to simulate first in first out (FIFO), least recently used (LRU),
least frequently used (LFU), optimal (OPT), random (RAND), most frequently used (MFU),
and most recently used (MRU) algorithms.

--- Usage
You may use simpager with no extra arguments, like so:
  python simpager.py

The program will then wait for user input. Input should be entered in this order:
  1. The page reference string. This string must be a series of integers separated by spaces.
  2. The number of frames allocated to a process.
  3. The mnemonics of the algorithms you want to test. Each algorithm is placed on its own line.
     Available mnemonics include:
        - FIFO: First in, first out
        - LRU:  Least recently used
        - LFU:  Least frequently used
        - OPT:  Optimal
        - RAND: Random
        - MFU:  Most frequently used
        - MRU:  Most recently used
  4. A blank line, used to denote the end of user input.

You may also redirect input from a text file, like so:
  python simpager.py < sampleInput.txt

In this case no other user input is necessary.

--- Bugs:
There are currently no known bugs with our program.

--- Estimated Time:
~ 4-5 hours per person.
