from django.shortcuts import render
import tweepy
from textblob import TextBlob
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests


class Analysis:
    def __init__(self, term):
        self.term = term
        self.sentiment = 0
        self.subjectivity = 0
        self.pos_count = 0
        self.neg_count = 0
        self.neu_count = 0
        self.gheadline_pos = []
        self.gheadline_neu = []
        self.gheadline_neg = []
        self.url = 'https://www.google.com/search?q=={0}&source=lnms&tbm=nws'.format(self.term)

    def run(self):
        response = requests.get(self.url)
        #print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_results = soup.find_all('div', class_='st')
        for h in headline_results:
            #print(h.text)
            blob = TextBlob(h.get_text())
            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

            if blob.sentiment.polarity< 0:
                self.gheadline_neg.append(h.text)
                self.neg_count += 1
            elif blob.sentiment.polarity== 0:
                self.gheadline_neu.append(h.text)
                self.neu_count += 1
            elif blob.sentiment.polarity> 0:
                self.gheadline_pos.append(h.text)
                self.pos_count += 1


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
        "neu_count": analysis.neu_count
    }
    return render(request, 'sentiment/google_sentiment.html', context)



