import numpy as np
from utils import get_dict
from prepare import word_2_one_vec,tokenize,slide_,context_words_to_vector
import matplotlib.pyplot as plt


def relu(z):
    res = z.copy()
    res[res<= 0] = 0
    return res

def softmax(z):
    return np.exp(z)/np.sum(np.exp(z))

W1 = np.array([[ 0.41687358,  0.08854191, -0.23495225,  0.28320538,  0.41800106],
               [ 0.32735501,  0.22795148, -0.23951958,  0.4117634 , -0.23924344],
               [ 0.26637602, -0.23846886, -0.37770863, -0.11399446,  0.34008124]])

# Define second matrix of weights
W2 = np.array([[-0.22182064, -0.43008631,  0.13310965],
               [ 0.08476603,  0.08123194,  0.1772054 ],
               [ 0.1871551 , -0.06107263, -0.1790735 ],
               [ 0.07055222, -0.02015138,  0.36107434],
               [ 0.33480474, -0.39423389, -0.43959196]])

# Define first vector of biases
b1 = np.array([[ 0.09688219],
               [ 0.29239497],
               [-0.27364426]])

# Define second vector of biases
b2 = np.array([[ 0.0352008 ],
               [-0.36393384],
               [-0.12775555],
               [-0.34802326],
               [-0.07017815]])

words = ['i', 'am', 'happy', 'because', 'i', 'am', 'learning']

word2Ind,Ind2word = get_dict(words)
V = 5
def make_training_data_for_network(words,C,word2Ind,V):
    for context_word,center_word in slide_(words,C):
        yield context_words_to_vector(context_word,word2Ind,V),word_2_one_vec(center_word, word2Ind, V)
    
    
training_examples = make_training_data_for_network(words,2,word2Ind,V)    
x_array,y_array = next(training_examples)

x = x_array.copy()
x.shape = (V,1)
y = y_array.copy()
y.shape = (V,1)

def cross_entropy(y,y_hat):
    loss = -sum(y*np.log(y_hat)).squeeze()
    return loss

W1_old = W1.copy()
W2_old = W2.copy()
b1_old = b1.copy()
b2_old = b2.copy()
learning_rate = 0.001

loss_metric = []
for i in range(5000):
    first_layer = np.dot(W1,x) + b1
    h = relu(first_layer)
    second_layer = np.dot(W2,h) + b2
    y_hat = softmax(second_layer)
    loss = cross_entropy(y,y_hat)
    print(f'Loss ->\t{loss}')
    loss_metric.append(loss)
#Backprop
    grad_b2 = y_hat - y
    grad_w2 = np.dot((y_hat - y),h.T)
    grad_b1 = relu(np.dot(W2.T,y_hat-y))
    grad_w1 = np.dot(relu(np.dot(W2.T,y_hat-y)),x.T)
    W1 = W1 - grad_w1*learning_rate
    W2 = W2 - grad_w2*learning_rate
    b2 = b2 - grad_b2*learning_rate
    b1 = b1 - grad_b1*learning_rate


x = [i for i in range(len(loss_metric))]
plt.plot(x,loss_metric,color='g')




    