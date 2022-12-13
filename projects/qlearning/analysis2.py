import csv 
import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np

def plotQLearnWDecay(path, title, yLabel, xLabel):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    allRewards = []
    os.chdir(path)
    print(os.getcwd())

    index = 0
    subR = 0
    for i in range(30):
        filename = 'q2_'+str(i)+'.csv'
        rewards = []
        with open(filename, 'r', encoding='utf-8-sig') as file:
            # reader = csv.reader(file, delimiter=' ')
            # index = 0
            # subR = 0
            # for row in reader:
            #     rewards.append(float(row[0]))
            reader = csv.reader(file, delimiter=' ')
            index = 0
            subR = 0
            for row in reader:
                if index % 100 !=0 or index == 0:
                    # print(row)
                    subR += float(row[0])
                else:
                    rewards.append((subR/100))
                    subR = 0
                index+=1
        avgreward = [0] + rewards
        # avgreward = rewards

        # print(len(avgreward))
        allRewards.append(np.squeeze(np.array(avgreward)))

    # runs = np.array(np.linspace(0, 20000, num=20, dtype='int64'))
    runs = np.array(np.linspace(0, 20000, num=200, dtype='int64'))
    
    # print(type(allRewards))
    # print(len(allRewards))
    # print(len(allRewards[0]))
    # print(len(runs))

    for reward in allRewards:
        assert len(reward) == len(runs)
        plt.plot(runs, reward)

    os.chdir('../')
    plt.title("Q Learning on CoffeeGame (with decay)")
    plt.ylabel('Average Reward (per 1000 Episodes)')
    plt.xlabel('Num Episodes')
    plt.show()

    print("QLearning (with Decay): ")
    print("Learning Rate = 0.1")
    print("Discount Rate = 0.6")
    print("(Initial) Epsilon = 1.0")
    print("Decay Rate = 0.0005")
    print("maxSteps = 20")

if __name__ == "__main__":
    print(os.getcwd())
    os.chdir('project-7-q')
    # plotQLearnWDecay('QwithDecay', title="Q Learning with Decay on Coffegame", yLabel='Average Reward (per 1000 Episodes)', xLabel='Num Episodes')
    plotQLearnWDecay('taxiQwDelay', title="Q Learning with Decay on Taxi V3", yLabel='Average Reward (per 1000 Episodes)', xLabel='Num Episodes')




