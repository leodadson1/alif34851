import json
import tweepy
import time
tweets=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        
        
        tweets.append(tweet.id)

        print(tweets)

        if len(tweets) >=20:
            print("sleeping")
            time.sleep(60*20)
            tweets.clear()

        print("Gotten some")

        tweet_id=tweet.id
        #########COMMENT######

        comment="""
Project just launched! Available on PancakeSwap 🥞

The #IRN Utility Token 💻 aims to put an end to #crypto scams 🚨 and rug pulls with IRN Gems 💎 and IRN Launchpad 🚀 #cryptogem #Altcoins #altcoingem

✅Liquidity locked🔥

✅Dev doxxed🧑‍💻

✅Audited 🚨

Irntoken.one
        """
        favorite_coun=tweet.favorite_count
        print(favorite_coun)
        if favorite_coun >=5 and  tweet.retweet_count >=0:
            print(tweet.favorite_count)
            # print("The tweet is greater than 0 or equal to 0  ")
            api.update_status(status=comment, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata=True)
            print("Done")
            time.sleep(60*25)
        
    def on_error(self, status):
        print("Error detected")

API_KEY="ttsogJ8fmqcPytCAdYRwnQme8"
API_SECRET_KEY="3xesbpTKpxuObCmTEo8qWUTedqzhO0aDHwPNeibRDFxId5DzVW"
ACCESS_TOKEN="1504649262214254593-vQsIQ0DputdSfVVo4JYFNiTjDUPSbd"
ACCESS_TOKEN_SECRET="YYhsM4rLZ4tLiOImlZEFcHXxSAHGLanOqQOtXQJW8Qwwh"



# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)



tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["#cryptogem", "#altcoins", "#altcoinpicks", "#cryptopicks", "#small-cap"], languages=["en"])
