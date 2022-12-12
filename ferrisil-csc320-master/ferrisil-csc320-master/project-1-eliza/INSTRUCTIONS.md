# Project 1: A Chatbot 
<!-- TOC -->

- [Project 1: A Chatbot](#project-1-a-chatbot)
  - [Description](#description)
  - [## Targets](#-targets)
  - [- [ ] CL.3 create SSH keys](#----cl3-create-ssh-keys)
  - [- [ ] SS.1P Conversational Agents (Practical)](#----ss1p-conversational-agents-practical)
  - [Setup:](#setup)
  - [Step 1: Learn how it works](#step-1-learn-how-it-works)
  - [Step 2: Customize it](#step-2-customize-it)
  - [Step 3: A better changePerson()](#step-3-a-better-changeperson)
  - [Step 4:  A memory](#step-4--a-memory)
  - [Step 5: Make it your own](#step-5-make-it-your-own)
  - [Challenge](#challenge)
  - [How and what to hand in:](#how-and-what-to-hand-in)

<!-- /TOC -->

## Description

[A fun video to watch](https://www.youtube.com/embed/WnzlbyTZsQY)

As you'll be reading about this week, ELIZA was a computer program written by Joseph Weizenbaum in the 1960s which incorporated some basic natural language processing in order to create an artificial "psychotherapist".  By taking a user's input and performing some simple matches and substitutions, it was able to carry on a conversation with a human.  Although not sophisticated by today's standards, ELIZA was a sensation at the time, with some people suggesting that it could supplant human psychoanalysts completely.    Richard Wallace's ALICE chatbot can be considered an evolution of the original ELIZA, and has won the Loebner prize (a modern iteration of the Turing Test) on multiple occasions.

The aim of this programming assignment is to re-familiarize yourself with Python, the programming language which we'll be using throughout the semester.   In the process, you'll also learn about how hard (or easy) it can be for a computer to "pass" as human.

Importantly you'll also be able to demonstrate proficiency in the following targets:


## Targets
---
- [ ] CL.1 navigate the command line
- [ ] CL.2 create/move/delete folders 
- [ ] CL.3 create SSH keys
---

- [ ] G.2 pull a repository
- [ ] G.3 commit and push to a repository
- [ ] G.5 writing Markdown

---
- [ ] PY.1	Python Programming (editing, compiling)
- [ ] PY.2	Python Debugging (your code, other's code)
- [ ] PY.3	Command-Line Python

---
- [ ] SS.1A Conversational Agents (Analytical)
- [ ] SS.1P Conversational Agents (Practical)
---

## Setup:

You should have already created an ssh keypair as part of the SSH tutorial. 

* log into cs-gitlab.union.edu
* clone the csc320-s22 project into your personal directory
  * `git clone git@cs-gitlab.union.edu:rieffelj/csc320-w20.git` (yes, I know the repo is called w20, but trust me it is the right one)
* I have created a class repository for you as well, named username-csc320. Clone it into your personal directory too.
* copy the project-1 directory from the class repo into your personal repo
  * `git add`, `commit`, and `push` the project-1 files to your personal repository


---
## Step 1: Learn how it works

Run the copy of `eliza.py` that is in your repo from the command line 

`python eliza.py`


Inspect the code to begin to understand how it works. I recommend  you use Microsoft Visual Studio Code, Atom, or Sublime as a text editor.  Please *do not* use IDLE or eclipse.

Here's a brief overview of the code.


* `driverLoop()` - this is the main loop which starts the conversational agent
* `generateReply()` - given an input string, this will return a reply

---
## Step 2: Customize it

* Add a few new hedges, some new prefixes, and at least one entirely new reply-producing function to `ReplyFunctionList`.

* Now, add some more pairs to the PronounDictionary (see Step 3 below).


---
## Step 3: A better changePerson()


Currently, the `PronounDictionary` will change first person to second person, but not vice versa.


Add appropriate values to the PronounDictionary to make that happen (i.e. 'you':'i'), and test it out.   It seems a bit buggy, why?


To resolve this, replace `changePerson()` with a new function called `switchPerson()`.  There are several possible ways you can do this - you can use the `map` function of python, map  `swapPerson` to the word list, or use the `string.replace()` function to swap key/value pairs in the input sentence.  There are any bynber of other approaches too. Each of these approaches has pitfalls that you might encounter, so be wary!


---
## Step 4:  A memory 

Develop a way to keep track of a list of all prior patient inputs, and use them to enrich the conversation with new prefixes, such as "Earlier you said that...."


---
## Step 5: Make it your own


Add as many additional bells and whistles as you want.  The aim is to not to make it enough to pass the Turing Test (this is quite hard) but to have fun with it - and just as importantly for *me* to have fun with it!

---
## Challenge 

Consider implementing one of the following
* Find a classmate and figure out how to have your agents (programatically) talk to each other
* Create a twitter or slack ChatBot

---
## How and what to hand in:

Your `project-1-eliza` folder should contain:
  * your `eliza.py`
  * a writeup, in the form of a README.md, with an annotated transcript of some of the chats.

`add/commit/push` your code to your repo.

