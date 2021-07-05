from set_twitter import *
from post_tweet import *


def main(event, context):
    twitter = set_twitter()
    post_tweet(twitter)
