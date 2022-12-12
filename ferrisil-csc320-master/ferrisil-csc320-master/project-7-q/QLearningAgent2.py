from gym import Env, spaces, utils
import numpy as np
import coffeegame
import time
import math
# import getch

class QLearningAgent2:

    def __init__(self, alpha, gamma, epsilon, maxSteps, maxEp, decay, env: Env):
        
        self.learningRate = alpha # ALPHA
        self.discountRate = gamma # GAMMA
        self.explorationRate = epsilon # EPSILON
        self.decayRate = decay

        self.maxStepsPerEpisode = maxSteps
        self.maxEpisodes = maxEp

        # sizes
        self.qSize = env.observation_space.n
        self.actionSize = env.action_space.n

        # generate table
        self.Qtable = np.zeros((self.qSize, self.actionSize))

        self.env = env
        self.state = self.env.reset()

        # self.stats = # we'll do this later for plotting results

    def learn(self):
        """
        Do Q Learning
        """

        rewards = []

        # Generate policy 
        policy = self.generatePolicy()
        
        decay = 1.0

        # for every episode 
        for episode in range(self.maxEpisodes):            

            self.state = self.env.reset()

            currentReward = 0
            stepsTaken = 0

            for i in range(self.maxStepsPerEpisode):

                # get probabilities from the current state
                action_prob = policy(self.state, decay=decay)

                action = np.random.choice(np.arange(len(action_prob)), p = action_prob) # get a random choice, use p param as prob of action

                # use action, get reward, move on to next state

                new_state,reward,done, info = self.env.step(action)

                #the q learning magic happens here.
                self.Qtable[self.state,action] = self.Qtable[self.state, action] * (1 - self.learningRate) + \
                                        self.learningRate * (reward + self.discountRate * np.max(self.Qtable[new_state, :]))

                # self.printQTable()
                stepsTaken+=1

                if (done):
                        #reset if game is over
                    # self.state = self.env.reset()
                    # rewards.append(currentReward/(i+1))
                    break

                else:
                        #otherwise update state
                    self.state = new_state
                    currentReward+=reward
                    # self.printQTable()
            # rewards.append(currentReward)
            rewards.append(currentReward/stepsTaken)

            decay *= self.decayRate
            print(f"Completed Episode {episode}, Average reward = {currentReward/stepsTaken}, currentReward: {currentReward}, decay: {decay}")

        return self.Qtable, rewards


    def __getNextState(self, stateID:int, action:int):
        """
        Gets the nextState and its corresponding ID
        based on an input stateID and action
        """

        possibleNexts = {
        0:(stateID, stateID+3, stateID+1, stateID),
        1:(stateID-1, stateID+3, stateID+1, stateID),
        2:(stateID-1, stateID+3, stateID, stateID),
        3:(stateID, stateID+3, stateID+1, stateID-3),
        4:(stateID-1, stateID+3, stateID+1, stateID-3),
        5:(stateID-1, stateID+3, stateID, stateID-3),
        6:(stateID, stateID, stateID+1, stateID-3),
        7:(stateID-1, stateID, stateID+1, stateID-3),
        8:(stateID-1, stateID, stateID, stateID-3)
        }
        
        currentState = possibleNexts[stateID]
        nextStateID = currentState[action]
        nextState = self.Qtable[nextStateID]
        return nextState, nextStateID

    def __getBestActionFor(self, state, stateID, verbose=False):
        """
        Finds the action with the highest reward for a given stateID and its correpsonding state
        containing up to 4 possible actions (LEFT, DOWN, RIGHT, UP)
        """
        bestActionVal = float(-math.inf)
        bestAction = 0
        for i in range(len(state)):
            actionVal = state[i]
            if actionVal > bestActionVal:
                    if verbose: print(f"- bestAction now: {i},{actionVal}")
                    bestActionVal = actionVal
                    bestAction = i
            else:
                continue
        
        nextState, nextStateID = self.__getNextState(stateID, bestAction)
        return (bestAction, bestActionVal), nextState, nextStateID

    def behave(self):
        """
        Following a completed QLearning set of episodes, follow the most optimal path
        in the resulting QTable
        """
        self.state = self.env.reset()

        optimalPath = []

        start = self.Qtable[0]

        # Get best action for start
        (bestAction, bestActionVal), nextState, nextStateID = self.__getBestActionFor(start, 0)
        optimalPath.append((bestAction, bestActionVal))

        # while loop    
        while nextStateID!=8:
            (bestAction, bestActionVal), nextState, nextStateID = self.__getBestActionFor(nextState, nextStateID)
            optimalPath.append((bestAction, bestActionVal))

        for actionTuple in optimalPath:

            action = actionTuple[0]
            actions = {0:"Left", 1:"Down", 2:"Right", 3:"Up"}
            print(f"Action: {actions[action]}:[{actionTuple[1]}]")

            self.printQTable()

            new_state,reward,done, info = self.env.step(action)
            self.Qtable[self.state,action] = self.Qtable[self.state, action] * (1 - self.learningRate) + \
                                        self.learningRate * (reward + self.discountRate * np.max(self.Qtable[new_state, :]))

            if (done):
                #reset if game is over
                self.state = self.env.reset()
                self.printQTable()
                return self.Qtable

            else:
                #otherwise update state
                self.state = new_state
                # self.printQTable()

        return self.Qtable

    def enableRendering(self):
        self.env.render()

    def disableRendering(self):
        self.env.reset()
        # maybe resetting will keep it un-rendered...

    def generatePolicy(self):
        """
        Uses an epsilon-greedy policy based on the q table

        """
        def policyFunc(state, decay):

            action_prob = np.ones(self.actionSize, dtype=float)* (self.explorationRate*decay / self.actionSize)

            bestAction = np.argmax(self.Qtable[state])

            action_prob[bestAction] += float((1.0 - self.explorationRate*decay))
            return action_prob

        return policyFunc

    def printQTable(self):
        qt = self.Qtable
        rows,cols  = qt.shape
        print("State ||    LEFT  |   DOWN  |   RIGHT  | UP     |")
        print("-------------------------------------------------")
        for row in range(rows):
            outstr = "   "+str(row)+"  "
            col = qt[row]
            for val in col:
                outstr+='    {:6.2f}'.format(val)
            print(outstr)

        print("\n")


if __name__ == "__main__":
    env = coffeegame.CoffeeEnv()
    q = QLearningAgent2(alpha=0.1, gamma=0.6, epsilon=0.5, maxSteps=20, maxEp=1000, decay=0.98, env=env)
    print("\n\nEmptyTable:")
    q.printQTable()
    print("================\n\n")

    l, rewards = q.learn()

    print(str(rewards))

    print("\n==============================\n")
    print("\n====== Episodes completed, inititating behavior ======\n")
    print("\n==============================\n")
    time.sleep(5)

    m = q.behave()
    # q.printQTable()

