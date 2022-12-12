import random
import sys
from phrases import RESPONSES, KWORDS
import time

class FerrisiChatAgent: 
    """ChatAgent - This is a very simple ELIZA-like computer program in python.
    Your assignent in Programming Assignment 1 is to improve upon it.

    I've created this as a python object so that your agents can chat with one another
    (and also so you can have some practice with python objects)
    """
    
    def __init__(self):
        responses = RESPONSES
        self.PronounDictionary = responses.PronounDictionary
        self.HedgeList = responses.HedgeList
        self.PrefixList = responses.PrefixList
        self.negResponses = responses.negResponses
        self.responsesToShyness = responses.responsesToShyness
        self.endPhrases = responses.endPhrases
        self.ReplyFunctionList = [self.generateHedge,self.switchPerson,self.changePersonAndAddPrefix, self.generateNegativeResponse] #this is what makes Python so powerful
        self.comfortResponses = responses.comfortResponses
        self.affirmingResponses = responses.affirmingResponses
        
        # canConverse: change to true if can be passed into converse function
        self.canConverse = True
        # # # # # # # # # # # # # #  

        self.LongTermMem = []
        
        self.quit = False
   
    def generateReply(self,inString):
        """Pick a random function, and call it on the input string """
        if inString == "":
            reply = random.choice(self.responsesToShyness)
        elif self.hasNegativeKWORD(inString):
            reply = self.generateComfortingResponse(inString)
        elif self.hasPositiveKWORD(inString):
            reply = self.generateAffirmingResponse(inString)
        elif self.isInsult(inString):
            reply = self.retort()
        elif inString==RESPONSES.davesRequest:
            reply = self.meme()
        elif inString in self.endPhrases:
            reply = "Okay, goodbye then."
            self.quit = True
        else:
            randFunction = random.choice(self.ReplyFunctionList) #pick a random function, I love python
            reply = randFunction(inString) 
        return reply

    def isInsult(self, inString):
        if inString in RESPONSES.attacks:
            return True
        else:
            return False
        
    def retort(self):   
        reply = random.choice(self.negResponses)
        return reply

    def generateComfortingResponse(self, inString):
        reply = self.switchPerson(inString)
        response = random.choice(self.comfortResponses)
        return ''.join([response, reply])
    
    def generateAffirmingResponse(self, inString):
        reply = self.switchPerson(inString)
        response = random.choice(self.affirmingResponses)
        return ''.join([response, reply])
    
    def meme(self):
        return RESPONSES.HALRESP

    def hasNegativeKWORD(self, inString):
        for string in inString.split(" "):
            if string in KWORDS.negativeAdjectives:
                # print("IS NEG")
                return True
        return False
    
    def hasPositiveKWORD(self, inString):
        for string in inString.split(" "):
            if string in KWORDS.positiveAdjectives:
                # print("IS POS")
                return True
        return False

    def driverLoop(self):
        """The main driver loop for the chat agent"""
        prompt = "how are you today?\n>> "
        while True:
            reply = input(prompt)
            response = self.drive(reply)
            prompt = response+"\n>>"
            # print("\n")
            # print(response)

    def drive(self, reply):
        """Runs once to collece a response"""
        if self.quit: quit()
        response = reply
        if response!="":
            triggeredMem ="" #left blank if nothing in longTerm mem
            if response in self.LongTermMem:
                triggeredMem="Earlier you said that... "
                self.LongTermMem.remove(response) # so that we can store it again
            else:            
                self.LongTermMem.append(response)
            reply = triggeredMem+self.generateReply(response)
        else:
            reply = self.generateReply("")
        return reply

    def swapPerson(self,inWord):
        """Replace 'I' with 'You', etc"""
        if (inWord in self.PronounDictionary.keys()):   #if the word is in the list of keys
            return self.PronounDictionary[inWord]

        elif (inWord in self.PronounDictionary.values()):
            for word in self.PronounDictionary.keys():
                if self.PronounDictionary[word]==inWord:
                    return word
        else:
            return inWord

    def changePersonAndAddPrefix(self,inString):
        reply = self.switchPerson(inString)
        randomPrefix = random.choice(self.PrefixList)
        return ''.join([randomPrefix,reply]) + " "

    def generateNegativeResponse(self, inString):
        toReturn = random.choice(self.negResponses) + " "
        return toReturn
  
    def generateHedge(self,inString):
        toReturn = random.choice(self.HedgeList) + " "
        return toReturn

    def switchPerson(self, inString : str):
        """change the pronouns etc of inString
        by iterating through the PrononDictionary
        and substituting keywords for subwords"""
        
        inWordList = str.split(inString)
        newWordList = map(self.swapPerson, inWordList)

        reply = ' '.join(newWordList)  #glue things back together
        return reply 

    # Converse logic ##########################

    def reply(self, inString):
        toReturn = self.drive(inString)
        # print(f"inString:{inString}, reply:{toReturn}")
        return toReturn

    def converse(self, chatBot2, ourName : str="Us", theirName : str="Them", timed=False, runtime=10):
        """The main driver loop for the conversation between chat agents"""

        prompt = "how are you today? "
        inString = prompt

        if chatBot2.canConverse != True:
            raise Exception("Chatbot is not able to converse! [bot must have converse method, repy method, and a boolean instance variable called 'canConverse' set to True]")
            # A chatBot we can converse with MUST have an instance variable indicating it canConverse, no exceptions

        if timed:
            startime = time.time()

        while True:
            # where inString is the prompt from me!
            responseFromChatbot2 = chatBot2.reply(inString) # Get their response from my input

            print(f"[{ourName}]: {inString}, [{theirName}]: {responseFromChatbot2}")
            # print(responseFromChatbot2) # The response from my other chatBot

            inString = self.reply(responseFromChatbot2) # get their input from my response

            if timed:
                if time.time() - startime > runtime:
                    inString = "Goodbye"
            
            time.sleep(1)

    #############################################
            
   #End of ChatAgent

if __name__ == '__main__': #will only be called if this is invoked directly by python, as opposed to included in a larger file
    
    #version checking
    MIN_PYTHON = (3, 7)
    assert sys.version_info >= MIN_PYTHON, "requires Python 3, run with `python3 eliza.py`"

    #program starts here
    random.seed() #if given no value, it uses system time
    agent = FerrisiChatAgent()
    agent.driverLoop()

