import csv
from QLearningAgent import QLearningAgent as Qla
from QLearningAgent2 import QLearningAgent2 as Qla2
import coffeegame
import numpy as np
import matplotlib.pyplot as plt
import gym
import os

def run(numTimes):
    # env = coffeegame.CoffeeEnv()

    env = gym.make("Taxi-v3").env
    for i in range(numTimes):
        
        DECAYRATE = 0.0005
        q = Qla2(alpha=0.1, gamma=0.6, epsilon=0.5, maxSteps=20, maxEp=20000, decay=1.0-DECAYRATE, env=env)
        l, rewards = q.learn()

        # ============================================================================
        csvName = 'q2_'+str(i)+'.csv'
        with open(csvName,'w', encoding='utf-8-sig', newline='') as qla1:
            writer1 = csv.writer(qla1)
            for item in rewards:
                writer1.writerow([item])

if __name__=="__main__":
    print(os.getcwd())
    # os.chdir('Q25')
    os.chdir('taxiQwDelay')


    run(30)
