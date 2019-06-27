from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


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
        self.headings = []
        self.urls = []
        self.url = 'https://www.google.com/search?q=={0}&source=lnms&tbm=nws'.format(self.term)

    def run(self):
        response = requests.get(self.url)
        #print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_heading = soup.find_all('h3', class_='r')
        headline_results = soup.find_all('div', class_='st')
        headline_url = soup.select('.r a')
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
            else:
                self.gheadline_pos.append(h.text)
                self.pos_count += 1

        for head in headline_heading:
            actual_head = head.text
            self.headings.append(actual_head)

        for link in headline_url:
            actual_link = link.get('href')
            url = 'https://google.com' + actual_link
            self.urls.append(url)


