"""
Python program to retweet public hashtag #NBA2K21
"""

import tweepy
import time

consumer_key = 'xxxxxxxxxxexxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = '#NBA2K21'
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)


def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print('retweet task is done!')
            time.sleep(2)
        except tweepy.tweepError as e:
            print(e.reason)
            time.sleep(2)


searchBot()
