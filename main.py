import json
from requests_oauthlib import OAuth1Session
import os
import argparse


def getTweetData(keyword, twitter, max_id=-1, url="https://api.twitter.com/1.1/search/tweets.json"):
    """
    最新のデータから、APIで取得可能な期間(七日前)まで遡ってデータを取得する。
    Rate limit: 450req/15min (Application Auth)
    """
    params = {
        'q': keyword,
        'count': 100,
        'result_type': 'recent',
        'exclude': "retweets",
        'tweet_mode': 'extended',
        'max_id': max_id
    }
    tweets = []
    res = twitter.get(url, params=params)
    if res.status_code == 200:
        sub_tweets = json.loads(res.text)["statuses"]
        tweet_ids = []
        for tweet in sub_tweets:
            tweet_ids.append(int(tweet['id']))
            tweets.append(tweet)
        if len(tweet_ids) > 0:
            max_id = min(tweet_ids) - 1
    else:
        print("Faild: {}".format(res.status_code))
        return [], max_id, 0

    print("Tweets: {}".format(len(tweets)))
    return tweets, max_id


if __name__ == "__main__":
    import output
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

    twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET,
                            ACCESS_TOKEN, ACCESS_SECRET)

    import time
    import argparse
    parser = argparse.ArgumentParser(description="TwitterAPI")
    parser.add_argument("query", type=str,
                        help="Twitter search query (e.g. from:kinkidaigakuPR)")
    parser.add_argument("filepath", type=str, help="csv file path")
    args = parser.parse_args()

    max_id = -1  # 最新max_id=-1で
    while True:
        tweets, max_id = getTweetData(
            args.query, twitter, max_id=max_id)
        output.write_tweets(tweets, args.filepath)
        if len(tweets) == 0:
            # 無駄にアクセスしない
            break
        time.sleep(1.5)  # 2秒間隔アクセスなら問題ない
