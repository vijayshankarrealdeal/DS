import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

def process_text(file_name):    
    word = re.findall(r'\w+',open('shakespeare.txt').read().lower())
    return word,len(word)

word_list,len_words = process_text('shakespeare.txt')

unique_words = set(word_list)

def frequency_word_count(word_list):
    bags_of_word = {}
    for word in word_list:
        if word in bags_of_word:
            bags_of_word[word] += 1
        else:
            bags_of_word[word] = 1
    return bags_of_word

get_frequency_of_word = frequency_word_count(word_list)
#plt.scatter(get_frequency_of_word.values(),get_frequency_of_word.keys())

def get_prob(get_frequency_of_word):
    total = sum(get_frequency_of_word.values())
    probs = {}
    for key,value in get_frequency_of_word.items():
        probs[key] = value/total
    return probs
prob = get_prob(get_frequency_of_word)

#plt.scatter(prob.keys(),prob.values())

def delete_word(word):
    delete_l = []
    split_l = []
    split_l = [(word[i:],word[:i]) for i in range(len(word)+1)]
    delete_l = [word[:i]+word[i+1:] for i in range(len(word))]
    return split_l,delete_l

    
    
    
    
    
    
    
    
    
    
    

