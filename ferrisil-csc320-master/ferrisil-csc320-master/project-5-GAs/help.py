import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

def getMaxGen(allData:list):
    firstData = allData[0]
    firstMax = firstData[['GEN']].iloc[-1].values[0]
    maxGen = firstMax
    gIDX = firstData.index

    for data in allData:
        val = data[['GEN']].iloc[-1].values[0]
        toPrint = str(val)+ ", current maxGen: " + str(maxGen)
        # print(f"Is greater? : Value {val}, maxGen {maxGen}, value > maxGen: {val > maxGen}, TYPES: {type(val)}, {type(maxGen)}")
        if  (val > maxGen):
            maxGen = val
            gIDX = data.index

    return maxGen, gIDX

def getMinGen(allData:list):
    firstData = allData[0]
    firstMax = firstData[['GEN']].iloc[-1].values[0]
    minGen = firstMax
    gIDX = firstData.index

    for data in allData:
        val = data[['GEN']].iloc[-1].values[0]
        toPrint = str(val)+ ", current maxGen: " + str(minGen)
        # print(f"Is less than? : Value {val}, minGen {minGen}, value < minGen: {val < minGen}, TYPES: {type(val)}, {type(minGen)}")
        if  (val < minGen):
            minGen = val
            gIDX = data.index

    return minGen, gIDX


def directoryToDataFrames(dirPath):
    current_path = os.getcwd()
    path = current_path+str(os.sep)+dirPath
    csvs = path+os.sep+'*.csv'

    allData = []

    for file in glob.glob(csvs):
        # print(str(file))
        df = pd.read_csv(file, sep=',')
        allData.append(df)

    return allData

def makeAllDataSameLen(allData, maxLen):
    """
    Makes all the data in a list the same length
    """

    toReturn = []
    
    for myList in allData:
        
        length = len(myList)
        diff = (maxLen) - length
        toAdd = [0] * diff
        if length!=maxLen:
            moddedData = myList+toAdd
            toReturn.append(moddedData)
        else:
            # print("SAME LEN")
            toReturn.append(myList)
    assert (len(data)==maxLen for data in toReturn)
    
    return toReturn

def collectMaxes(allData, maxLen):
    allMaxes = []
    for df in allData:
        maxes = df[['MAX']].squeeze().tolist()
        allMaxes.append(maxes)
    toReturn = makeAllDataSameLen(allMaxes, maxLen)
    return toReturn

def combineData(all, maxLen, requiredLen=30):
    """
    Combines a list of 30 lists of maxes, one for each run
    Returns a tuple of means, mins, and maxes of ever run's maximums
    """
    assert len(all)==requiredLen

    means = [0] * maxLen
    mins = [0] * maxLen
    maxes = [0] * maxLen

    assert [len(data) == maxLen for data in all]

    for generation in range(maxLen):
        
        # Get the every max value from every dataset for this generation
        currents = [int(all[i][generation]) for i in range(len(all))] 

        meanMax = avgMax(currents)
        maxMax = maxmax(currents)
        minMax = minmax(currents)
        means[generation] = meanMax if meanMax > means[generation-1] else means[generation-1]
        mins[generation] = minMax if minMax > mins[generation-1] else mins[generation-1]
        maxes[generation] = maxMax if maxMax > maxes[generation-1] else maxes[generation-1]

    return (means, mins, maxes)

def avgMax(currents):
    c = __removeZeros(currents)
    output = np.mean(c)
    return int(output)

def maxmax(currents):
    c = __removeZeros(currents)
    output = max(c)
    return output

def minmax(currents):
    c = __removeZeros(currents)
    output = min(c)
    return output

def __removeZeros(input: list):

    for item in input:
        if int(item)==0:
            input.pop(item)
    
    return input

def grabDataFromFileAndPlot(filename : str, popSize, title='', numRuns=30):
    data = directoryToDataFrames(filename)
    maxLen = getMaxGen(data)[0]+1
    minLen = getMinGen(data)[0]+1
    allMaxes = collectMaxes(data, maxLen)

    assert [len(i)==maxLen for i in allMaxes]

    allData = combineData(allMaxes, maxLen, numRuns)
    x = [gen * popSize for gen in range(maxLen)]
    y = allData[0]
    w = allData[1]
    z = allData[2]

    df1 = pd.DataFrame({'Mean': y, 'Minimum': w, 'Maximum' : z}, index=x)
    ax = df1.plot()

    plt.show()
    return ax, maxLen, minLen


if __name__ == "__main__":
    # data = directoryToDataFrames('project-5-GAs\hillclimber_data')
    # minLen = getMinGen(data)[0]+1
    # print(minLen)

    # data = directoryToDataFrames('project-5-GAs\\rrga_data')
    # minLen = getMinGen(data)[0]+1
    # print(minLen)

    data = directoryToDataFrames('project-5-GAs\\rrga_woINTER_data')
    minLen = getMinGen(data)[0]+1
    print(minLen)