## Description

The purpose of this assignment is to give you practice implementing Q-Learning in increasingly challenging environments, and to reinforce your understanding of reinforcement learning and Agent-Environment interactions.

## Targets

- [ ] L.1.A - Q Learning
- [ ] L.1.P - Q Learning

## Setup:

Begin by pulling the class repository and copying the project 6 repository into your own class repository. Play around with the interactive program I wrote, and familiarize yourself with the code and concepts


## Step 1: A Simple Q-Learning Agent

Beginning with the qlearning.py agent, create a QLearningAgent class.  

QLearningAgents should have the following properties:

* a learning rate (alpha), initially 0.1
* a discount rate (gamma), initially 0.6
* an exploration rate (epsilon), initially 0.5 -- this is the probability that the agent picks a new random action, rather than the max q-table entry.
* a max number of steps that an agent takes *per episode*)
* a max number of episodes (i.e. from restart)
* a q-table (size determined by environment)
* the agent's constructor should have an environment as an argument (among others)

QLearningAgents should have the following methods (among others):

* learn: perform q-learning in the given environment
* behave: This is a test of if your q-learning algorithm has been successful.  It should choose actions from start state to finish state that maximize reward (presuming q-learning has worked)
* Your agent should be able to enable/disable rendering to speed up learning.
* Provide testing code so that I can run your agent myself and verify that it works (and that you tested your code).
* Run the Q-Learning over the CoffeeGame environment 

What learning rate, discount rate, and exploration rate seem to work best in each environment?

## Analytics:

Gather data on your agent's reward rate (typically, average reward per 1000 episodes) over time.  That is, does the per-episode reward increase between the first 1000 episodes and the second?

## Step 2: Decay Rates

(In a new file called QLearningAgent2.py)

Often, the exploration rate of an agent isn't fixed, instead it decays very slowly over the epochs. Start epsilon at 1 for your agent, and add an epsilon decay rate to your agent.  Re-run your experiments from Part 1.

## Step 4: Frozen Lake (Reach)

 and the FrozenLake-V0 environment.  

## Step 3: Implement in a new environment (Challenge)

Now try your reinforcement agent on the Taxi-V3 environment.   Gather Metrics.


