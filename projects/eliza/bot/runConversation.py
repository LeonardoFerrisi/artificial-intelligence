import eliza
import azile # CLONE OF MY CHATBOT
# import traveller

if __name__ == '__main__':
    e = eliza.FerrisiChatAgent()
    a = azile.FerrisiChatAgent()
    # t = traveller.ChatAgent() # traveller can be you!

    e.converse(chatBot2=a, ourName="ELIZA", theirName="AZILE", timed=True, runtime=10)