from read_tweets_features import *
from get_keywords import *


def generate_message(bucket):
    tweets_features = read_tweets_features(bucket)

    # 検索キーワードを取得
    keywords = get_keywords(tweets_features)
    kw_str = ' '.join(keywords)

    message = '現在の {} の様子です。\n\n#LLNow'.format(kw_str)

    return message
