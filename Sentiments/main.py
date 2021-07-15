import nltk
import numpy as np
import pandas as pd
from nltk.corpus import twitter_samples
from pre_process import process_tweet, build_freqs

#Logistic regression function--------------------------------------------------
def sigmoid(x):
    return 1 / (1+np.exp(-x))

def gradient_decent(x,y,theta,alpha,num_iters):
    m = x.shape[0]
    for i in range(0,num_iters):
        z = x.dot(theta)
        h = sigmoid(z)
        J = -1.0/m *(( np.dot(y.T,np.log(h)) + np.dot( (1-y.T),np.log(1-h)) ))
        theta = theta - alpha/float(m)*(np.dot(x.T,(h-y)))
        print(f'loss -> {J} weightupdate->{theta}')

    return J ,theta

def extract_features(tweet,freq):
    word_l = process_tweet(tweet)
    x = np.zeros((1,3))
    x[0,0] = 1
    for word in word_l:
        x[0,1] = freq.get((word,1.0)) if (word,1.0) in freq else 0
        x[0,2] = freq.get((word,0.0)) if (word,0.0) in freq else 0
    return x
        
def train(train_x,freq,train_y):
    X = np.zeros((len(train_x),3))
    for i in range(len(train_x)):
        X[i,:] = extract_features(train_x[i],freq)
    Y = train_y
    J,theta = gradient_decent(X,Y,np.zeros((3,1)),1e-9,1500)
    print(f'final--->cost ->{J}\t theta -> {theta}')
    return J,theta

def predict_output(tweet,freq,theta):
    x = extract_features(tweet,freq)
    y_pred = sigmoid(x.dot(theta))
    return  y_pred
#------------------------------------------------------------------------------

#data--------------------------------------------------------------------------
postive_tweet = twitter_samples.strings('positive_tweets.json')
negative_tweet = twitter_samples.strings('negative_tweets.json')

test_pos = postive_tweet[4000:]
train_pos = postive_tweet[:4000]
test_neg = negative_tweet[4000:]
train_neg = negative_tweet[:4000]

train_x = train_pos + train_neg
test_x = test_pos + test_neg

train_y = np.append(np.ones((len(train_pos), 1)),
                    np.zeros((len(train_neg), 1)), axis=0)
test_y = np.append(np.ones((len(test_pos), 1)),
                   np.zeros((len(test_neg), 1)), axis=0)


freq = build_freqs(train_x, train_y)
#------------------------------------------------------------------------------

J,theta = train(train_x,freq,train_y)


for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'you are a dumb']:
    print( '%s -> %f' % (tweet, predict_output(tweet, freq, theta)))


#Examples-----------------------
my_tweet = 'This is great.'
y_hat = predict_output(my_tweet, freq, theta)
print(y_hat)
if y_hat > 0.5:
    print('Positive sentiment')
else: 
    print('Negative sentiment')