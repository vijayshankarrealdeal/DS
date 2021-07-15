import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import numpy as np

all_postive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

def pre_process(s):
    stopwords_english = stopwords.words('english')
    stem = PorterStemmer()
    s  = s.lower()
    s = re.sub(r'^RT[\s]+', '', s)
    s = re.sub(r'https?:\/\/.*[\r\n]*', '', s)
    s = re.sub(r'#', '', s)
    token = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    s = token.tokenize(s)
    new_word = []
    for text_word in s:
        if text_word not in stopwords_english and text_word not in string.punctuation:
            k = stem.stem(text_word)
            new_word.append(k)
    return new_word
    
#Build Frequency Dict
label = np.append(np.ones(len(all_postive_tweets)),np.zeros(len(all_negative_tweets)))

def build_freq(tweets,ys):
    yslist = np.squeeze(ys).tolist()
    freqs = {}
    for y,tweet in zip(yslist,tweets):
        for word in pre_process(tweet):
            pair = (word,y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] += 1
    return freqs
build_freq(10000, label)