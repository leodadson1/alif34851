import json
import tweepy
import time 

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print("Gotten some")
        tweet_id=tweet.id
        #########COMMENT######
        comment="""
            I am just testing if My bot would work or not?
        """

        if tweet.favorite_count >=0 or  tweet.retweet_count >=0:
            print(tweet.favorite_count)
           
            api.update_status(status=comment, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)
            print("Done replying")
            time.sleep(60*25)
        
    def on_error(self, status):
        print("Error detected")

API_KEY="WI1tfVUIg0IJaQ1nuxS0WqnSX"
API_SECRET_KEY="0OusFSDVi4qy9akDZuBYSfxuTeQ1TSEdgm1tJUisFAfD4Zdmag"
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)



tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
######Hashtags#####
stream.filter(track=["Python", "#btc", "bitcoin"], languages=["en"])
