from pq import *
from search import *
import time
import pdb


class InformedProblemState(ProblemState):
    """
    Implement this.
    """

    def heuristic(self, goalState):
        """
        takes the goal state as a 
        parameter and returns the estimate 
        of the distance from the current 
        state to the goal state.

        Args:
            goalState (InformedProblemState): The goal problem state
        """
        abstract()


class InformedNode(Node):
    """
    A Node class to be used in combination with state space search.  A
    node contains a state, a parent node, and the depth of the node in
    the search tree.  The root node should be at depth 0.
    """

    def __init__(self, state: InformedProblemState, parent, depth, goalState: InformedProblemState, default=True):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.goalState = goalState
        self.default = default

    def __str__(self):
        result = "\nState: " + str(self.state)
        result += "\nDepth: " + str(self.depth)
        if self.parent != None:
            result += "\nParent: " + str(self.parent.state)
        return result

    def priority(self):
        """ Calculates the F - Score value for A*. 
            Where F = H(euristic) + G(depth)

            Returns:
                int: The F-score value 
        """
        g = self.depth
        h = self.state.heuristic(self.goalState, default=self.default)
        # print(f"G is {g}, H is {h}, so priority is {g+h}")
        fScore = g + h
        return fScore


class InformedSearch(Search):
    """
    Implement this.
    """

    def __init__(self, initialState: InformedProblemState, goalState: InformedProblemState, verbose=False, default=True):
        self.uniqueStates = {}
        self.uniqueStates[initialState.dictkey()] = True
        self.pq = PriorityQueue()
        self.default = default
        self.pq.enqueue(InformedNode(initialState, None, 0,
                        goalState, default=self.default))
        self.goalState = goalState
        self.verbose = verbose

        self.solved = False
        solution = self.execute()

        if solution == None:
            print("Search failed")
        else:
            self.showPath(solution)
            self.solved = True

    def execute(self):
        """
        Searches for goal state, returns the solution, or None if no solution is available

        """
        # pdb.set_trace()

        while not self.pq.empty() and self.solved != True:
            current = self.pq.dequeue()
            # Where current.state is the EIGHTPUZZLE state not its internal list
            if self.goalState.equals(current.state):
                return current  # WHERE WE EQUAL THE GOAL
            else:
                successors = current.state.applyOperators()

                for nextState in successors:

                    if nextState.dictkey() not in self.uniqueStates.keys():

                        iN = InformedNode(state=nextState, parent=current, depth=current.depth +
                                          1, goalState=self.goalState, default=self.default)
                        self.pq.enqueue(iN)
                        self.uniqueStates[nextState.dictkey()] = True
                if self.verbose:
                    print("Expanded:", current.state.dictkey() +
                          str(current.state.operator))
                    print("Number of successors:", len(successors))
                    print("Queue length:", self.pq.size())
                    print("Queue: ", str(self.pq))
                    print("-------------------------------")
            # time.sleep(1)
        return None

    def showPath(self, node: InformedNode):
        path = self.buildPath(node)
        stateNum = 1
        for current in path:
            # print("\n")
            print(f"State # {stateNum}")
            # print(current.state.showGrid())
            print(current.state.state)
            stateNum += 1
            # print("\n")
        print("Goal reached in", current.depth, "steps")

    def buildPath(self, node: InformedNode):
        """
        Beginning at the goal node, follow the parent links back
        to the start state.  Create a list of the states traveled
        through during the search from start to finish.
        """
        result = []
        while node != None:
            result.insert(0, node)
            node = node.parent
        return result
