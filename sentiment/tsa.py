import tweepy
from textblob import TextBlob

consumer_key = 'LnNMAVgk4sg8oFuzi0A7OqNmm'
consumer_secret = 'eldO1tzF61vN9d5oLjTv2K50cFAUQhN7tShJVpIkeTVVK9fJHI'

access_token = '850268858506031104-v3drln7zpYQfgxdP7sGtLA2eYa7v0dX'
access_token_secret = 'IDxeSexLZ1Iq7eFh4ywLzee0VAR0wYrBRr7L8i3dL6V2T'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = input('Enter the keyword--')

public_tweets = api.search(keyword)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


