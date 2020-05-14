# coding: utf-8
import re


def write_tweets(tweets, filepath="tweets.csv"):
    """
    csv形式で保存
    """
    with open(filepath, mode="a") as f:
        for tweet in tweets:
            f.write(parse_tweets(tweet) + "\n")
        f.flush()


def parse_tweets(tweet):
    """
    保存する情報を取捨選択する
    """
    tweet_id = tweet["id_str"]
    created_at = tweet["created_at"]
    text = ""
    try:
        # 改行、タブ除去
        text = tweet.get("full_text", "-").strip(
        ).replace("\n", "").replace("\t", "")
        # URL除去
        text = re.sub(
            "(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "", text)
    except:
        import traceback
        traceback.print_exc()
        print(tweet)

    uid = tweet["user"]["id_str"]
    screen_name = tweet["user"]["screen_name"]
    favorite_count = tweet["favorite_count"]
    retweet_count = tweet["retweet_count"]
    # コンマ区切りで表記
    return "{},{},{},{},{},{},{}".format(tweet_id, created_at, uid, screen_name, favorite_count, retweet_count, text)
