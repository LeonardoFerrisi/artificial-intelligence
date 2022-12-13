# Genetic Algorithms

## Description
This assignment is relatively straightforward:  Try to replicate Melanie Mitchell's Royal Roads paper.  Specifically, evolve bitstrings using her two different RR measures in order to assign fitness.

There's deliberately no starter code, but your programs must be written in python and able to run on department machines. You may use scipy and numpy and matplotlib as you see fit.  You'll need to gather data and then display it visually  -  I'm fine with a a Jupyter (or Google Colab) notebook.  


## Targets
- [ ] HS.1.A	Stochastic Search and Hillclimbing
- [ ] HS.1.P	Stochastic Search and Hillclimbing
- [ ] HS.2A 	Genetic Algorithms																			
- [ ] HS.2P 	Genetic Algorithms																			

Some starter parameters for your Hillclimber and GA (where relevant):

* 64-bit bitstrings
* Population size 128
* simple fitness proportional selection
* you may implement sigma scaling (described on the first page of this paper) if you so choose.
* Crossover Rate: 0.7 per pair of parents
  * i.e. 70% of new members added to population come as a result of crossover (followed by mutation), and the remainder via mutation only.
* Mutation Rate: 0.005 per locus.
    note: mutation is applied both to offspring of a single parent as well as to offspring created through crossover.
Gathering Data:

At a minimum you'll be running three experiments:

* Hillclimber
* RR GA
* RR GA without intermediate levels
 
For each experiment (with same parameters), be sure to do 30 independent  runs with different random seeds.  Keep track of the *best* fitness for each generation.    Your graphs (below) of fitness over time should then aggregate those 30 data sets to display the min/max/mean fitness over the 30 runs. 

Each run of an experiment should produce a file of data saved in a text format (csv), and should contain a header with the random seed for that run, as well as the parameter settings, followed by column headings and data (you may use the PANDAS package if you'd like) 

Graph the data from each experiment onto a single graph with shared axes. *The x axis of your graphs should be fitness evaluations not generations*.

You may plot in Google Sheets if you insist.

Follow Mitchell's guidance regarding Hillclimbing parameters and duration of experiment.
Additional Experiments:

As time allows, do design and run experiments to answer the following questions.

* what effect, if any, does two-point crossover, rather than single-point have on the results?
* what effect, if any, does uniform crossover, rather than single-point have on the results?
* what effect does a different fitness function (such as HIFF) have on the results?

# Submit

 * all code in the project-5-ga folder in your repo, containing all of your code and data
 * a nicely formatted Markdown writeup of your results.  Be sure to analyze your results and try to explain them!  
