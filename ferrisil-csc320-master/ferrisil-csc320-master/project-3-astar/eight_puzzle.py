from requests import TooManyRedirects
from informedSearch import *


class EightPuzzle(InformedProblemState):
    """
    Implement this
    """

    def __init__(self, stateRep, operator=None, verbose=False):
        self.state = stateRep
        self.operator = operator
        self.verbose = verbose
        self.LENGTH = len(self.state)

    def applyOperators(self):
        """
        Returns a list of legal successors to the current state.
        """
        possibleOperators = [self.up(), self.down(), self.left(), self.right()]
        legalOperators = []
        for operator in possibleOperators:

            if operator != None:

                legalOperators.append(operator)
        if self.verbose:
            # print(f"Operator result: {operator}")
            print(
                f"up: {self.up()}, down:{self.down()}, left:{self.left()}, right:{self.right()} ")
            print(f"Legal Operators Length {len(legalOperators)}")
        return legalOperators

    def equals(self, otherState: InformedProblemState):
        """
        Tests whether the state instance equals the given state.
        """
        if (len(self.state) != len(otherState.state)):
            return False

        for i in range(len(otherState.state)):
            if self.state[i] != otherState.state[i]:
                return False
        return True

    def dictkey(self):
        """
        Returns a string that can be used as a dictionary key to
        represent the unique state.
        """
        return str(self.dict())

    def heuristic(self, goalState: InformedProblemState, default: bool = True):
        """
        Gets the (manhattan) distance between ourItem's coordinates in our state and the goal state
        """
        if default:
            return self.__sumOfDistances(goalState)
        else:
            return self.__numOuttaPlace(goalState)

    # OPERATORS

    def __swap(self, index1, index2):
        """Swaps the locations of two items in state

        Returns:
            list: The modified state with swap
        """

        swp = self.state[:]

        holder1 = swp[index1]
        holder2 = swp[index2]

        swp[index1] = holder2
        swp[index2] = holder1

        return swp

    def up(self):
        """If possible, swaps the blank space with the space above it

        Returns:
            EightPuzzle: The next state with the operator applied, if possible
                         otherwise; None
        """
        blnkIdx = self.__locateBlank()

        if blnkIdx > 2:
            newGrid = self.__swap(blnkIdx, blnkIdx-3)
            nextState = EightPuzzle(stateRep=newGrid, operator="up")
        else:
            nextState = None
        return nextState

    def down(self):
        """If possible, swaps the blank space with the space below it

        Returns:
            EightPuzzle: The next state with the operator applied, if possible
                         otherwise; None
        """
        blnkIdx = self.__locateBlank()

        if blnkIdx < 5:
            newGrid = self.__swap(blnkIdx, blnkIdx+3)
            nextState = EightPuzzle(stateRep=newGrid, operator="down")
            nextState.isLegal = True
        else:
            nextState = None
        return nextState

    def left(self):
        """If possible, swaps the blank space with the space to its left

        Returns:
            EightPuzzle: The next state with the operator applied, if possible
                         otherwise; None
        """
        blnkIdx = self.__locateBlank()
        illegalIndicies = [0, 3, 6]
        if blnkIdx not in illegalIndicies:
            newGrid = self.__swap(blnkIdx, blnkIdx-1)
            nextState = EightPuzzle(stateRep=newGrid, operator="left")
            nextState.isLegal = True
        else:
            nextState = None
        return nextState

    def right(self):
        """If possible, swaps the blank space with the space to its right

        Returns:
            EightPuzzle: The next state with the operator applied, if possible
                         otherwise; None
        """
        blnkIdx = self.__locateBlank()
        illegalIndicies = [2, 5, 8]
        if blnkIdx not in illegalIndicies:
            newGrid = self.__swap(blnkIdx, blnkIdx+1)
            nextState = EightPuzzle(stateRep=newGrid, operator="right")
            nextState.isLegal = True
        else:
            nextState = None
        return nextState

    def dict(self):
        """ Generates a dictionary containing all items and their locations 
            in the list representing the state

        Returns:
            dict: Dictionary representation of this 8puzzle
        """
        dictState = {}

        for index in range(len(self.state)):
            item = self.state[index]
            dictState[item] = index

        return dictState

    def showGrid(self):
        toReturn = ""
        for index in range(self.LENGTH):
            if index == 0:
                toReturn += self.state[index]+", "
            elif index == 2 or index == 5 or index == 8:
                toReturn += self.state[index] + "\n"
            else:
                toReturn += self.state[index] + ", "
        return toReturn

    def __coords(self, item):
        """ Coordinates are represented the terms of a 9 tile grid.

            0, 1, 2
            3, 4, 5
            6, 7, 8

            With respect, the top left corner is 0, 0
            The bottom row is y=2, the top is y=0
            The leftmost column is x=0, the rightmost is x=2

        Args:
            item (string): The item we are searching for the coordinates of

        Returns:
            tuple: x, y coordinates of item if present, else returns (None, None)
        """
        index = self.dict()[item]
        # print(f"{item}, {index}")
        if index < 3:
            y = 0
            x = index
        elif 2 < index < 6:
            y = 1
            x = index - 3
        else:
            y = 2
            x = index - 6
        # print(f"Current x: {x}, y: {y}")
        return (x, y)

    def __locateItem(self, item):
        """Locates a string item in the grid and returns its index,
        return -1 if not present

        Returns:
            int: The index of the item we are searching for, if present.
                 Otherwise returns -1
        """
        index = -1

        state = self.state
        for i in range(len(state)):
            if state[i] == item:
                index = i
                # print(f"BLANK at index {index}")
        return index

    def __locateBlank(self):
        """ Locates a blank in the grid and returns its index,
            return -1 if not present

        Returns:
            int: the index of the blank in the state
        """
        return self.__locateItem(" ")

    def __getDistance(self, goalState: InformedProblemState, item):
        """
        Gets the distance between ourItem's coordinates in our state and the goal state
        """
        Xdiff = abs(self.__coords(item)[0] - goalState.__coords(item)[0])
        Ydiff = abs(self.__coords(item)[1] - goalState.__coords(item)[1])

        # print(f"Xdiff is: {Xdiff}, YDiff is {Ydiff}")
        totalDiff = Xdiff + Ydiff
        return totalDiff

    def __sumOfDistances(self, goalState: InformedProblemState):
        """
        Gets the sum of all distances between our tiles and goal tile positions.
        Gets the sum of manhattan distances 
        """
        totalDistance = 0

        for item in self.state:
            if item != " ":
                dist = self.__getDistance(goalState, item)
                # print(f"item: '{item}', dist: {dist}")
                totalDistance += dist
            else:  # WE DO NOT WANT TO INCLUDE BLANK
                continue

        return totalDistance

    def __numOuttaPlace(self, goalState: InformedProblemState):
        """
        Alternative Heuristic where we just count the number of tiles out of place 
        in comparison to the goalstate
        """

        numOutOfPlace = 0
        # print("IN NUM OUTTA PLACE")

        for i in range(self.LENGTH):
            item = self.state[i]
            if item != " ":
                if item != goalState.state[i]:
                    numOutOfPlace += 1
            else:
                continue

        return numOutOfPlace


if __name__ == "__main__":

    aState = EightPuzzle(
        stateRep=[" ", "1", "3", "8", "2", "4", "7", "6", "5"], verbose=True)
    goal = EightPuzzle(stateRep=["1", "2", "3", "8", " ", "4", "7", "6", "5"])

    # searcher = InformedSearch(initialState=initState, goalState=goalState, verbose=False)

    print(aState.heuristic(goal))
    # searcher.execute()

    print(aState.heuristic(goal, default=True))
