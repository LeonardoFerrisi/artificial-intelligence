# Implementing Back-Propagation

The goal of this project is to implement back propagation, as explained in lectures and in the assigned reading.  You'll have a "deeper" appreciation of learning after completeing this assignment!

## Targets

L.2.A	Neural Networks
L.2.P	Neural Networks

## Steps
Take some time to read and understand the starting point code. It uses three classes: Unit,Connection, and Network. You will need to complete several methods of the Network class that are involved in:


* forward propagating activation
* teaching the network a pattern by backward propagating error
* computing error during training


Follow the comments provided in the file when implementing these methods. Feel free to create additional methods within the other classes in order to complete the Network class.

**make small changes to the code and test reguarly!!**

Even if you are precocious you may not use any numpy vector-based methods for this.  (I want you to do things the hard way for now).

Your completed code should be able to successfully learn the two examples provided at the end of the file. The XOR problem may take several thousand iterations to find a solution (and in some cases, it may even fail after 10,000 iterations). If you'd like to improve learning speed, read about how to include momentum in the back-propagation algorithm.


## Common Mistakes


* The activations of units in the input layer should simply be the values in the input pattern. The sigmoid function should NOT be applied to input unit activations.

* Be sure that the bias unit is contributing to the net input of the units in the hidden and output layers. If you loop over all incoming connections to a unit, you will automatically get the connection from the bias unit.

* Calculate all of the weight increments throughout the entire network before modifying any of the weights. If you modify weights as you go, you will not be able to calculate the correct values for back-propagation of error.

## Challenges:

* Re-do the assignment with numpy, and provide a quantitative analysis of the speedup.
* learn a new problem with a two-layer network
* implement a  multi-layer network

## Submit:
* add/commit/push all your code
* a short `Writeup.md` explaining results, and providing some quantitative analysis of how the system works.
