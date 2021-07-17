import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import  Counter
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
    return delete_l

def insert_word(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []
    split_l = [(word[i:],word[:i]) for i in range(len(word)+1)]
    insert_l = [L+c+R for L,R in split_l for c in letters]
    return insert_l
    
def switch_letters(word):
    switch_l = []
    split_l = []
    
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    switch_l = [L + R[1] + R[0] + R[2:] for L,R in split_l if len(R)>1]
    return switch_l

def replace_letters(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    split_l = []
    replace_l = []
    split_l = [(word[i:],word[:i]) for i in range(len(word)+1)][:-1]
    replace_l = [L + c + R[1:] for L,R in split_l for c in letters]
    replace_l[:] = [x for x in replace_l if x != word]
    replace_l.sort()
    return replace_l
        
def one_away(word,switch = True):
    one_edit = set()
    
    if switch:
        one_edit = set(insert_word(word) + replace_letters(word) + switch_letters(word)+delete_word(word))
    else:
        one_edit = set(insert_word(word)+ replace_letters(word)+delete_word(word))
    return one_edit

def two_away(word,switch = True):
    two_edit_away = set()
    one_away_edit = one_away(word,switch)
    for edit_one_word in one_away_edit:
        two_edit_away = two_edit_away.union(one_away_edit(edit_one_word))
    return two_edit_away


def corrections(word,probs,vocab,n = 2):
    suggestions = []
    n_best = []
    
    word_prob = {}
    
    if word in vocab:
        word_prob[word] = probs[word]
    
    if len(word_prob) == 0:
        word_one_edit = one_away(word)
        for temp_word in word_one_edit:
            if temp_word in vocab:
                word_prob[temp_word] = probs[temp_word]
    n_best = Counter(word_prob).most_common(n)
    for best_word,probablity in n_best:
        suggestions.append(best_word)
    
    print("entered word = ", word, "\nsuggestions = ", suggestions)   
    return n_best         
            
        
    
my_word = 'som' 
tmp_corrections = corrections(my_word, prob, unique_words, 2) 
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")

print(f"data type of corrections {type(tmp_corrections)}")
    
    
    
    
    

