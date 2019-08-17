from django.shortcuts import render
import tweepy
from textblob import TextBlob
from django.contrib.auth.decorators import login_required
from sentiment.googlesentiment import Analysis


@login_required
def home(request):
    return render(request, 'sentiment/sentiment.html', {'title': 'Sentiment Analysis'})


def sentiment(request):
    consumer_key = 'P3gunyBoRZcRl6FxrE9LqURlC'
    consumer_secret = 'EPYBXJ2YgTzykmE5qdJCLmbicwW3xqquXbxlJDIUmvDuvi5TQ3'

    access_token = '850268858506031104-6KxzqF7BxK52takTqkcgt1lTiaPVAm2'
    access_token_secret = 'm6PWJMdP8inGoxxIsKRTNkUEkR3zIXRimUmyoD6rIj91X'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    keyword = request.POST['keyword']

    public_tweets = api.search(keyword)

    N = 1000  # Number of Tweets
    Tweets = tweepy.Cursor(api.search, keyword).items(N)
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

    context = {
        'newtweetn':newtweetn, 'newtweetp':newtweetp, 'pos_count':pos_count,
        'neg_count':neg_count,'neutral_count':neutral_count, 'keyword': keyword,
        'title': 'Analysis Result'
    }

    return render(request, 'sentiment/analysis.html', context)


def googlesentiment(request):
    term = request.POST['googlekeyword']
    analysis = Analysis(term)
    analysis.run()
    context = {
        "Term": term,
        "Sentiment": analysis.sentiment,
        "Subjectivity": analysis.subjectivity,
        "gheadline_pos": analysis.gheadline_pos,
        "gheadline_neu": analysis.gheadline_neu,
        "gheadline_neg": analysis.gheadline_neg,
        "pos_count": analysis.pos_count,
        "neg_count": analysis.neg_count,
        "neu_count": analysis.neu_count,
        "title": 'Google Sentiment',
        "urls": analysis.urls,
        "mylist": analysis.mylist,
    }
    return render(request, 'sentiment/google_sentiment.html', context)



