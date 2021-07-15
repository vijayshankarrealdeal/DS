# backfunctions
import numpy as np
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


def process_tweets(s):
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
    s = re.sub(r'\$\w*', '', s)
    s = re.sub(r'^RT[\s]+', '', s)
    s = re.sub(r'https?:\/\/.*[\r\n]*', '', s)
    s = re.sub(r'#', '', s)
    token = TweetTokenizer(preserve_case=False,strip_handles=True,reduce_len=True)
    tokenize = token.tokenize(s)
    tweet_clean = []
    for word in tokenize:
        if word not in stopwords_english and word not in string.punctuation:
            stem = stemmer.stem(word)
            tweet_clean.append(stem)
    
    return tweet_clean

def build_freq(tweet,label):
    y_label = np.squeeze(tweet).tolist()
    freqs = {}
    for y,tweet in zip(y_label,tweet):
        for word in process_tweets(tweet):
            pair = (word,y)
            if pair not in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1
    return freqs

def lookup(freqs,word,label):
    n = 0
    pair = (word,label)
    if pair in freqs:
        n = freqs[pair]
    return n
    
def confidence_ellipse(x,y,ax,n_std = 3.0,facecolor='none',**kwargs):
    
    cov = np.cov(x,y)
    per = cov[0,1]/ np.sqrt(cov[0,0]*cov[1,1])
    ell_radius_x = np.sqrt(1 + per)
    ell_radius_y = np.sqrt(1 - per)
    ellipse = Ellipse((0, 0),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor=facecolor,
                      **kwargs)
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)
    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
