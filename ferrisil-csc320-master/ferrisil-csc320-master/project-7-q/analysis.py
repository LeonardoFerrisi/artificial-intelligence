import csv 
import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np

def plotQLearn(path, title, yLabel, xLabel):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    allRewards = []
    os.chdir(path)
    print(os.getcwd())

    index = 0
    subR = 0
    for i in range(30):
        filename = 'q_'+str(i)+'.csv'
        rewards = []
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter='\n')
            index = 0
            subR = 0
            for row in reader:
                
                # rewards.append(row[0])

                if index % 100 !=0 or index == 0:
                    # print(row)
                    subR += float(row[0])
                    # pass
                else:
                    rewards.append((subR/100))
                    subR = 0
                
                index+=1
        avgreward = [0] + rewards
        # avgreward = rewards

        allRewards.append(np.squeeze(np.array(avgreward)))

    # print(np.shape(rewards))
    runs = np.array(np.linspace(0, 20000, num=200, dtype='int64'))
    # runs = np.array(np.linspace(0, 20000, num=20000, dtype='int64'))
    # print(np.shape(runs))


    for reward in allRewards:
        # print(len(reward))
        assert len(reward) == len(runs)
        plt.plot(runs, reward)

    os.chdir('../')
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.show()

    print("QLearning (No Decay): ")
    print("Learning Rate = 0.1")
    print("Discount Rate = 0.6")
    print("Epsilon = 0.5")
    print("maxSteps = 20")




if __name__ == "__main__":
    os.chdir('project-7-q')
    # plotQLearn('q2', title="Q Learning on CoffeeGame", yLabel='Average Reward (per 1000 Episodes)', xLabel='Num Episodes')
    plotQLearn('taxiQ', title="Q Learning on Taxi V3", yLabel='Average Reward (per 1000 Episodes)', xLabel='Num Episodes')
    # plotQLearn('flQ', title="Q Learning on Frozen Lake", yLabel='Average Reward (per 1000 Episodes)', xLabel='Num Episodes')


