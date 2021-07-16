import re
import string
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt

def process_tweets(s):
    stem = PorterStemmer()
    stopword = stopwords.words('english')
    s = re.sub(r'\$\w*', '', s)
    s = re.sub(r'^RT[\s]+', '', s)
    s = re.sub(r'https?:\/\/.*[\r\n]*', '', s)
    s = re.sub(r'#', '', s)
    token = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    token_word = token(s)
    clean =[]
    for word in token_word:
        if word not in stopword and word not in string.punctuation:
            s_ = stem.stem(word)
            clean.append(s_)
        
def cosine_similar(A,B):
    dot_product = np.dot(A,B)
    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)
    cos = dot_product/ (norm_a*norm_b)
    return cos

def plot_vectors(vectors, colors=['k', 'b', 'r', 'm', 'c'], axes=None, fname='image.svg', ax=None):
    scale = 1
    scale_units = 'x'
    x_dir = []
    y_dir = []
    
    for i, vec in enumerate(vectors):
        x_dir.append(vec[0][0])
        y_dir.append(vec[0][1])
    
    if ax == None:
        fig, ax2 = plt.subplots()
    else:
        ax2 = ax
      
    if axes == None:
        x_axis = 2 + np.max(np.abs(x_dir))
        y_axis = 2 + np.max(np.abs(y_dir))
    else:
        x_axis = axes[0]
        y_axis = axes[1]
        
    ax2.axis([-x_axis, x_axis, -y_axis, y_axis])
        
    for i, vec in enumerate(vectors):
        ax2.arrow(0, 0, vec[0][0], vec[0][1], head_width=0.05 * x_axis, head_length=0.05 * y_axis, fc=colors[i], ec=colors[i])
    
    if ax == None:
        plt.show()
        fig.savefig(fname)

    
            
            