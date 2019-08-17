import tweepy
from textblob import TextBlob


class TwitterSentiment:
    def __init__(self, keyword):
        self.keyword = keyword
        self.consumer_key = 'P3gunyBoRZcRl6FxrE9LqURlC'
        self.consumer_secret = 'EPYBXJ2YgTzykmE5qdJCLmbicwW3xqquXbxlJDIUmvDuvi5TQ3'
        self.access_token = '850268858506031104-6KxzqF7BxK52takTqkcgt1lTiaPVAm2'
        self.access_token_secret = 'm6PWJMdP8inGoxxIsKRTNkUEkR3zIXRimUmyoD6rIj91X'
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
