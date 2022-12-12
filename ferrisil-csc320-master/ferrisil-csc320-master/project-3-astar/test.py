from eight_puzzle import *
from informedSearch import *
from pdb import *

# Test all required Scenarios

# A
aState = EightPuzzle(
    stateRep=[" ", "1", "3", "8", "2", "4", "7", "6", "5"], verbose=False)

# B
bState = EightPuzzle(stateRep=["1", "3", "4", "8", "6", "2", " ", "7", "5"])

# C
cState = EightPuzzle(stateRep=["1", "3", " ", "4", "2", "5", "8", "7", "6"])

# D
dState = EightPuzzle(stateRep=["7", "1", "2", "8", " ", "3", "6", "5", "4"])

# E
eState = EightPuzzle(stateRep=["8", "1", "2", "7", " ", "4", "6", "5", "3"])

# F
fState = EightPuzzle(stateRep=["2", "6", "3", "4", " ", "5", "1", "8", "7"])

# G
gState = EightPuzzle(stateRep=["7", "3", "4", "6", "1", "5", "8", " ", "2"])

# H
hState = EightPuzzle(stateRep=["7", "4", "5", "6", " ", "3", "8", "1", "2"])

# GOAL STATE
goal = EightPuzzle(stateRep=["1", "2", "3", "8", " ", "4", "7", "6", "5"])
# goalB = EightPuzzle(stateRep=["1", "2", "3", " ", "8", "4", s"7", "6", "5"])


# BEGIN EVALUTATION
VERBOSE = True
DEFAULT = False

print("\nA========================================\n")

# searchA = InformedSearch(
#     initialState=aState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchA.execute()

# print("\nB========================================\n")

# searchB = InformedSearch(
#     initialState=bState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchB.execute()

# print("\nC========================================\n")

# searchC = InformedSearch(
#     initialState=cState, goalState=goal, verbose=VERBOSE, default=True)
# searchC.execute()

# print("\nD========================================\n")

# searchD = InformedSearch(
#     initialState=dState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchD.execute()

# print("\nE========================================\n")

# searchE = InformedSearch(
#     initialState=eState, goalState=goal, verbose=VERBOSE, default=True)
# searchE.execute()

# print("\nF========================================\n")

# searchF = InformedSearch(
#     initialState=fState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchF.execute()

# print("\nG========================================\n")

# searchG = InformedSearch(
#     initialState=gState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchG.execute()

# print("\nH========================================\n")

# searchH = InformedSearch(
#     initialState=hState, goalState=goal, verbose=VERBOSE, default=DEFAULT)
# searchH.execute()
