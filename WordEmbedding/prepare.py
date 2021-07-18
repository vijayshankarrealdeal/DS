import  re
import emoji
import numpy as np
import nltk
from utils import get_dict

def tokenize(corpus):
    s = re.sub(r'[,!?;-]+', '.', corpus)
    s = nltk.word_tokenize(s)
    s = [ch.lower() for ch in s
            if ch.isalpha()
            or ch == '.'
            or ch == emoji.get_emoji_regexp().search(ch)
        ]
    return s

corpus = "Now it's your turn: try with your own sentence!"
corpus = tokenize(corpus)

def slide_(corpus,C):
    i = C
    while i < len(corpus) -C:
        center = corpus[i]
        context = corpus[C-i:i] + corpus[i+1:C+1+i]
        yield context,center
        i += 1
      
def word_2_one_vec(word, word2Ind, V):
    one_hot_vector = np.zeros(V)
    one_hot_vector[word2Ind[word]] = 1
    return one_hot_vector

def context_words_to_vector(context_words, word2Ind, V):
    context_words_vectors = [word_2_one_vec(w, word2Ind, V) for w in context_words]
    context_words_vectors = np.mean(context_words_vectors, axis=0)
    return context_words_vectors



