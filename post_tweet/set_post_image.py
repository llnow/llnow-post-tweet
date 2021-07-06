import boto3


def set_post_image(bucket, key):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)

    # ツイートする画像をs3からダウンロード
    image_path = '/tmp/' + key.split('/')[1]
    bucket.download_file(key, image_path)
