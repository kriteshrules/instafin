import tweepy
from textblob import TextBlob


def primary(input_hashtag):
    consumer_key = 'LnNMAVgk4sg8oFuzi0A7OqNmm'
    consumer_secret = 'eldO1tzF61vN9d5oLjTv2K50cFAUQhN7tShJVpIkeTVVK9fJHI'

    access_token = '850268858506031104-v3drln7zpYQfgxdP7sGtLA2eYa7v0dX'
    access_token_secret = 'IDxeSexLZ1Iq7eFh4ywLzee0VAR0wYrBRr7L8i3dL6V2T'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    N = 100  # Number of Tweets
    Tweets = tweepy.Cursor(api.search, q=input_hashtag).items(N)
    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    tweetp = []
    tweetn = []

    for tweet in Tweets:
        # print tweet.text
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:  # Negative
            neg += blob.sentiment.polarity
            neg_count += 1
            tweetn.append(tweet.text)
        elif blob.sentiment.polarity == 0:  # Neutral
            neutral_count += 1
        else:  # Positive
            pos += blob.sentiment.polarity
            pos_count += 1
            tweetp.append(tweet.text)

    newtweetn = list(set(tweetn))
    newtweetp = list(set(tweetp))

    #return newtweetn, newtweetp, pos_count, neg_count, neutral_count, input_hashtag

    return [['newtweetn', newtweetn], ['newtweetp', newtweetp], ['pos_count', pos_count], ['neg_count', neg_count],
            ['neutral_count', neutral_count], ['keyword', input_hashtag], ['title', 'Analysis Result']]
