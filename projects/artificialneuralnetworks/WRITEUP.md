# Project 6 - ANN
## Leonardo Ferrisi


The ANN designed for this project uses exactly 6 Nodes (+ 2 BIAS nodes)
to perform the XOR operation.

The ANN designed for this project uses 19 Nodes (+ 2 BIAS nodes) to perform 
Auto Association

# Description

The Neural Network uses backpropogration to adjust its weights and descent the gradient 

In the computing the error however, rather than calculting the square of the difference it stores a maximum error value and waits until the maximum error
value is less than the tolerance.

This allows the ANN to work for both datasets like the XOR input, or a larger dataset like the one for the Auto-Association.

### Backend

The ANN for this project uses a sigmoid function in each node to calculate how the node itself will handle an input from a previous connection.

The ANN learns using backpropogration with the quantitiy of epochs needed depending on the tolerance for error and the complexity of the 
inputs and outputs in needs to learn.

# Results

| Function | Tolerance | Learning Rate | TSS Error | Epochs Taken | Time | Speedup |
|----------|-----------|---------------|-----------|--------------|------|---------|
|   XOR    |   0.0001  |      0.2      | 0.0001    |     77819    |12.64 |    x    |
|   XOR    |   0.0001  |      0.3      | 0.0001    |     59036    |10.01 |   1.26  |
|   XOR    |   0.0001  |      0.4      | 0.0001    |     46510    | 7.83 |   1.28  |



*AA was not possible with even 500,000 cycles at a tolerance of 0.0001*


| Function | Tolerance | Learning Rate | TSS Error | Epochs Taken | Time |  Speedup |
|----------|-----------|---------------|-----------|--------------|------|----------|
|   XOR    |   0.001   |      0.2      | 0.0010    |     18559    |  2.84|     x    |
|   XOR    |   0.001   |      0.3      | 0.0010    |     12105    |  1.91|    1.49  |
|   XOR    |   0.001   |      0.4      | 0.0010    |     8358     |  1.2 |    1.59  |
|   AA     |   0.001   |      0.2      | 0.0010    |     41034    | 41.95|     x    |
|   AA     |   0.001   |      0.3      | 0.0010    |     23614    | 33.48|    1.25  | 
|   AA     |   0.001   |      0.4      | 0.0010    |     20185    | 44.4|     0.75  |

| Function | Tolerance | Learning Rate | TSS Error | Epochs Taken | Time | Speedup |
|----------|-----------|---------------|-----------|--------------|------|---------|
|   XOR    |   0.01    |      0.2      | 0.0100    |     10525    | 1.51 |    x    | 
|   XOR    |   0.01    |      0.3      | 0.0100    |     5433     | 1.11 |   1.36  |
|   XOR    |   0.01    |      0.4      | 0.0100    |     3688     | 0.58 |   1.91  |
|   AA     |   0.01    |      0.2      | 0.0100    |     5704     | 6.54 |    x    |
|   AA     |   0.01    |      0.3      | 0.0100    |     3729     | 4.12 |   1.58  |
|   AA     |   0.01    |      0.4      | 0.0100    |     4276     | 5.35 |   0.77  |

------------------------------

## ARTIFICIAL NEURAL NET STRUCTURE
- 1 Input Layer, 1 Hidden Layer, 1 Output Layer
- 2 BIAS nodes, one connected to hidden layer, one connection to output layr
- All connections between layers are represented by **Connection** objects which store their two and from connections and a weight.

## Functionality:
### FWD PROPAGATION
- Our starting input pattern is fed to the neural net as is, pattern is allowed to move or **propagate** through the neural network to see what the initial output generated is. 
*Weights at the start are randomly genereated but typically all around 0.5**

### BACKPROPAGATION
- The first step for backprop is forward propagation and calculating the error assocaited at each output node
- Error is calculated, a delta is calculated for the output nodes, and then each node before it.
    - **Where *delta* for output layer equals the dervative of the activation x error**
    - **Where *delta* for the preceeding layers equals the sum of derivatives and weights of its outgoing connections**
- After all deltas are calculated, the *increments* the amount to change each weight by are determined
- The weights are all adjusted according to these increments

### TRAINING THE NETWORK 
- Use backpropogation until the squared error is below a desired value
- Where each run is called an **EPOCH**, calculate error for each epoch
- Repeat over multople epochs of the training input data until the error between the resulting outputs and desired outputs is less than a tolerance value
