from cgi import print_arguments
import random


def evaluteProb(prob):
    """
    Evaluates a value produced by input probability
    """
    r = random.random()
    # r = random.randint(0,100)
    return r < prob


class Genome:
    """
    A class that creates a geneome composed of a bitstring of 
    size 'bitStringSize' composed of 0s and 1s randomly
    """

    def __init__(self, bitStringSize, bitstring=''):
        self.size = bitStringSize
        self.bitstring = bitstring
        if bitstring == '':
            self.__generateBitstring()

    def __generateBitstring(self):
        while len(self.bitstring) < self.size:
            self.bitstring += str((random.randint(0, 1)))

    def mutateGene(self, input):
        """
        Mutates a single gene by swapping its value
        """
        bit = '1' if input == '0' else '1'
        return bit

    def mutate(self, mutRate):
        """
        Iterates through every bit in geneome (bitstring)
        Will mutate according to provided mutation rate
        """
        listGenome = self.asList()
        for i in range(self.size):
            willMutate = evaluteProb(mutRate)
            if willMutate:
                gene = listGenome[i]
                listGenome[i] = self.mutateGene(gene)
        self.bitstring = "".join(listGenome)

    def __str__(self):
        return str(self.bitstring)

    def getBitString(self):
        return self.bitstring

    def asList(self):
        return [gene for gene in self.bitstring]


if __name__ == "__main__":
    # for i in range(1000):
    #     r = random.random()
    #     if r < 0.005:
    #         print("hit")

    g = Genome(64)
    print(str(g))
    g.mutate(mutRate=0.5)
    print(str(g))

    # print(g.asList())
    # print(len(g.asList()))
