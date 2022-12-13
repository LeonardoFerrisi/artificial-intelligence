import random
from unit import Unit
from connection import Connection
import time
from encoder import Encoder
import numpy as np

class Network:

    def __init__(self, numInputs, numHiddensA, numHiddensB, numOutputs, learningRate=0.3, tolerance=0.1):

        # create all layers
        self.outputLayer = self.generateLayer(
            numOutputs, namePrefix='outNode', type='output')
        
        self.hiddenLayer1 = self.generateLayer(
            numHiddensA, namePrefix='hidNodeA', type='hidden')
        self.hiddenLayer2 = self.generateLayer(
            numHiddensB, namePrefix='hidNodeB', type='hiddenB')

        self.inputLayer = self.generateLayer(
            numInputs, namePrefix='inNode', type='input')

        # Generate connection placeholders
        self.synapseA = []
        self.synapseB = []
        self.synapseC = []
        self.synapses = [self.synapseA, self.synapseB, self.synapseC]

        # wire up the network
        self.connectLayers(self.inputLayer, self.hiddenLayer1, 'SA')
        self.connectLayers(self.hiddenLayer1, self.hiddenLayer2, 'SB') # new layer added
        self.connectLayers(self.hiddenLayer2, self.outputLayer, 'SC')

        # Add bias units
        self.outputBias = Unit(activation=1.0, name='outputBIAS')
        self.connectUnitToLayer(self.outputBias, self.outputLayer, 3, 'SBB')
        self.hiddenBias = Unit(activation=1.0, name='hiddenBIAS1')
        self.connectUnitToLayer(self.hiddenBias, self.hiddenLayer1, 1, 'SAB1')

        # >>
        self.hiddenBias2 = Unit(activation=1.0, name='hiddenBIAS2')
        self.connectUnitToLayer(self.hiddenBias2, self.hiddenLayer2, 2, 'SAB2')
        # <<

        # learning parameters
        self.learningRate = learningRate
        self.tolerance = tolerance

    def generateLayer(self, size: int, namePrefix: str = 'node', type='input'):
        """
        Generates a layer and names all of the nodes
        """
        layer = []
        for i in range(size):
            node = Unit(name=str(namePrefix+"_"+str(i)), type=type)
            layer.append(node)
        return layer

    def connectUnitToLayer(self, node: Unit, layer: list, synapseID: int, namePrefix):
        """
        Connects a single unit to every unit in the provided layer
        """
        for i in range(len(layer)):
            subUnit = layer[i]
            c = Connection(node, subUnit, name=str(namePrefix)+"_"+str(i))
            node.addOutConnection(c)
            subUnit.addInConnection(c)
            if synapseID == 1:
                self.synapseA.append(c)
            elif synapseID == 2:
                self.synapseB.append(c)
            elif synapseID == 3:
                self.synapseC.append(c)

    def connectLayers(self, fromLayer, toLayer, namePrefix):
        
        type = fromLayer[0].type
        if type == 'input':
            synapseID = 1
        elif type == 'hidden':
            synapseID = 2 # the synapse between hiddenLayer1 and hiddenLayer 2
        elif type == 'hiddenB':
            synapseID = 3 # the synapse between hiddenLayer2 and outputLayer
        idx = 0
        for node in fromLayer:
            self.connectUnitToLayer(
                node=node, layer=toLayer, synapseID=synapseID, namePrefix=str(namePrefix+str(idx)))
            idx += 1

    def propogate(self, pattern: list):
        """
        This method takes an input pattern, represented as a list of
        floating-point values, propagates the pattern through the
        network, and returns the resulting output pattern as a list of
        floating-point values.  This method should update the
        activation values of all input, hidden, and output units in
        the network as a side effect.

        It ensures that given pattern is the appropriate length and
        that the values are in the range 0-1.
        """
        output = []

        assert len(pattern) == len(self.inputLayer)

        # Set the activations for the input layer
        for i in range(len(self.inputLayer)):
            node = self.inputLayer[i]
            node.setActivation(pattern[i])
            # print(f"innode: {str(node)}")

        # send values through hidden layer
        for i in range(len(self.hiddenLayer1)):
            nodeH1 = self.hiddenLayer1[i]
            nodeH1.updateActivation()  # should update connections by default

        # <<
        for i in range(len(self.hiddenLayer2)):
            nodeH2 = self.hiddenLayer2[i]
            nodeH2.updateActivation() # should update connections by default
        # >> 

        for i in range(len(self.outputLayer)):
            nodeO = self.outputLayer[i]
            nodeO.updateActivation()

            output.append(nodeO.getActivation())

        return output

    def test(self, VERBOSE=True):
        # print('weights =', pretty([c.weight for c in self.allConnections]))
        # print(f'connections = {[str(c) for c in self.allConnections]}' )

        for pattern in self.inputs:
            output = self.propogate(pattern)
            # hiddenRep = pretty([h.activation for h in self.hiddenLayer])
            hiddenRep1 = []
            hiddenRep2 = []

            for h1 in self.hiddenLayer1:
                hiddenRep1.append(h1.getActivation())

            for h2 in self.hiddenLayer2:
                hiddenRep2.append(h2.getActivation())

            # # print(hiddenRep+" "+str(len(hiddenRep)))
            # if len(self.inputs)<10:
            #     print('%s -> [%s], [%s] -> output %s' % (pattern, hiddenRep1, hiddenRep2, output))

        if VERBOSE:
            for connection in self.synapseA:
                print(f"{str(connection)}")
            for connection in self.synapseB:
                print(f"{str(connection)}")
        print()

    # ====================================================
    # Backprop test

    def computeError(self):
        """
        This method evaluates the network's performance on the
        patterns stored in self.inputs with answers stored in
        self.targets, returning a tuple of the form

        (correct, total, score, error)

        where total is the total number of individual values in the
        target patterns, correct is the number of these that the
        network got right (to within self.tolerance), score is the
        percentage (0-100) of correct values, and error is the total
        sum squared error across all values.
        """
        assert self.targets  # Check if we have defined self.targets

        for idx in range(len(self.inputs)):
            input = self.inputs[idx]
            self.outputs[idx] = self.propogate(input)


        # if len(self.inputs)<11 and len(self.targets)<11:
        #     print(f"targets: {self.targets}, outputs: {self.outputs}")
        
        
        # targets and inputs should be of same length
        assert len(self.targets) == len(self.outputs)
        assert self.outputs

        total = len(self.targets)

        numCorrect = 0

        error = 0
        maxError = 0
        totalError = 0
        for i in range(total):
            # error = self.targets[i] - self.outputs[i][0]

            target = self.targets[i]
            output = self.outputs[i]
            
            try:
                for j in range(len(target)):
                    diff = abs(target[j] - output[j])
                    error += abs(diff)
                    maxError = diff if diff > maxError else maxError
            except:
                print("Failed because target was: ")
                print(target)

            maxErrorSquared = maxError * maxError
            # totalError += errorSqaured
            # totalError += maxErrorSquared # we doing error squared

            # if errorSqaured < self.tolerance:
            if maxErrorSquared < self.tolerance:
                numCorrect += 1

        percentCorrect = (numCorrect/total)*100

        # self.outputs = [] # reset outputs
        totalError = maxErrorSquared

        return (numCorrect, total, percentCorrect, totalError)

    def teachPattern(self, pattern, target, index, sleep=True, sleeptime=1):
        """
        Modifies the weights according to the back-propagation
        learning rule using the given input pattern and associated
        target pattern.

        This method should begin by forward propagating activations.
        Next it should backward propagate error as follows:
        1. Update the deltas associated with every unit in the output layer.
        2. Update the deltas associated with every unit in the hidden layer.
        3. Update the increments associated with every connection in the
           network and then use these to update all weights in the network.
        """
        outputDeltas = []
        hiddenDeltas2 = []
        hiddenDeltas = []
        

        out = self.propogate(pattern)

        # breakpoint()

        # Propogate backwards
        if sleep:
            time.sleep(1)
        # print("UPDATING OUTPUT DELTAS")
        # 1
        # Update deltas for output layer
        for i in range(len(self.outputLayer)):
            node = self.outputLayer[i]
            # get the delta for this node #TODO: EVALUATE WHETHER OR NOT WE NEED TO HAVE THIS HERE
            dO = node.updateDelta(target[i])
            # TARGET INPUT SHOULD NEVER BE A LIST
            outputDeltas.append(dO)

        if sleep:
            time.sleep(sleeptime)
        # print("UPDATING HIDDEN DELTAS")
        # 2
        # Go thru hidden nodes
        
        # >>
        for n in range(len(self.hiddenLayer2)):
            hNode2 = self.hiddenLayer2[n]
            dH2 = hNode2.updateDelta(target)
            hiddenDeltas2.append(dH2)
        # <<

        for m in range(len(self.hiddenLayer1)):
            hNode = self.hiddenLayer1[m]
            dH = hNode.updateDelta(target)
            hiddenDeltas.append(dH)

        if sleep:
            time.sleep(sleeptime)
        # print("UPDATING BIAS DELTAS")
        # Update BIAS deltas
        oBIAS = self.outputBias
        d1 = oBIAS.updateDelta(target)
        outputDeltas.append(d1)

        hBIAS = self.hiddenBias
        hBIAS2 = self.hiddenBias2

        d01 = hBIAS2.updateDelta(target)
        outputDeltas.append(d01)

        d0 = hBIAS.updateDelta(target)
        outputDeltas.append(d0)

        if sleep:
            time.sleep(sleeptime)
        # print("UPDATING SYNAPSE B INCREMENTS")
        # 3A
        
        for connection in self.synapseC:
            connection.updateIncrement(self.learningRate, False)
            
        for connection in self.synapseB:
            connection.updateIncrement(self.learningRate, False)

        if sleep:
            time.sleep(sleeptime)
        # print("UPDATING SYNAPSE A INCREMENTS")

        for connection in self.synapseA:
            connection.updateIncrement(self.learningRate, False)

        # 3B : set new weights

        if sleep:
            time.sleep(sleeptime)
        # print("UPDATING WEIGHTS")
        
        for connection in self.synapseC:
            # increment = self.learningRate * error * prime * activation
            # newWeight = connection.getWeight()
            connection.updateWeight()
            
        for connection in self.synapseB:
            # increment = self.learningRate * error * prime * activation
            # newWeight = connection.getWeight()
            connection.updateWeight()

        for connection in self.synapseA:
            connection.updateWeight()

        # This is where index comes in
        # self.outputs[index] = self.propogate(pattern)

    # ===========================================================
    def teachDataset(self, sleep=False, sleeptime=1):
        """
        Performs one learning sweep through the training set.  Patterns
        are randomly reordered on each sweep.
        """
        assert len(self.inputs) > 0, 'no training data'

        dataset = list(zip(self.inputs, self.targets))

        random.shuffle(dataset)

        i = 0
        for (pattern, target) in dataset:
            
            # if len(pattern)<11 and len(target)<11:
            #     print('   teaching %s -> %s' % (pattern, target))
            
            # print(f"Index: {i}")
            self.teachPattern(pattern, target, i, sleep, sleeptime)
            i += 1

        for j in range(len(self.inputs)):
            input = self.inputs[j]
            self.outputs[j] = self.propogate(input)

    def train(self, cycles=10000, sleep=False, sleeptime=0.003):
        """
        Trains the network for the given number of training cycles
        (with a default of 10000).  This method repeatedly calls
        teachDataset, displaying the current cycle number and
        performance of the network after each call.
        """
        assert len(self.inputs) > 0, 'no training data'
        (correct, total, score, error) = self.computeError()
        print('Epoch #    0: TSS error %7.4f, %d/%d correct (%.1f%%)' %
              (error, correct, total, score))
        for t in range(1, cycles+1):
            self.teachDataset(sleep, sleeptime)
            (correct, total, score, error) = self.computeError()
            print('Epoch #%5d: TSS error %7.4f, %d/%d correct (%.1f%%)' %
                  (t, error, correct, total, score))
            if correct == total:
                print('All patterns learned')
                break
    # =====================================================

    def setTargets(self, targets: list = []):

        targs = []
        for target in targets:
            targs.append(target)

        self.targets = targs
        self.outputs = [0.0]*len(self.targets)
        # print(self.outputs)

    def setInputs(self, inputs: list = []):
        self.inputs = inputs

    def getInputs(self):
        assert self.inputs  # self.inputs should exist
        return self.inputs


