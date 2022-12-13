import math
import random

class Unit:
    """
    A Unit object represents a node in a network.  It keeps track of
    the node's current activation value (between 0.0 and 1.0), as well
    as all of the connections from other units into this unit, and all
    of the connections from this unit to other units in the network.
    """

    def __init__(self, activation=0.0, name='node', type='input'):
        assert 0.0 <= activation <= 1.0, 'activation out of range'
        self.activation = activation
        self.incomingConnections = []
        self.outgoingConnections = []
        self.delta = 0

        self.name = name
        assert type == 'input' or type == 'hidden' or type == 'hiddenB' or type == 'output'  # Must be one of these 3
        self.type = type

    def sigmoidFunction(self, x):
        if x < 0:
            return 1 - 1/(1 + math.exp(x))
        else:
            return 1/(1 + math.exp(-x))

    # Wire Operations
    def addInConnection(self, connection):
        self.incomingConnections.append(connection)

    def addOutConnection(self, connection):
        self.outgoingConnections.append(connection)

    # def updateOutgoingConnections(self):
    #     for connection in self.outgoingConnections:
    #         # update the toUnits value
    #         toUnit = connection.getToUnit()
    #         weight = connection.getWeightedInput()
    #         newVal = 
    #         toUnit.setActivation()

    def updateActivation(self):
        newVal = 0
        for connection in self.incomingConnections:
            newVal += connection.getWeightedInput()
        
        newActivation = self.sigmoidFunction(newVal)
        self.setActivation(newActivation)

    def updateDelta(self, target=None):
        """
        Updates own delta and returns updated delta value
        target not need
        """
        prime = self.activation * (1 - self.activation) # derivative of activation

        if self.type=='output':
            assert target != None

            if type(target) != list:
                error = target - self.activation
            else:
                error = 0
                for i in range(len(target)):
                    error += target[i] - self.activation
            
            self.setDelta(prime*error)
        elif self.type=='hidden' or self.type=='hiddenB' or self.type=='input': # TODO: Make exclusive to hidden and input nodes
            delta = 0
            for out in self.outgoingConnections:
                # nextNode = out.getToUnit()
                w = out.getWeight()
                d = out.getToUnit().getDelta()
                delta += w * d
            self.delta = delta*prime
        return self.delta

    # SETTERS

    def setActivation(self, value):
        self.activation = float(value)
        # self.updateDelta()

    def setDelta(self, value):
        self.delta = value

    # GETTERS

    def getActivation(self):
        return self.activation

    def getDelta(self):
        return self.delta

    def __str__(self):
        # return ("["+str(self.name)+"]:"+str(self.type)+" - activation: "+str(self.activation)+", delta: "+str(self.delta))
        return ("["+str(self.name)+"]:"+str(self.type)+" - a: "+str(self.activation)+", d: "+str(self.delta))

