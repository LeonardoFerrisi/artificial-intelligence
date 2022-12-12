# ELIZA, as implemented by Leonardo Ferrisi
#### CSC320 Spring 2022, John Riefell

### How to run ELIZA with user input:
- open a terminal and navigate to /project-1-eliza/bot/
- run python or python3 with "eliza.py" 
    
        python eliza.py

### How to have ELIZA chat with another chatbot
- navigate to /project-1-eliza/bot/runConversation.py
- open runConversation.py
- make sure the other chatBot is also in the /bot/ directory
    
### IMPORTANT!!!
##### In order to have your bot chat with this one add the following code into your ChatAgent() class

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

- In addition add the following to your instance variables

    self.canConverse = True

- Aaaaaaaand you should be all set!
- Go back to runConversation.py, make sure both bots are in the same directory and:
    - import my bot, declare its chat agent   
    - usage: 
        
            import eliza
            e = eliza.FerrisiChatAgent()
        
    - import your bot, and do the same
- call the function converse from either chatBot (you rembered to add the code right?)

        e.converse(yourChatbot) # other params are defaulted, feel free to edit them

- feel free to alter any of the parameters
- run the code using the same syntax you used to run the bot on its own!
        
        python runConversation.py

- enjoy!

# Transcript of some chats:
###### '>>' indicates user response

### Chat 1: The quarrel

    how are you today?
    >> I am feeling great today 
    Im glad to hear you are feeling great today
    >> How are you?
    What do you mean that {You said: How are you?}: 
    >> I mean to say you are the worst
    you mean to say I am the worst
    >> Yes, yes I do
    That's great! : 
    >> Oh is it now?
    Ahh I see : 
    >> You see what?
    Why do you say that {You said: You see what?}: 
    >> I dont like you
    Well I never! *Slaps you*
    >> Ah, it's a duel you want then???
    How dare you! :
    >> How dare I? How dare you!
    How dare I? How dare you!
    >> Thats it! Good day to you !
    Can you kindly un-say this :
    >> Goodbye
    Okay, goodbye then.


### Chat 2: Two bots just vibing
    [ELIZA]: how are you today? , [JOSHBOT]: how am I today?
    [ELIZA]: Can you kindly un-say this  , [JOSHBOT]: Thank you for being respectful
    [ELIZA]: How dare you!  , [JOSHBOT]: Thank you for being respectful
    [ELIZA]: Earlier you said that... Well I never! *Slaps you*  , [JOSHBOT]: I'm not sure what you mean
    [ELIZA]: I could not disagree more  , [JOSHBOT]: I remember that earlier you said: Earlier you said that... How dare you!  .... Is:  I could not disagree more    related to this??
    [ELIZA]: you remember that earlier I said: Earlier I said that... How dare you! .... Is: you could not disagree more related to this??, [JOSHBOT]: That's life
    [ELIZA]: That's really something...  , [JOSHBOT]: I appreciate the respectful language
    [ELIZA]: you appreciate the respectful language, [JOSHBOT]: I appreciate the insight
    [ELIZA]: Earlier you said that... Can you kindly un-say this  , [JOSHBOT]: That's life
    [ELIZA]: Earlier you said that... Well I never! *Slaps you*  , [JOSHBOT]: Wait what
    [ELIZA]: Earlier you said that... Wait what, [JOSHBOT]: That is fascinating
    [ELIZA]: Earlier you said that... That is very interesting  , [JOSHBOT]: I understand. Earlier I said that... That is very interesting
    [ELIZA]: you understand. Earlier you said that... That is very interesting, [JOSHBOT]: That's life
    [ELIZA]: I could not disagree more  , [JOSHBOT]: Thank you for being respectful
    [ELIZA]: Earlier you said that... I could not disagree more  , [JOSHBOT]: That's life
    [ELIZA]: Earlier you said that... I do not understand what you mean when you say that That's life , [JOSHBOT]: I appreciate the respectful language
    [ELIZA]: Earlier you said that... Well I never! *Slaps you*  , [JOSHBOT]: That is fascinating
    [ELIZA]:  , [JOSHBOT]: I remember that earlier you said: Why do you say that Why do I say that? Are you sure that you remember that earlier I said: What do I mean that I could not disagree more .... Is: What do I mean that I could not disagree more related to this?? .... Is:     related to this??
    [ELIZA]: What do you mean that you remember that earlier I said: Why do I say that Why do you say that? Are I sure that I remember that earlier you said: What do you mean that you could not disagree more .... Is: What do you mean that you could not disagree more related to this?? .... Is: related to this?? , [JOSHBOT]: I appreciate the respectful language
    [ELIZA]: Are you sure that you appreciate the respectful language , [JOSHBOT]: Why are you acting like this? Are I sure that I appreciate the respectful language
    [ELIZA]: Why am I acting like this? Are you sure that you appreciate the respectful language, [JOSHBOT]: I remember that earlier you said: That's great!  .... Is:  Why am I acting like this? Are you sure that you appreciate the respectful language  related to this??



### Chat 3: ELIZA talking to themselves in the mirror

##### using the timed=True, runtime=10 parameters in converse method

    [ELIZA]: how are you today? , [AZILE]: Let's change the subject  
    [ELIZA]: Well I never! *Slaps you*  , [AZILE]: That's really something...  
    [ELIZA]: lol  , [AZILE]: Well I never! *Slaps you*  
    [ELIZA]: Can you kindly un-say this  , [AZILE]: Well I never! *Slaps you*  
    [ELIZA]: Earlier you said that... Well I never! *Slaps you*  , [AZILE]: Earlier I said that... Well you never! *Slaps you*
    [ELIZA]: I could not disagree more  , [AZILE]: Are you sure that you could not disagree more 
    [ELIZA]: I do not understand what you mean when you say that Are I sure that I could not disagree more , [AZILE]: That's great!  
    [ELIZA]: Ahh I see That's great! , [AZILE]: ... 
    [ELIZA]: ..., [AZILE]: ...
    [ELIZA]: Can you kindly un-say this  , [AZILE]: Earlier you said that... How dare you!  
    [ELIZA]: What do you mean that Earlier I said that... How dare you! , [AZILE]: Well I never! *Slaps you*  
    [ELIZA]: Goodbye, [AZILE]: Okay, goodbye then.