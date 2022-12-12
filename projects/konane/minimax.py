from updatedKonane import *
import pdb
import math
import sys
import time
from alarm import *


# LEONARDO FERRISI MINIMAX.PY

# Algorithm for Konane Minimax Algorithm:
# Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle River, New Jersey: Prentice Hall, ISBN 0-13-790395-2
#
# Static Evalution Inspiration from:
#  Thompson, D. (2005). Teaching a Neural Network to Play Konane. Undergraduate Thesis, Bryn Mawr College, Bryn Mawr PA (USA).


class MinimaxNode:
    """
    Black always goes first and is considered the maximizer.
    White always goes second and is considered the minimizer.
    """

    def __init__(self, state, player, depth, operator, value=0):
        """
        state: board represented by list
        player: string representing this player
        depth: the depth of the node in the search tree
        operator: the move that resulted in the current board configuration
        staticEval: the value stored in each node representing the 'state' or 'score' of a configuration. Starts at 0
        """
        self.state = state
        self.player = player
        self.depth = depth
        self.operator = operator
        self.staticEval = value

    def __str__(self):
        result = f"State: {str(self.state)},\n"
        result += f"Depth: {str(self.depth)},\n"
        result += f"Player: {str(self.player)},\n"
        result += f"Operator: {str(self.operator)}\n\n"
        return result

    def staticEvaluation(self, value):
        self.staticEval = value

    def getDepth(self):
        return self.depth

    def getPlayer(self):
        return self.player

    def getBoard(self):
        return self.state

    def getEval(self):
        return self.staticEval


class MinimaxPlayer(Konane, Player):

    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.size = size
        self.limit = depthLimit
        self.bestMove = None
        self.wins = 0
        self.losses = 0

    def initialize(self, side):
        """
        Initializes the player's color and name.
        """
        self.side = side
        self.name = "MinimaxDepth" + str(self.limit) + "FoisGras"
        self.currentMov = []

    # From updatedKonane ==============================================

    def generateMoves(self, board, player):
        """
        Generates and returns all legal moves for the given player
        using the current board configuration.
        """
        return super().generateMoves(board, player)

    def nextBoard(self, board, player, move):
        """
        Given a move for a particular player from (r1,c1) to (r2,c2) this
        executes the move on a copy of the current konane board.  It will
        raise a KonaneError if the move is invalid. It returns the copy of
        the board, and does not change the given board.
        """
        return super().nextBoard(board, player, move)

    def opponent(self, player):
        """
        Given a player symbol, returns the opponent's symbol, 'B' for black,
        or 'W' for white.
        """
        return super().opponent(player)

    # ==================================================================

    @timed_out(3)  # Such that we make a random move if timedout
    def getMove(self, board):
        """
        Returns the chosen move based on doing an alphaBetaMinimax
            search.
        """
        self.bestMove = []

        currentNode = MinimaxNode(state=board, player=self.side, depth=0, operator=[])
        self.alphaBetaMinimax(node=currentNode, alpha=-math.inf,
                              beta=math.inf)  # self.best move should be altered as we go through

        # if len(self.successors(current)) == 0:
        #     return []
        # # if self.bestMove == []:
        # #     return []

        return self.bestMove

    def staticEval(self, node: MinimaxNode):
        """
        Returns an estimate of the value of the state associated
        with the given node.
        """
        p1 = self.side
        p2 = self.opponent(p1)
        myMoves = self.generateMoves(node.getBoard(), p1)
        theirMoves = self.generateMoves(node.getBoard(), p2)

        if len(theirMoves) != 0:
            evaluation = len(myMoves) / (len(theirMoves))
            return evaluation
        else:
            return len(myMoves)

    def isValid(self, row, col):
        """
        Borrowed from Konane class, validates a move
        """
        return row >= 0 and col >= 0 and row < self.size and col < self.size

    def successors(self, node: MinimaxNode):
        """
        Returns a list of the successor nodes for the given node.
        """
        children = []
        depth = node.getDepth() + 1
        nextMoves = self.generateMoves(node.getBoard(), node.getPlayer())
        if len(nextMoves) == 0:
            return []
        else:
            for move in nextMoves:
                player = node.getPlayer()
                opponent = self.opponent(player)
                childBoard = self.nextBoard(node.getBoard(), player, move)
                child = MinimaxNode(state=childBoard, operator=move, depth=depth, player=opponent)
                score = self.staticEval(child)
                child.staticEvaluation(score)
                children.append(child)
        return children

    # AB minimax with pruning, as inspired by textbook

    def getMax(self, node: MinimaxNode, alpha, beta):
        """
        Gets the maximum value from children nodes
        """
        assert type(node) == MinimaxNode
        if (node.getDepth() > self.limit):  # Terminal Case
            return node.getEval()

        children = self.successors(node)

        if children == [] or len(children) == 0:  # indicates a winning state may have been hit
            return node.getEval()

        maxVal = -math.inf

        for child in children:
            assert type(child) == MinimaxNode

            returnValue = self.getMin(child, alpha, beta)

            if returnValue > maxVal:
                maxVal = returnValue
                if node.getDepth() == 0:
                    self.bestMove = child.operator
            
            alpha = max(alpha, maxVal)
                
            # maxVal = max(maxVal, returnValue)
            if beta <= alpha:
                break # PRUNE
            # if maxVal >= beta:
            #     return maxVal

        return maxVal

    def getMin(self, node: MinimaxNode, alpha, beta):
        """
        Gets the minimum value from children nodes
        """
        assert type(node) == MinimaxNode # Should be minimax node

        if (node.getDepth() > self.limit):  # Terminal Case
            return node.getEval()

        children = self.successors(node)

        if children == [] or len(children) == 0:  # indicates a winning state may have been hit
            return node.getEval()

        minVal = math.inf
        # Search Children
        for child in children:
            returnValue = self.getMax(child, alpha, beta)
            minVal = min(minVal, returnValue)
            beta = min(beta, minVal)
            if beta <= alpha:
                break # PRUNE
        return minVal

    def alphaBetaMinimax(self, node: MinimaxNode, alpha=-math.inf, beta=math.inf):
        """
        Returns the best score for the player associated with the
        given node.

        Also sets the instance variable bestMove to the
            move associated with the best score at the root node.

        Initialize alpha to -infinity and beta to +infinity.
        """
        bestValue = self.getMax(node, alpha, beta)
        return bestValue


if __name__ == "__main__":
    BOARD_SIZE = 10
    # game = Konane(BOARD_SIZE)
    # game.playNGames(200, MinimaxPlayer(BOARD_SIZE, 100), SimplePlayer(BOARD_SIZE), False)

    game = Konane(BOARD_SIZE)
    # breakpoint()
    t1 = time.time()
    # game.playNGames(10, MinimaxPlayer(BOARD_SIZE, 4), RandomPlayer(BOARD_SIZE), False)
    game.playNGames(10, MinimaxPlayer(BOARD_SIZE, 4), SimplePlayer(BOARD_SIZE), False)



    p1 = MinimaxPlayer(BOARD_SIZE, 3)
    p1.name = "FoisGras"
    p2 = MinimaxPlayer(BOARD_SIZE, 3)
    p2.name = "GrasFois"
    # game.playNGames(10, MinimaxPlayer(BOARD_SIZE, 3), MinimaxPlayer(BOARD_SIZE, 2), False)

    t2 = time.time()
    timeElapsed = t2 - t1
    print(f"Time Elapsed: {round(timeElapsed, 2)}")