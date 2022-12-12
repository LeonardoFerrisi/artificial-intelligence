import random
from unit import Unit

class Connection:
    """
    A Connection object represents a connection between two units of a
    network.  The connection strength is initialized to a small random
    value.
    """

    def __init__(self, fromUnit:Unit, toUnit:Unit, name:str=''):
        self.fromUnit = fromUnit
        self.toUnit = toUnit
        self.randomize()
        self.increment = 0

        self.name = name

    def randomize(self):
        self.weight = random.uniform(-0.1, +0.1)

    def getfromUnit(self):
        return self.fromUnit
    
    def getToUnit(self):
        return self.toUnit

    def getWeightedInput(self):
        return self.weight*self.fromUnit.getActivation()

    def __str__(self):
        return f"{self.name}: [{str(self.fromUnit)}] > (w:{self.weight}) > [{str(self.toUnit)}]"

    def setWeight(self, newValue):
        self.weight = newValue

    def updateWeight(self, VERBOSE=False):
        """
        Updates the weight by mutliplying the increment
        PRECONDION:
        Must have updated increments prior to using
        """
        newWeight = self.weight + self.increment # where new weight equals self.weight + (learningRate * fromActivation * toDelta)
        if VERBOSE: print(f"[{self.name}]: w: {self.weight}, i: {self.increment}")
        self.setWeight(newWeight)
 
    def updateToUnit(self):
        """
        Updates the activation of the toUnit's activation
        """
        newActivation = self.weight * self.fromUnit.getActivation()
        to = self.toUnit
        to.setActivation(newActivation)

    def getIncrement(self):
        return self.increment

    def updateIncrement(self, learningRate, VERBOSE=False):
        """
        Updates the increment
        """
        # increment = self.learningRate * error * prime * activation
        # error = target - self.toUnit.activation
        # newValue = learningRate * error *self.fromUnit.getActivation() * self.toUnit.getDelta()
        newValue = learningRate * self.fromUnit.getActivation() * self.toUnit.getDelta() 
        self.increment = newValue
        if VERBOSE: print(f"[{self.name}]: {str(self.fromUnit)}, {self.toUnit}, [{self.weight}], inc:[{newValue}]")


    def getWeight(self):
        """
        Gets the weight
        """
        return self.weight
