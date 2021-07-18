import numpy as np
import pandas as pd
from collections import defaultdict

def sigmoid(z):
    return 1 / (np.exp(-z)+1)

def get_idx(words,word2Ind):
    idx = []
    for word in words:
        idx = idx + [word2Ind[word]]
    return idx

def pack_idx_with_frequency(context_word,word2Ind):
    freq_dict = defaultdict(int)
    for word in context_word:
        freq_dict[word] += 1
    idxs = get_idx(context_word,word2Ind)
    packed = []
    for i in range(len(idxs)):
        idx = idxs[i]
        freq = freq_dict[context_word[i]]
        packed.append((idx,freq))
    
    return packed

def get_vectors(data,word2Ind,V,C):
    i = C
    while i < len(data) -C:
        x = np.zeros(V)
        y = np.zeros(V)
        center_word = data[i]
        y[word2Ind[center_word]] = 1
        context_word = data[C-i:i] + data[i+1:C+i+1]
        num_ctx_words = len(context_word)
        for idx,freq in pack_idx_with_frequency(context_word,word2Ind):
            x[idx] = freq/num_ctx_words
        yield x,y
        i += 1
        if i >= len(data):
            i = 0
            
    
def get_batches(data,word2Ind,V,C,batch_size):
    batch_x = []
    batch_y = []
    for x,y in get_vectors(data,word2Ind,V,C):
        while len(batch_x) < batch_size:
            batch_x.append(x)
            batch_y.append(y)
        else:
            yield np.array(batch_x).T ,np.array(batch_y).T
            batch = []

def PCA(data,n_components = 2):
    m,n = data.shape
    
    data -= data.mean(axis = 0)
    R = np.cov(data,rowvar=False)
    
    evals,evecs = np.linalg.eigh(R)
    idx = np.argsort(evals)[::-1]
    evecs = evecs[:,idx]
    evals = evals[idx]
    evecs = evecs[:,:n_components]
    return np.dot(evecs.T,data.T).T
    
def get_dict(data): 
    words = sorted(list(set(data)))
    idx = 0
    word2Ind = {}
    Ind2word = {}
    for k in words:
        word2Ind[k] = idx
        Ind2word[idx] = k
        idx += 1
    return word2Ind,Ind2word
    
    
    
    
    
        
        