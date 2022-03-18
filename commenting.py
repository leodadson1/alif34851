import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        tweet_id=tweet.id
        print(tweet_id)
        # api.retweet(tweet_id)
        


    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("2eVT67VNmTdY3rpzt2BHdWVhL", "B2ttH8vl78eIyS2DmLXMNxB4vAh7DhCEajn5GICSkB4fKdrPyS")
auth.set_access_token("1075083604353564672-xTHmNCFI5SHFUJu1HwLgp5ERCJ8ecW", "FkYRE8N06DRyNYCTpq3CBWcL5rG9BMFGBaA7Jd2aBudYQ")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])
