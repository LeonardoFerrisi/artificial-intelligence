import pandas as pd
import os
import glob

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


def getPlottableDataFrame(genr, maxGen, idx):
    # allPlots = []
    # x = genr[['GEN']].squeeze().tolist()
    # x = [gen * popSize for gen in x]


    y = genr[['MEAN']].squeeze().tolist()
    w = genr[['MIN']].squeeze().tolist()
    z = genr[['MAX']].squeeze().tolist()
    df = pd.DataFrame({'Means': y, 'Mins': w, 'Maxs' : z}, index=idx)
    # allPlots.append(df)
    # df.plot(ax=ax)
    return df


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

def collectAllMeans(allData, maxLen):
    """
    Takes a list of a bunch of df and gets all means
    """
    allMeans = []
    
    for df in allData:
        means = df[['MEAN']].squeeze().tolist()
        allMeans.append(means)

    toReturn = makeAllDataSameLen(allMeans, maxLen)
    return toReturn

def collectAllMaxes(allData, maxLen):
    """
    Takes a list of a bunch of df and gets all means
    """
    allMaxes = []
    
    for df in allData:
        means = df[['MAX']].squeeze().tolist()
        allMaxes.append(means)

    toReturn = makeAllDataSameLen(allMaxes, maxLen)
    return toReturn


def combineAllData(allGENS, maxLen):
    """
    Where all is all 30 datasets, should just be a list of 30 lists of the MEANS data

    Input allGENS should be a 1D arrayvv 
    """
    
    assert len(allGENS) == 30

    means = [0] * maxLen # across all 30
    mins = [0] * maxLen
    maxes = [0] * maxLen

    assert [len(data) == maxLen for data in allGENS]

    for generation in range(maxLen):
        
        currents = [int(allGENS[i][generation]) for i in range(len(allGENS))]
         
        mean = __getMeanFromCurrents(means, generation, currents)
        maximum = __getMaxFromCurrents(maxes, generation, currents)
        minimum = __getMinFromCurrents(mins, generation, currents)

        means[generation] = mean
        mins[generation] = minimum
        maxes[generation] = maximum

    return (means, mins, maxes)

def __getMeanFromCurrents(means, generation, currents):
    myMeans = []
    mean = 0
    for i in range(len(currents)):
        current = currents[i]
        if current != 0:
            myMeans.append(int(current))
    mean = sum(myMeans) / len(myMeans)
    return mean

def __getMaxFromCurrents(maxes, generation, currents):
    maximum = 0
    currentMax = max(currents)
    if maximum > 0:
            maximum = currentMax 
    else: 
        maximum = maxes[generation-1]
    return maximum

def __getMinFromCurrents(mins, generation, currents):
    minimum = 0
    currentMin = min(currents)
    if minimum > 0:
            minimum = currentMin
    else: 
        minimum = mins[generation-1]
    return minimum

if __name__ == "__main__":
    
    pass