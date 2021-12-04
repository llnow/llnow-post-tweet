import boto3
from boto3.dynamodb.conditions import Key
from check_datetime_in_range import *
from generate_bd_hashtag import *


def generate_message(mode):
    table = boto3.resource('dynamodb').Table('ll-now-search-keyword')

    # 検索キーワードを取得
    # default_keywordsを取得
    res = table.query(
        KeyConditionExpression=Key('type').eq('default')
    )
    default_keywords = [d['keyword'] for d in res['Items']]

    # option_keywordsを取得
    res = table.query(
        KeyConditionExpression=Key('type').eq('option')
    )
    option_keywords = []
    option_list = res['Items']
    for option in option_list:
        kw = option['keyword']
        since_str = option['since']
        until_str = option['until']
        if check_datetime_in_range(since_str, until_str):
            option_keywords.append(kw)

    keywords = default_keywords + option_keywords
    kw_str = ' '.join(keywords)

    # 生誕祭ハッシュタグを取得
    bd_hashtag = generate_bd_hashtag(mode)

    message = '現在の {} の様子です。\n\n{} #LLNow'.format(kw_str, bd_hashtag)

    return message
