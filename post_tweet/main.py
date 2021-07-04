from set_twitter import *
from get_tweets_features import *
from post_tweet import *


def main(event, context):
    twitter = set_twitter()
    tweets_features = get_tweets_features()
    post_tweet(twitter, tweets_features)
