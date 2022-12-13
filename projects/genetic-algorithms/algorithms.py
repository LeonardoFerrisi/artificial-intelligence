import random
import numpy as np
import matplotlib

from royalroad import RR
from population import Population
from genome import Genome
import os
import csv


def evaluteProb(prob):
    """
    Evaluates a value produced by input probability
    """
    r = random.random()
    return r < prob


class HillClimber:

    def __init__(self, popSize, genomeLen, mutRate, usingRR=True, seed=None):

        if seed != None:
            random.seed(int(seed))
            self.seed = seed
        # some constants
        self.royalroad = RR()
        self.targetFitness = self.getTargetFitness()

        self.popSize = popSize
        self.bitlen = genomeLen
        self.mutRate = mutRate

        self.currentFitness = 0

        self.generateInitialPopualtion()  # creates initial population of random genomes

        # holders
        self.allOptimums = []
        self.allMinimums = []
        self.allMeans = []

    def record(self):
        pass

    def getFitness(self, genome: Genome):
        return self.royalroad.evaluateFitness(genome.getBitString())

    def generateInitialPopualtion(self):

        self.population = Population(self.popSize, self.bitlen, generation=0)
        self.population.generatePopulation()  # make a random one initially
        # self.population.sort()

    def getTargetFitness(self):
        genomeLen = 64
        dummyGenome = Genome(genomeLen, "1"*genomeLen)
        return self.getFitness(dummyGenome)

    def evalPopulation(self, pop: Population):
        population = pop.getPopulation()  # returns population as list

        assert len(population) != 0

        max = 0
        min = 0
        mean = 0
        fitnesses = []
        for genome in population:
            fitnesses.append(self.getFitness(genome))

        fitnesses.sort(reverse=True)
        max = fitnesses[0]
        min = fitnesses[-1]
        mean = np.mean(fitnesses)
        return max, min, mean

    def mutatePopulation(self):
        gen = self.population.gen
        newPopulation = []
        for genome in self.population.getPopulation():
            childGenome = genome
            childGenome.mutate(mutRate=self.mutRate)
            newPopulation.append(childGenome)
        return Population(self.popSize, self.bitlen,
                          population=newPopulation, generation=gen+1)

    def execute(self, verbose=True, writeToFile=False, filepath=str(str(os.getcwd())+str(os.sep)+'ferrisil-csc320'+str(os.sep)+'project-5-GAs'+str(os.sep)+'hillclimber_data'), iter=None):

        # initial fitness vals and stuffs
        max, min, mean = self.evalPopulation(self.population)
        self.allOptimums.append(max)
        self.allMinimums.append(min)
        self.allMeans.append(mean)
        generations = [0]
        if verbose:
            print(
                f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")

        if writeToFile:
            assert filepath != ''  # filepath must be specified
            assert iter != None  # Iter must be equal to the file num, cannot be None
            f = open(
                str(filepath+str(os.sep)+f'data_{iter}.csv'), 'w', encoding='utf-8-sig')
            writer = csv.writer(f)
            header = ['GEN', 'MAX', 'MIN', 'MEAN', 'SEED']
            writer.writerow(header)
            writer.writerow([self.population.gen, max, min, mean, self.seed])

        while self.allOptimums[-1] < self.targetFitness:

            # random.seed(random.randint(0, 1000))

            # self.population = self.breedNextGen()
            self.population = self.mutatePopulation()
            generations.append(self.population.gen)
            max, min, mean = self.evalPopulation(self.population)
            self.allMinimums.append(min)
            self.allMeans.append(mean)
            self.allOptimums.append(max)
            if verbose:
                print(
                    f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")
            if writeToFile:
                writer.writerow([self.population.gen, max, min, mean])
        print(f"COMPLETED ITERATION: {iter}")


class RoyalGeneticAlgortithm:

    """
    Creates a genetic algorithm inspired by Mitchel's "Royal Roads" paper
    Does not use intermediate levels
    """

    def __init__(self, populationSize, bitStringSize, mutRate=0.005, crossoverRate=0.7, seed=None):

        if seed != None:
            random.seed(int(seed))
            self.seed = seed

        # some constants
        # uses intermediates as default
        self.royalroad = RR(useIntermediate=False)

        self.targetFitness = self.getTargetFitness()

        self.popSize = populationSize
        self.bitlen = bitStringSize
        self.mutRate = mutRate
        self.crossoverRate = crossoverRate

        self.currentFitness = 0

        self.generateInitialPopualtion()  # creates initial population of random genomes

        # holders
        self.allOptimums = []
        self.allMinimums = []
        self.allMeans = []

        # do stuff
        # self.generatePopulation()

    def generateInitialPopualtion(self):

        self.population = Population(
            self.popSize, self.bitlen, generation=0)
        self.population.generatePopulation()  # make a random one initially
        # self.population.sort()

    def getTargetFitness(self):
        genomeLen = 64
        dummyGenome = Genome(genomeLen, "1"*genomeLen)
        return self.getFitness(dummyGenome)

    def getFitness(self, geneome: Genome):
        return self.royalroad.evaluateFitness(geneome.getBitString())

    def evalPopulation(self, pop: Population):
        population = pop.getPopulation()  # returns population as list

        assert len(population) != 0

        max = 0
        min = 0
        mean = 0
        fitnesses = []
        for genome in population:
            fitnesses.append(self.getFitness(genome))

        fitnesses.sort(reverse=True)
        max = fitnesses[0]
        min = fitnesses[-1]
        mean = np.mean(fitnesses)
        return max, min, mean

    def halvePopulation(self):
        targetSize = int(self.popSize/2)
        # prevGen = self.population.gen
        newPopulation = self.population.getPopulation()[:targetSize]
        return newPopulation

    def crossover(self, genome1: Genome, genome2: Genome, mutate=True):
        """
        Crosses over two genomes according to crossover rate,
        then mutates them
        """
        willCross = evaluteProb(self.crossoverRate)

        if willCross:
            crossIdx = np.random.randint(self.bitlen)

            bS1A = genome1.getBitString()[:crossIdx]
            bS2A = genome2.getBitString()[:crossIdx]
            bS1B = genome1.getBitString()[crossIdx:]
            bS2B = genome2.getBitString()[crossIdx:]
            newGenome1 = Genome(self.bitlen, bS1A+bS2B)
            newGenome2 = Genome(self.bitlen, bS2A+bS1B)

            if mutate:
                newGenome1.mutate(self.mutRate)
                newGenome2.mutate(self.mutRate)

            return newGenome1, newGenome2

        else:
            if mutate:
                genome1.mutate(self.mutRate)
                genome2.mutate(self.mutRate)

            return genome1, genome2

    def doCrossovers(self):
        pop = self.population.getPopulation()
        for i in range(self.popSize-1):
            genomeA, genomeB = self.crossover(pop[i], pop[i+1])
            pop[i] = genomeA
            pop[i+1] = genomeB
        return pop

    def breedNextGen(self):
        """
        Takes the currently stored population,
        halves it, and then generates a new half
        sorts the new population and returns it 
        as a Population object of one greater generation
        """
        gen = self.population.gen
        newPopulation = self.doCrossovers()

        assert (len(newPopulation) == self.popSize)

        toReturn = Population(self.popSize, self.bitlen,
                              population=newPopulation, generation=gen+1)
        # toReturn.sort()
        return toReturn

    def execute(self, verbose=True, writeToFile=False, filepath=str(str(os.getcwd())+str(os.sep)+'ferrisil-csc320'+str(os.sep)+'project-5-GAs'+str(os.sep)+'rrga_woINTER_data'), iter=None):

        # initial fitness vals and stuffs
        max, min, mean = self.evalPopulation(self.population)
        self.allOptimums.append(max)
        self.allMinimums.append(min)
        self.allMeans.append(mean)
        generations = [0]
        if verbose:
            print(
                f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")

        if writeToFile:
            assert filepath != ''  # filepath must be specified
            assert iter != None  # Iter must be equal to the file num, cannot be None
            f = open(
                str(filepath+str(os.sep)+f'rr_noInter_data_{iter}.csv'), 'w', encoding='utf-8-sig')
            writer = csv.writer(f)
            header = ['GEN', 'MAX', 'MIN', 'MEAN', 'SEED']
            writer.writerow(header)
            writer.writerow([self.population.gen, max, min, mean, self.seed])

        while self.allOptimums[-1] < self.targetFitness:

            # random.seed(random.randint(0, 1000))

            self.population = self.breedNextGen()
            # self.population = self.mutatePopulation()
            generations.append(self.population.gen)
            max, min, mean = self.evalPopulation(self.population)
            self.allMinimums.append(min)
            self.allMeans.append(mean)
            self.allOptimums.append(max)

            if verbose:
                print(
                    f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")

            if writeToFile:
                writer.writerow([self.population.gen, max, min, mean])

        print(f"COMPLETED ITERATION: {iter}")
        # return self.population.gen, self.allOptimums[-1], self.allMinimums[-1], self.allMeans[-1]


class RoyalInterGeneticAlgorithm:
    """
    Creates a genetic algorithm inspired by Mitchel's "Royal Roads" paper
    """

    def __init__(self, populationSize, bitStringSize, mutRate=0.005, crossoverRate=0.7, seed=None):

        if seed != None:
            random.seed(int(seed))
            self.seed = seed

        # some constants
        self.royalroad = RR()  # uses intermediates as default
        self.targetFitness = self.getTargetFitness()

        self.popSize = populationSize
        self.bitlen = bitStringSize
        self.mutRate = mutRate
        self.crossoverRate = crossoverRate

        self.currentFitness = 0

        self.generateInitialPopualtion()  # creates initial population of random genomes

        # holders
        self.allOptimums = []
        self.allMinimums = []
        self.allMeans = []

        # do stuff
        # self.generatePopulation()

    def generateInitialPopualtion(self):

        self.population = Population(
            self.popSize, self.bitlen, generation=0)
        self.population.generatePopulation()  # make a random one initially
        # self.population.sort()

    def getTargetFitness(self):
        genomeLen = 64
        dummyGenome = Genome(genomeLen, "1"*genomeLen)
        return self.getFitness(dummyGenome)

    def getFitness(self, geneome: Genome):
        return self.royalroad.evaluateFitness(geneome.getBitString())

    def evalPopulation(self, pop: Population):
        population = pop.getPopulation()  # returns population as list

        assert len(population) != 0
        max = 0
        min = 0
        mean = 0
        fitnesses = []
        for genome in population:
            fitnesses.append(self.getFitness(genome))

        fitnesses.sort(reverse=True)
        max = fitnesses[0]
        min = fitnesses[-1]
        mean = np.mean(fitnesses)
        return max, min, mean

    def halvePopulation(self):
        targetSize = int(self.popSize/2)
        # prevGen = self.population.gen
        newPopulation = self.population.getPopulation()[:targetSize]
        return newPopulation

    def crossover(self, genome1: Genome, genome2: Genome, mutate=True):
        """
        Crosses over two genomes according to crossover rate,
        then mutates them
        """
        willCross = evaluteProb(self.crossoverRate)

        if willCross:
            crossIdx = np.random.randint(self.bitlen)

            bS1A = genome1.getBitString()[:crossIdx]
            bS2A = genome2.getBitString()[:crossIdx]
            bS1B = genome1.getBitString()[crossIdx:]
            bS2B = genome2.getBitString()[crossIdx:]
            newGenome1 = Genome(self.bitlen, bS1A+bS2B)
            newGenome2 = Genome(self.bitlen, bS2A+bS1B)

            if mutate:
                newGenome1.mutate(self.mutRate)
                newGenome2.mutate(self.mutRate)

            return newGenome1, newGenome2

        else:
            if mutate:
                genome1.mutate(self.mutRate)
                genome2.mutate(self.mutRate)

            return genome1, genome2

    def doCrossovers(self):
        pop = self.population.getPopulation()
        for i in range(self.popSize-1):
            genomeA, genomeB = self.crossover(pop[i], pop[i+1])
            pop[i] = genomeA
            pop[i+1] = genomeB
        return pop

    def breedNextGen(self):
        """
        Takes the currently stored population,
        halves it, and then generates a new half
        sorts the new population and returns it 
        as a Population object of one greater generation
        """
        gen = self.population.gen
        newPopulation = self.doCrossovers()

        assert (len(newPopulation) == self.popSize)

        toReturn = Population(self.popSize, self.bitlen,
                              population=newPopulation, generation=gen+1)
        # toReturn.sort()
        return toReturn

    def execute(self, verbose=True, writeToFile=False, filepath=str(str(os.getcwd())+str(os.sep)+'ferrisil-csc320'+str(os.sep)+'project-5-GAs'+str(os.sep)+'rrga_data'), iter=None):

        # initial fitness vals and stuffs
        max, min, mean = self.evalPopulation(self.population)
        self.allOptimums.append(max)
        self.allMinimums.append(min)
        self.allMeans.append(mean)
        generations = [0]
        if verbose:
            print(
                f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")

        if writeToFile:
            assert filepath != ''  # filepath must be specified
            assert iter != None  # Iter must be equal to the file num, cannot be None
            f = open(
                str(filepath+str(os.sep)+f'rrga_data_{iter}.csv'), 'w', encoding='utf-8-sig')
            writer = csv.writer(f)
            header = ['GEN', 'MAX', 'MIN', 'MEAN', 'SEED']
            writer.writerow(header)
            writer.writerow([self.population.gen, max, min, mean, self.seed])

        while self.allOptimums[-1] < self.targetFitness:

            # random.seed(random.randint(0, 1000))

            self.population = self.breedNextGen()
            # self.population = self.mutatePopulation()
            generations.append(self.population.gen)
            max, min, mean = self.evalPopulation(self.population)
            self.allMinimums.append(min)
            self.allMeans.append(mean)
            self.allOptimums.append(max)
            if verbose:
                print(
                    f"GEN {self.population.gen}, max: {max}, min: {min}, mean: {mean}\n")
            if writeToFile:
                writer.writerow([self.population.gen, max, min, mean])
        print(f"COMPLETED ITERATION: {iter}")

        # return self.population.gen, self.allOptimums[-1], self.allMinimums[-1], self.allMeans[-1]

    def writeToCSV(self, filename):
        pass


if __name__ == "__main__":
    # ga = GeneticAlgorithm(128, 64)

    # population generation test
    # ga.generatePopulation()
    # ga.printPopulation()

    # hc = HillClimber(128, 64, 0.005)
    # hc.execute()

    # rrga = RoyalInterGeneticAlgorithm(128, 64, 0.005, 0.7)
    # rrga.execute()

    # rrnimga = RoyalGeneticAlgortithm(128, 64, 0.005, 0.7)
    # rrnimga.execute()
    pass
