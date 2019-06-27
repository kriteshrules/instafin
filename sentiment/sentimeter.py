import tweepy
from textblob import TextBlob


class TwitterSentiment:
    def __init__(self, keyword):
        self.keyword = keyword
        self.consumer_key = 'LnNMAVgk4sg8oFuzi0A7OqNmm'
        self.consumer_secret = 'eldO1tzF61vN9d5oLjTv2K50cFAUQhN7tShJVpIkeTVVK9fJHI'
        self.access_token = '850268858506031104-v3drln7zpYQfgxdP7sGtLA2eYa7v0dX'
        self.access_token_secret = 'IDxeSexLZ1Iq7eFh4ywLzee0VAR0wYrBRr7L8i3dL6V2T'
        self.N = 100  # Number of Tweets
        self.neg = 0.0
        self.pos = 0.0
        self.neg_count = 0
        self.neutral_count = 0
        self.pos_count = 0
        self.tweetp = []
        self.tweetn = []

    def run(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        Tweets = tweepy.Cursor(api.search, self.keyword).items(self.N)

        for tweet in Tweets:
            # print tweet.text
            blob = TextBlob(tweet.text)
            if blob.sentiment.polarity < 0:  # Negative
                self.neg += blob.sentiment.polarity
                self.neg_count += 1
                self.tweetn.append(tweet.text)
            elif blob.sentiment.polarity == 0:  # Neutral
                self.neutral_count += 1
            else:  # Positive
                self.pos += blob.sentiment.polarity
                self.pos_count += 1
                self.tweetp.append(tweet.text)

        self.newtweetn = list(set(self.tweetn))
        self.newtweetp = list(set(self.tweetp))
