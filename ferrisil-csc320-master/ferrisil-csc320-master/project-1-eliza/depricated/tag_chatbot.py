from eliza import ChatAgent
import tweepy
from credentials import keys
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
import logging
import time


class TAG:

    def __init__(self, since_id=1):
        self.api = self.createAPI()
    
    def createAPI(self):
        CONSUMER_KEY = keys['consumer_key']
        CONSUMER_SECRET = keys['consumer_secret']
        ACCESS_TOKEN = keys['access_token']
        ACCESS_TOKEN_SECRET = keys['access_token_secret']

        # setup logger
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            api.verify_credentials()
        except Exception as e:
            logging.error("Error in making API", exc_info=True)
            raise e
        logging.info("API done!")
        return api

    def driverLoop(self):
        agent = ChatAgent(isTAG=True)

        self.since_id = 1
        
        while True:
            self.since_id = self.checkMentions(agent, self.since_id)
            self.logger.info("Waiting...")
            time.sleep(60)

    """
    Checks for mentions, if there is a mention, generate a reply
    """
    def checkMentions(self, bot, since_id):
        self.logger.info("Retrieving mentions")

        new_since_id = self.since_id
        for tweet in tweepy.Cursor(self.api.mentions_timeline, since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)

            if tweet.in_reply_to_status_id is not None:

                self.logger.info(f"Answering to {tweet.user.name}")
                m = bot.generateReply(tweet)
                self.api.update_status(
                    status=m, in_reply_to_status_id=tweet.id)
        return new_since_id

if __name__ == "__main__":
    t = TAG()
    t.driverLoop()