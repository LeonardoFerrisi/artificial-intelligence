import csv
from QLearningAgent import QLearningAgent as Qla
from QLearningAgent2 import QLearningAgent2 as Qla2
import coffeegame
import numpy as np
import matplotlib.pyplot as plt
import os
import gym

def run(numTimes):

    # env = coffeegame.CoffeeEnv()
    
    # env = gym.make("Taxi-v3").env

    env = gym.make("Taxi-v3").env
    # env = gym.make('FrozenLake8x8-v1')


    for i in range(numTimes):
        
        q = Qla(alpha=0.1, gamma=0.6, epsilon=0.5, maxSteps=20, maxEp=20000, env=env)
        l, rewards = q.learn()

        # ============================================================================
        csvName = 'q_'+str(i)+'.csv'
        with open(csvName,'w', encoding='utf-8-sig', newline='') as qla1:
            writer1 = csv.writer(qla1)
            for item in rewards:
                writer1.writerow([item])

            # rewardPer1k = 0

            # for i in range(len(rewards)):
            #     if i % 100 == 0 and i!=0:
            #         writer1.writerow([rewardPer1k/i])
            #         rewardPer1k = 0
            #     else:
            #         rewardPer1k+=rewards[i]

# avgReward = sum(rewards)/len(rewards)
# print(f"Avg Reward for 3000 episodes with a max of 20 steps: {avgReward}")

if __name__=="__main__":
    print(os.getcwd())
    os.chdir('taxiQ')
    # os.chdir('flQ')


    run(30)
