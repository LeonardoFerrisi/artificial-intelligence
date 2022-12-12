### File: missionary.py
# Implements the borg problem for state
# space search

from search import *
from improvedSearch import *


class BorgState(ProblemState):
    """
    The Borg Problem:

        - Exactly Three (3) Members of the Federation and of Three (3) Borg find themselves isolated on a strange planet, and despite being enemies, 
          have reached a temporary truce so they can return back to their ships.  However, there is a river in the way, along with a boat that can hold 
          either one or two people. 

        - There can never be a group of humans on either of the river outnumbered by the Borg

    Each operator returns a new instance of this class representing
    the successor state.  
    """

    def __init__(self, crew, borgs, boatIsLeft, operator=None, verbose=False):
        self.crew = crew
        self.borgs = borgs

        if boatIsLeft == 0:
            self.isLeft = True
        else:
            self.isLeft = False

        self.currentState = (self.crew, self.borgs, boatIsLeft)
        self.operator = operator
        self.verbose = verbose

    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        result = ""
        if self.operator is not None:
            result += "Operator: " + self.operator + "\n"
        result += str(self.crew) + "," + str(self.borgs) + \
            "," + str(self.currentState[2])
        return result

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.crew == state.crew and self.borgs == state.borgs and self.isLeft == state.isLeft

    def dictkey(self):
        """
        Required method for use with the Search class.
        Returns a string that can be used as a ditionary key to
        represent unique states.
        """
        return str(self.crew) + "," + str(self.borgs) + "," + str(self.currentState[2])

    def movCrew(self):
        """
        If there are any Crew left, mov 'em to the other side of the river 
        """
        if self.isLeft and self.crew >= 1:
            newState = BorgState(self.crew - 1, self.borgs,
                                 boatIsLeft=1, operator="movCrewwmate")
            if (newState.isIllegal() == False):
                return newState
        else:
            if self.crew < 3:
                newState = BorgState(
                    self.crew + 1, self.borgs, boatIsLeft=0, operator="movCrewwmate")
                if (newState.isIllegal == False):
                    return newState
        return 0

    def mov2Crew(self):
        """
        If there are 2 crew left on boat side, move 'em to the other side of the river 
        """
        if self.isLeft and self.crew > 1:
            newState = BorgState(self.crew - 2, self.borgs,
                                 boatIsLeft=1, operator="mov2Crewwmates (C)")
            if (newState.isIllegal() == False):
                return newState
        else:
            if self.crew < 2:
                newState = BorgState(
                    self.crew + 2, self.borgs, boatIsLeft=0, operator="mov2Crewwmates (CC)")
                if (newState.isIllegal == False):
                    return newState
        return 0

    def movBorg(self):
        """
        If there are any Borgs on boat side, mov 'em to the other side of the river
        """

        if self.isLeft and self.borgs >= 1:
            newState = BorgState(self.crew, self.borgs - 1,
                                 boatIsLeft=1, operator="movBorg (B)")
            if (newState.isIllegal() == False):
                return newState
        else:
            if self.borgs < 3:
                newState = BorgState(
                    self.crew, self.borgs + 1, boatIsLeft=0, operator="movBorg (B)")
                if (newState.isIllegal() == False):
                    return newState
        return 0

    def mov2Borg(self):
        """
        If there are any Borgs on boat side, mov 'em to the other side of the river
        """

        if self.isLeft and self.borgs > 1:
            newState = BorgState(self.crew, self.borgs - 2,
                                 boatIsLeft=1, operator="mov2Borgs (BB)")
            if (newState.isIllegal() == False):
                return newState
        else:
            if self.borgs < 2:
                newState = BorgState(
                    self.crew, self.borgs + 2, boatIsLeft=0, operator="mov2Borgs (BB)")
                if (newState.isIllegal() == False):
                    return newState
        return 0

    def mov1Crew1Borg(self):
        """
        Moves both at the same time
        """
        if self.isLeft and self.crew >= 1 and self.borgs >= 1:
            newState = BorgState(self.crew - 1, self.borgs - 1,
                                 boatIsLeft=1, operator="mov1Crew1Borg (CB)")
            if (newState.isIllegal() == False):
                return newState
        else:
            if self.crew < 3 and self.borgs < 3:
                newState = BorgState(
                    self.crew + 1, self.borgs + 1, boatIsLeft=0, operator="mov1Crew1Borg (CB)")
                if (newState.isIllegal == False):
                    return newState
        return 0

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of valid successors to the current state
        """
        possibleOperators = [self.movCrew(), self.movBorg(
        ), self.mov2Crew(), self.mov2Borg(), self.mov1Crew1Borg()]
        legalOperators = []
        for operator in possibleOperators:
            if self.verbose:
                print(f"Operator result: {operator}")
            if operator != 0:
                legalOperators.append(operator)
        if self.verbose:
            print(f"Legal Operators Length {len(legalOperators)}")
        return legalOperators

    def isIllegal(self):
        crewmates = self.currentState[0]
        borgs = self.currentState[1]

        if crewmates != 3 and crewmates != 0:  # Cannot be illegal if 3 on one side
            if (crewmates < borgs):
                if self.verbose:
                    print(f"{self.currentState}... Yep that's illegal")
                return True
            else:
                if self.verbose:
                    print("All clear mate!")
                return False
        return False


if __name__ == "__main__":

    print("Initial Search:\n")
    startTime = time.time()
    Search(BorgState(3, 3, 0), BorgState(0, 0, 1), verbose=False)
    timeElapsedSearch = round(time.time() - startTime, 8)
    print(f"(( TIME ELAPSED: {timeElapsedSearch}))")
    print("\n==========================\n")
    print("Improved Search:\n")
    startTime = time.time()
    improvedSearch(BorgState(3, 3, 0), BorgState(0, 0, 1), verbose=False)
    timeElapsedImprovedSearch = round(time.time() - startTime, 8)
    print(f"(( TIME ELAPSED: {timeElapsedImprovedSearch}))")
    print(
        f"\n\nImproved search was {round(timeElapsedSearch - timeElapsedImprovedSearch, 8)} seconds faster than Initial Search")
