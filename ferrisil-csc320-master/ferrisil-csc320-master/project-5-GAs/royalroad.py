class RR:
    """
    Generates a royal road as described in the royal roads paper
    """

    def __init__(self, min: int = 8, max: int = 64, steps: int = 4, useIntermediate=True):

        self.min = min
        self.max = max
        self.startingParams = []
        self.royalroad = []
        self.maxScoreArray = []
        currentParam = min
        multiplier = 2
        for i in range(steps):
            self.startingParams.append(currentParam)
            currentParam = currentParam * multiplier
        # print(self.startingParams)
        self.generateRoad(useIntermediate)
        # print(str(self.maxScoreArray))

    def generateRoad(self, useIntermediate):
        """
        Generates the royal road as according to the starting parameters
        """

        if useIntermediate:
            for geneSize in self.startingParams:
                q = int(self.max/geneSize)

                for i in range(q):
                    self.maxScoreArray.append(geneSize)
                    self.royalroad.append(self.genBitString(
                        start=geneSize*i, size=geneSize))
        else:
            subParams = [self.startingParams[0], self.startingParams[-1]]

            for geneSize in subParams:
                q = int(self.max/geneSize)
                for i in range(q):
                    self.maxScoreArray.append(geneSize)
                    self.royalroad.append(self.genBitString(
                        start=geneSize*i, size=geneSize))

    def genBitString(self, start, size):
        """
        Generates a a single bitstring to put in the royal road
        """

        bitString = ['0' for x in range(self.max)]
        end = start+size
        i = start
        while i < end:
            bitString[i] = '1'
            i += 1
        toReturn = ''
        for item in bitString:
            toReturn += (item)
        return toReturn

    def __str__(self):
        return str(self.royalroad)

    def printRR(self):
        """
        Prints the royal road
        """

        for row in self.royalroad:
            print(str(row))

    def get(self):
        """
        Returns the list representing the royal road
        """
        return self.royalroad

    def evaluateFitness(self, inputGene):
        """
        Evaluates how many bitstrings an input genome satisfies the requirement of
        The maximum possible score for the mitchel paper royal road is 256
        Scores range from 0 - 256
        """
        score = 0
        for index in range(len(self.royalroad)):
            bitstring = self.royalroad[index]
            score += self.__evalauteFitnessForSingleBitString(
                bitstring, inputGene, index)
        return score

    def __evalauteFitnessForSingleBitString(self, bitString: str, inputGene: str, index: int):
        # print(inputGene)
        inGene = inputGene
        ourBitString = bitString

        score = 0
        desiredOutput = self.maxScoreArray[index]

        for i in range(len(ourBitString)):
            currentBit = ourBitString[i]
            if currentBit == '1':
                if inGene[i] == '1':
                    score += 1
        if score == desiredOutput:
            return score
        else:
            return 0


if __name__ == "__main__":
    rr = RR(8, 64, 4, useIntermediate=False)
    # print(str(rr))
    rr.printRR()
    # for i in range(4):
    #     print(rr.genBitString(16, (i*16)))
    print("\n")
    # testbit = ''
    # for i in range(64):
    #     if i < 48:
    #         testbit += '1'
    #     else:
    #         testbit += '0'
    # print(testbit)
    # # alpha = rr.evalauteFitnessForSingleBitString(rr.get()[8], testbit, 8)
    # alpha = rr.evaluateFitness(testbit)
    # print(f"\n{alpha}")
