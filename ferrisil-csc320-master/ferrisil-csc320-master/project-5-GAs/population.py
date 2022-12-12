import random
from genome import Genome
from royalroad import RR

globalRR = RR()


class Population:
    """
    Generates a population
    """

    def __init__(self, popSize, genomeLength, population=[], generation=0):
        self.popSize = popSize
        self.length = genomeLength
        self.gen = generation

        if population == []:
            self.generatePopulation()
        else:
            if len(population) == popSize:
                self.pop = population

    def generatePopulation(self, mutate=False, mutRate=0.7):
        pop = []
        while len(pop) < self.popSize:
            newGenome = Genome(self.length)
            if mutate:
                newGenome.mutate(mutRate)
            pop.append(newGenome)
        self.pop = pop

    def print(self):
        for genome in self.pop:
            print(str(genome))

    def getPopulation(self):
        return self.pop

    def giveFitnesses(self):
        allF = []
        for genome in self.pop:
            allF.append(globalRR.evaluateFitness(genome.getBitString()))
        return allF

    def sort(self):
        genomesCovered = []
        fitnesses = {}

        for i in range(self.popSize):
            genome = self.pop[i]
            fitness = globalRR.evaluateFitness(genome.getBitString())
            fitnesses[i] = fitness
            genomesCovered.append(genome)

        sortedFitness = {}
        sortedIdx = []
        # sort fitnesses
        for index, fitness in sorted(fitnesses.items(), key=lambda x: x[1], reverse=True):
            sortedFitness[index] = fitness
            sortedIdx.append(index)

        sortedPopulation = []

        for idx in sortedIdx:
            sortedPopulation.append(self.pop[idx])
        self.pop = sortedPopulation

        # print(sortedIdx)

        # print("\n\n")

        # # print(fitnesses)
        # # for key, value in fitnesses:
        # #     print(f"{}")
        # # print("\n\n")
        # print(sortedFitness)


if __name__ == "__main__":
    p = Population(128, 64, [], 0)
    p.generatePopulation()

    # p.print()
    # print("\n"+str(p.giveFitnesses()))
    # p.sort()
    # # print("\n\n")
    # p.print()
    # print("\n"+str(p.giveFitnesses()))
