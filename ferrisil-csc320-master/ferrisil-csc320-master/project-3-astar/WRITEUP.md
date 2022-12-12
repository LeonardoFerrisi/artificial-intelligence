# Leonardo Ferrisi - PROJECT 3:: A* 

##### Node Expansions
| Problem  |  A*(dist) |   A*(tiles) |
|----------|------------|------------|
|A         |      3     |      3     |
|B         |      6     |      7     |
|C         |      8     |      10     |
|D         |      159     |     599      |
|E         |      73    |      257    |
|F         |      15    |      56    |
|G         |      39    |      190    |
|H         |      118    |      1193    |


All in all the manhattan distance based A* heuristic yielded 
substatiantially smaller amounts of node expansions in comparison to the
tile displacement based heuristic.

This is likely because the manhattan distance model does a better job at making
an educated guess of the better resulting state given legal moves in comparison to one which doesnt consider how close something is to the state, just its whether tiles are or are not in the goal position. 

Because of the way the distance method searchers through states, it finds states that are closer to the goal, faster than analyzing misplaced tiles can.
