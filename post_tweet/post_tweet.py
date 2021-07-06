import json


def post_tweet(twitter):
    url_media = 'https://upload.twitter.com/1.1/media/upload.json'
    url_post = 'https://api.twitter.com/1.1/statuses/update.json'

    # 収集したツイートの情報
    # n_tweets = tweets_features['n_tweets']
    # latest_tweet_posted_time = tweets_features['latest_tweet_posted_time']
    # oldest_tweet_posted_time = tweets_features['oldest_tweet_posted_time']

    # 画像をアップロード
    files = {'media': open('/tmp/post_image.png', 'rb')}
    res_media = twitter.post(url_media, files=files)

    # レスポンスを確認
    if res_media.status_code != 200:
        print('Failed to upload media: {}'.format(res_media.text))
        exit()

    # media_id を取得
    media_id = json.loads(res_media.text)['media_id']

    # アップロードした画像を添付したツイートを投稿
    # message = 'test\n' \
    #           + '収集ツイート数:{}\n'.format(n_tweets) \
    #           + 'ツイート収集範囲：\n{}~{}\n'.format(oldest_tweet_posted_time, latest_tweet_posted_time) \
    #           + '#lovelive #LLNow'
    message = 'test\n' + '#lovelive #LLNow'
    params = {'status': message, 'media_ids': [media_id]}
    res_post = twitter.post(url_post, params=params)

    # レスポンスを確認
    if res_post.status_code == 200:
        print("Success.")
    else:
        print("Failed.")
        print(" - Response Status Code : {}".format(res_post.status_code))
        print(" - Error Code : {}".format(res_post.json()["errors"][0]["code"]))
        print(" - Error Message : {}".format(res_post.json()["errors"][0]["message"]))
        # {'errors': [{'code': 170, 'message': 'Missing required parameter: status.'}]}
