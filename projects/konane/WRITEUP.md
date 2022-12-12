# Konane Minimax Player
### Leonardo Ferrisi CSC 320, project 4

##### Algorithm for Konane Minimax Algorithm:
##### Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle River, New Jersey: Prentice Hall, ISBN 0-13-790395-2

##### Static Evalution Inspiration from:
#####  Thompson, D. (2005). Teaching a Neural Network to Play Konane. Undergraduate Thesis, Bryn Mawr College, Bryn Mawr PA (USA).


# =====================================================

My variation of the Konane Minimax Player utilize alpha beta minimax to play Konane. The algorithm is inspired by psuedocode regarding minimax for
Konane players in Russell and Norvig's Artifical Intelligence: A Modern Approach book.

The static evaluator is a weighted ratio of the number of remaining moves for my player versus the oponents. I took inspiration from the several
evaluation methods detailed in "Teaching a Neural Network to Play Konane" which provides a graph describing the usefullness of several Konane 
static evaluation techniques. 

In writing this up I considered using the difference between the number of pieces I have versus my oponents, however this ended up making the code run longer than prefered, even when attempted by only using the difference metric for the first half of the game and the weighted ratio for the second half.

I also implemented a randomizer that chooses randomly between minimax nodes of the same value.

I deterimined which features were most effective as a result of copious trial and error, eventually looping back to the fundamentals with Russel and Norvigs description of Alpha Beta Minimax.


### Revisions Pt 1: What went wrong ==========================================

##### Without ALPHA / BETA PRUNING 
| Opponent Type | Wins | Loss | maxDepth | Time Elapsed | Speedups |
|---------------|------|------|----------|--------------|----------|
|    Simple     |  5  |  5  |     1    |     2.29       |    x     |
|    Random     |  2   |  8  |     1    |     2.42      |    x     |
|    Simple     |  0   |  10  |     2    |     16.4     |    0.20  | 
|    Random     |  0   |  10  |     2    |     24.44    |    0.099  |
|    Simple     |  5   |  5   |     4    |     537.46  |    0.025 |
|    Random     |  4   |  6  |     4    |     759.11   |    0.023 |

##### With ALPHA / BETA PRUNING 
| Opponent Type | Wins | Loss | maxDepth | Time Elapsed | Speedups |
|---------------|------|------|----------|--------------|----------|
|    Simple     |  10  |  0  |     1    |     1.5       |    x     |
|    Random     |  8   |  2  |     1    |     2.01      |    x     |
|    Simple     |  0   |  10  |     2    |     7.64     |    0.20  | 
|    Random     |  0   |  10  |     2    |     10.94    |    0.18  |
|    Simple     |  0   |  10   |     4    |     126.88  |    0.060 |
|    Random     |  0   |  10  |     4    |     186.75   |    0.060 |


## Analysis

So obviously, a maxDepth of one does not give the minimax the proper ability to make an informed decision on the best possible next moves.

With Alpha Beta Pruning implemented, the speedups are marginially faster, and the wins are far more consistent. With many of the runs without
Alpha Beta Pruning, the loss was a result of timeout - however at times it was a natural win from the computer side.

With Alpha Beta pruning, despite the higher speeds of completion as well as high success rate, for whatever reason anything with a depth of 3 resulted in 
a near complete loss from the MinimaxPlayer.

Perhaps this has to do with the way minimax was implemented causing the player to make a less then optimal decision if there is an odd number of depth causing *it* to make a minimum scoring play instead of the other

**As it turned out, AB was not fixed and the timed_out clause needed to be put onto get move, because prior this wasnt using sig alarm at all**


### Revisions Pt 2: At last, AB Pruning functions and this thing knows what to do on timeout ==========================================

The Alpha Beta Pruning had been failing, mainly in the area of alphabetaminimax that handles MIN nodes, as well as a static evaluator that would help the opponent half the time if they happened to go first.

Some edits mainly to the pruning area as well as adjusting the static evaluator to look for the Minimax player side rather than the node's player allowed for more optimal and more consistent wins.

In addition, adding a timeout for 3 seconds for get move allows for a random move to be played if a move is taking to long rather than causing the game to crash if Minimax Player takes longer than 3 seconds to decide on its next move. 

| Opponent Type | Wins | Loss | maxDepth | Time Elapsed | Speedups (Slowdowns Rather) |
|---------------|------|------|----------|--------------|----------|
|    Simple     |  0  |  10  |     1    |      14.64 |    x     |
|    Random     |  0   |  10  |     1    |     22.88      |    x     |
|    Simple     |  0   |  10  |     2    |     50.32    |    0.29  | 
|    Random     |  0   |  10  |     2    |     108.72   |    0.21  |
|    Simple     |  0   |  10  |     3    |     274.89    |    0.18  | 
|    Random     |  1   |  9  |     3    |     607.94   |    0.18  |
|    Simple     |  0   |  10   |     4    |     751.43  |    0.36 |
|    Random     |  0   |  10  |     4    |     794.71   |    0.76 |
|    MinimaxPlayer (MaxDepth of 2)     |  4   |  6   |   3    |     616.7  |    x |


For the deeper depths, even with functioning Alpha Beta Pruning, there are many instances where the move takes longer than 3 seconds triggering a random move instead. Regardless, the AB minimax function is still able to function on time most of the time allowing a near 100% win rate with the exception of one game with Random at depth 3.

In terms of slow downs,  the slowdown between depth 3 and 4 is the least of a slowdown (only about 24% slower for Random, 64% slow down for Simple) whereas the slowdown for depths 1 to 2 or 2 to 3 are both about 80% slower.

When versing itself, the MinimaxPlayer as expected, scored roughly even with a 6 wins and 4 losses. (and the other 4 wins and 6 losses)




