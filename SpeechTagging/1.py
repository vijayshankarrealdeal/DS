import string
from collections import defaultdict
import pandas as pd
file = "WSJ_02-21.pos"

def read_file(file_name):
   with open(file_name) as f:
       return f.readlines()

    
lines = read_file(file)
##build vocab

def build_vocab(line):
    words = [line.split('\t')[0] for line in lines]
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    vocab = [k for k, v in freq.items() if (v > 1 and k != '\n')]
    vocab.sort()
    return vocab       

vocab = build_vocab(lines)     

def unknown(word):
    
    punctuation = set(string.punctuation)
    noun_suffix = ["action", "age", "ance", "cy", "dom", "ee", "ence", "er", "hood", "ion", "ism", "ist", "ity", "ling", "ment", "ness", "or", "ry", "scape", "ship", "ty"]
    verb_suffix = ["ate", "ify", "ise", "ize"]
    adj_suffix = ["able", "ese", "ful", "i", "ian", "ible", "ic", "ish", "ive", "less", "ly", "ous"]
    adv_suffix = ["ward", "wards", "wise"]
    
    if any(char.isdigit() for char in word):
        return "--unk_digit--"
    elif any(char.isupper() for char in word):
        return "--unk_upper--"

    elif any(word.endswith(suffix) for suffix in noun_suffix):
        return "--unk_noun--"

    elif any(word.endswith(suffix) for suffix in verb_suffix):
        return "--unk_verb--"

    elif any(word.endswith(suffix) for suffix in adj_suffix):
        return "--unk_adj--"

    elif any(word.endswith(suffix) for suffix in adv_suffix):
        return "--unk_adv--"
    
    return "--unk--"
    
    
    
def get_tag(line,vocab):
    
    if not line.split():
        word = "--n--"
        tag = '--s--'
    else:
        word,tag = line.split()
        if word in vocab:
            word = unknown(word)
    return word,tag

get_word_tag('In\tIN\n', vocab)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        