from twitter import *
import config
import sys
import time

auth = OAuth(
    consumer_key= str(config.twitter['consumerKey']),
    consumer_secret=str(config.twitter['consumerSecret']),
    token=str(config.twitter['accessToken']),
    token_secret=str(config.twitter['accessTokenSecret'])
)

t = Twitter(auth=auth, retry=True)

def get_new_tweets():
    x = t.search.tweets(q="instagram.com")
    for status in x['statuses']:
        try:
            s = status['entities']['urls'][0]['expanded_url']
            print  s
        except:
            e = sys.exc_info()[0]
            sys.stderr.write(str(e)+'\n')


while True:
    get_new_tweets()
    time.sleep(4)
