from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from textblob import TextBlob
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'sentiment/sentiment.html', {'title': 'Sentiment Analysis'})

def sentiment(request):
    consumer_key = 'LnNMAVgk4sg8oFuzi0A7OqNmm'
    consumer_secret = 'eldO1tzF61vN9d5oLjTv2K50cFAUQhN7tShJVpIkeTVVK9fJHI'

    access_token = '850268858506031104-v3drln7zpYQfgxdP7sGtLA2eYa7v0dX'
    access_token_secret = 'IDxeSexLZ1Iq7eFh4ywLzee0VAR0wYrBRr7L8i3dL6V2T'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    keyword = request.POST['keyword']

    public_tweets = api.search(keyword)

    #for tweet in public_tweets:
        #twee = (tweet.text)
        #analysis = TextBlob(tweet.text)
        #ana= analysis.sentiment
    #return render(request, 'sentiment/analysis.html', {'tweet':twee})

    N = 1000  # Number of Tweets
    Tweets = tweepy.Cursor(api.search, keyword).items(N)
    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    for tweet in Tweets:
        # print tweet.text
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:  # Negative
            neg += blob.sentiment.polarity
            neg_count += 1
        elif blob.sentiment.polarity == 0:  # Neutral
            neutral_count += 1
        else:  # Positive
            pos += blob.sentiment.polarity
            pos_count += 1

    total_tweets = N
    #positive = round((float(pos_count/N)*100), 2)
    #negative = round((float(neg_count/N)*100), 2)
    #neutral = round((float(neutral_count/N)*100), 2)

    #return [['Sentiment', 'no. of tweets'], ['Positive', pos_count], ['Neutral', neutral_count], ['Negative', neg_count]]

    return render(request, 'sentiment/analysis.html', {'pos_count':pos_count, 'neg_count':neg_count,
                                                       'neutral_count':neutral_count, 'keyword': keyword,
                                                       'title': 'Analysis Result'})














