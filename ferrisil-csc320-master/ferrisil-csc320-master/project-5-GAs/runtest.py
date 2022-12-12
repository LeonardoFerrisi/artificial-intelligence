from tabnanny import verbose
from algorithms import *
import numpy as np
import matplotlib
import pandas as pd
import os
import csv


def runHillClimber(numRuns, path, defaultFolder='hillclimber_data'):
    path = path+os.sep+defaultFolder
    for i in range(numRuns):
        # todo: include new random seeds
        # Do the algortithm
        h = HillClimber(popSize=128, genomeLen=64, mutRate=0.005, seed=i*1234)
        # there is a filepath parameter for the parentdir of the data if it is not working by default
        h.execute(verbose=False, writeToFile=True, iter=i, filepath=path)


def runGA(numRuns, path, defaultFolder='rrga_data'):
    path = path+os.sep+defaultFolder
    for i in range(numRuns):
        ga = RoyalInterGeneticAlgorithm(
            populationSize=128, bitStringSize=64, mutRate=0.005, crossoverRate=0.7, seed=i*1234)
        ga.execute(verbose=False, writeToFile=True, iter=i, filepath=path)


def runGA_withoutIntermediate(numRuns, path, defaultFolder='rrga_woINTER_data'):
    path = path+os.sep+defaultFolder
    for i in range(numRuns):

        ga = RoyalGeneticAlgortithm(
            populationSize=128, bitStringSize=64, mutRate=0.005, crossoverRate=0.7, seed=i*1234)
        ga.execute(verbose=False, writeToFile=True, iter=i, filepath=path)

def runAll(numRuns, path):
    """
    Runs the hillClimber algorithm until completion numRuns times
    
    Runs the genetic algorithm using Royal Roads w/ Intermediate until completion numRuns times
    
    Runs the genetic algorithm using Royal Roads wo/ Intermediate until completion numRuns times
    """
    runHillClimber(numRuns, path)
    runGA_withoutIntermediate(numRuns, path)
    runGA(numRuns, path)

if __name__ == "__main__":

    # runHillClimber(30)
    # runGA_withoutIntermediate(30)
    runGA(30)
