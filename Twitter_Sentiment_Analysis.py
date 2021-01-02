import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
plt.style.use('fivethirtyeight')

api_key = ""
api_secret_key = ""
access_token = ""
access_token_secret = ""

auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_secret_key)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = "Google"
tweet_amount = 100

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0

for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2]
    analysis = TextBlob(final_text)
    polarity += analysis.polarity

print(polarity)
