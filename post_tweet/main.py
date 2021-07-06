from set_post_image import *
from set_twitter import *
from post_tweet import *


def main(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    set_post_image(bucket, key)
    twitter = set_twitter()
    post_tweet(twitter)
