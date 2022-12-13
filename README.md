##### The following is a collection of projects demonstrating the fundamentals of Artificial Intelligence

# Fundamentals of Artificial Intelligence

<br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li>
        <a href="#projects">Projects</a>
        <ul>
            <li><a href="#**Conversational Agents - Origins of AI**">Converstational Agents</a></li>
            <li><a href="#Searching with AI">Searching with AI</a></li>
            <ul>
                <li><a href="# **State Space Search**">State Space Search</a></li>
                <li><a href="# **A - Star Search**">A* Search</a></li>
            </ul>
            <li><a href="#Game - Playing Artificial Intelligence">Game - Playing AI<a></li>
            <ul>
                <li><a href="# **Konane (Hawian Checkers) using Alpha - Beta Minimax Search**">Alpha Beta Minimax with Konane</a></li>
            </ul>
            <li><a href="# **Genetic Algorithms**">Genetic Algorithms</a></li>
            <li><a href="# **Artificial Neural Networks**">Artificial Neural Networks</a></li>
            <li><a href="# **Reinforcement Learning**">Reinforcement Learning</a></li>
            <li><a href="# **Classifying Handwriting with Neural Networks**">Training AI to read handwriting</a></li>
        </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Setup</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br>

# 

### About

    some text

### Getting Started

    some text

#### Prerequisites

    some text

#### Setup

    some text

### Usage

    some text


#

## Projects

#

### **Conversational Agents**

[ELIZA](https://en.wikipedia.org/wiki/ELIZA) was a computer program written by Joseph Weizenbaum in the 1960s which incorporated some basic natural language processing in order to create an artificial "psychotherapist".  By taking a user's input and performing some simple matches and substitutions, it was able to carry on a conversation with a human.  Although not sophisticated by today's standards, ELIZA was a sensation at the time, with some people suggesting that it could supplant human psychoanalysts completely. Richard Wallace's ALICE chatbot can be considered an evolution of the original ELIZA, and has won the Loebner prize (a modern iteration of the [Turing Test](https://plato.stanford.edu/entries/turing-test/)) on multiple occasions.

The aim of this project was to implement a chatbot in the likeness of ELIZA using Python. In the process, gaining a feel for the challenge of getting a program to "pass" as human.

This is a very *bare bones* implementation of randomly selecting responses and formatting them to sound as such. ( The original ELIZA used a similar functionality to format random responses to sound more natural ).

[ELIZA Project](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/eliza)

# 

## Searching with AI

<br>

### **State Space Search**

State space search is a general approach that can be applied to any problem domain that is deterministic, discrete, and static. 

In Chapter 3 of Artificial Intelligence: A Modern Approach by Russel and Norvig, they discuss a number of applications for this approach including route finding, VLSI layout, and automatic assembly sequencing. 

Here, the project's goal is to formulate a new problem so that state space search can be used. I've also taken the liberty of recording all of the unique states that have been visited in a dictionary, and only adding unvisited states to the search queue so as to improve the efficiency of the state space search.

[State Space Search Project](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/statespacesearch)

<br>

### **A - Star Search**

The goal of this project was to apply [A* search](https://brilliant.org/wiki/a-star-search/) to the eight puzzle problem. The eight puzzle consists of a three by three board with eight numbered tiles and a blank space. A tile adjacent to the blank space can slide into the space. The object is to figure out the steps needed to get from one configuration of the tiles to another.

[A* Search Project](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/astar)

<br>

## Game - Playing Artificial Intelligence

<br>

### **Konane (Hawian Checkers) using Alpha - Beta Minimax Search**

The game - player I implmented for this project works by using alpha beta minimax to play Konane. The algorithm is inspired by psuedocode regarding minimax for
Konane players in Russell and Norvig's Artifical Intelligence: A Modern Approach book.

The static evaluator is a weighted ratio of the number of remaining moves for my player versus the oponents. I took inspiration from the several
evaluation methods detailed in "Teaching a Neural Network to Play Konane" which provides a graph describing the usefullness of several Konane 
static evaluation techniques. 

In writing this up I considered using the difference between the number of pieces I have versus my oponents, however this ended up making the code run longer than prefered, even when attempted by only using the difference metric for the first half of the game and the weighted ratio for the second half.

I also implemented a randomizer that chooses randomly between minimax nodes of the same value.

I deterimined which features were most effective as a result of copious trial and error, eventually looping back to the fundamentals with Russel and Norvigs description of Alpha Beta Minimax.

[Konane Minimax Project](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/konane)

<br>

### **Genetic Algorithms**

This project was relatively straightforward:  Try to replicate Melanie Mitchell's Royal Roads paper.  Specifically, evolve bitstrings using her two different RR measures in order to assign fitness.

There's deliberately no starter code, but your programs must be written in python and able to run on department machines. You may use scipy and numpy and matplotlib as you see fit.  You'll need to gather data and then display it visually  -  I'm fine with a a Jupyter (or Google Colab) notebook.

[Genetic Algorithms](https://github.com/LeonardoFerrisi/artificial-intelligence/projects/genetic-algorithms)

<br>

### **Artificial Neural Networks**

The goal of this project was to implement artificial neural networks which is trained by utilizing back propogation.

[Artificial Neural Networks](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/artificialneuralnetworks)

<br>

### **Reinforcement Network**

The purpose of this project was to practice implementing Q-Learning in increasingly challenging environments, and to reinforce my understanding of reinforcement learning and Agent-Environment interactions.

[Q - Learning](https://github.com/LeonardoFerrisi/artificial-intelligence/projects/qlearning)


<br>

### **Classifying Handwriting with Neural Networks**

Artificial Neural Networks are designed to function based on concepts in learning inspired by what we know about how neurons in the human brain learn. Whereas a regular neuron communicates using ion gradients and a combination of charge and neurotransmitters between neurons, artificial neurons, better known as perceptrons take an input and apply it to an activation function defining what gets output.

Depending on the correctness of the output value as determined by simply propagating forward, the value is back propagated through and weights from the activation function to the output are altered until the value output matches the target. 

Some (most) problems however are far too complex for a single neuron (perceptron) to solve, so by wiring them up (and a ton of tweaking) complex problems can become solvable.

There are several variations on the Artificial Neural Network, which typically involves a small number of layers, an input, hidden and output layer. One such variation, the Deep Neural Network for example, involves a great many hidden layers allowing for more neurons and weights to adjust to targets.

This final project involved an attempt to classify MNIST data using an Artificial Neural Network.

[Teaching Neural Nets to read Handwriting](https://github.com/LeonardoFerrisi/artificial-intelligence/tree/main/projects/handwriting)