if __name__ == "__main__":
    
    # WORKS FOR AUTO ASSOCAITION
    # a = Network(8, 3, 8, 8, learningRate=0.4, tolerance=0.01)
    # inputs = [[1, 0, 0, 0, 0, 0, 0, 0],
    #           [0, 1, 0, 0, 0, 0, 0, 0],
    #           [0, 0, 1, 0, 0, 0, 0, 0],
    #           [0, 0, 0, 1, 0, 0, 0, 0],
    #           [0, 0, 0, 0, 1, 0, 0, 0],
    #           [0, 0, 0, 0, 0, 1, 0, 0],
    #           [0, 0, 0, 0, 0, 0, 1, 0],
    #           [0, 0, 0, 0, 0, 0, 0, 1]]

    # targets = inputs

    # a.setInputs(inputs)
    # a.setTargets(targets)
    # a.test(VERBOSE=False)
    # time.sleep(2)
    # t1 = time.time()
    # a.train(cycles=100000, sleeptime=0.03)
    # t2 = time.time()
    # timeElapsed = t2 - t1
    # print(f"Time Elapsed: {round(timeElapsed,2)}")
    # a.test(VERBOSE=False)
    
    
    e = Encoder()
    
                                # data starts at 28 x 28, scaled down in divisible numbers like 7, 4, 2
    e.encodeAll(subDimension=4) # use if you want 7 x 7 dataset for total of 49 inputs
    # e.encodeAll(subDimension=7) # use if you want 4 x 4 dataset for total of 16 possible inputs

    
    # n = e.encodedXtrain[0]
    
    # print(np.shape(n))

    a = Network(49, 28, 28, 10, learningRate=0.6, tolerance=0.1)
    # a = Network(16, 7, 10, 10, learningRate=0.4, tolerance=0.2)
    
    inputs = e.encodedXtrain[:60]
    targets = e.encodedYtrain[:60]

    a.setInputs(inputs)
    a.setTargets(targets)
    a.test(VERBOSE=False)
    time.sleep(2)
    t1 = time.time()
    a.train(cycles=100000, sleeptime=0.003)
    t2 = time.time()
    timeElapsed = t2 - t1
    print(f"Time Elapsed: {round(timeElapsed,2)}")
    a.test(VERBOSE=False)
