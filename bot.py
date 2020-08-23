"""
Python program to reply, like and retweet when someone @mentions the bot using #sherlocked
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

file_name = 'last_seen.txt'


# Updating a status
# api.update_status("Sherlock twitter bot live!!!")


def read_last_seen(file_name):
    file = open(file_name, 'r')
    last_seen_id = int(file.read().strip())
    file.close()
    return last_seen_id


def store_last_seen(file_name, last_seen_id):
    file = open(file_name, 'w')
    file.write(str(last_seen_id))
    file.close()
    return


def reply():
    # Tweets from the timeline of the bot account
    tweets = api.mentions_timeline(read_last_seen(file_name), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(tweet.full_text)
        if '#sherlocked' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " It's elementary my dear watson!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(file_name, tweet.id)


while True:
    reply()
    time.sleep(16)
