#Visualizing Naive Bayes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from back import confidence_ellipse

data = pd.read_csv('bayes_features.csv')

fig, ax = plt.subplots(figsize = (8, 8))
colors = ['red', 'green']
ax.scatter(data.positive, data.negative, 
    c=[colors[int(k)] for k in data.sentiment], s = 0.1, marker='*')

plt.xlim(-250,0)
plt.ylim(-250,0)

plt.xlabel("Positive") 
plt.ylabel("Negative")

fig, ax = plt.subplots(figsize = (8, 8))

colors = ['red', 'green'] 


ax.scatter(data.positive, data.negative, c=[colors[int(k)] for k in data.sentiment], s = 0.1, marker='*')  # Plot a dot for tweet

plt.xlim(-200,40)  
plt.ylim(-200,40)

plt.xlabel("Positive") 
plt.ylabel("Negative") 

data_pos = data[data.sentiment == 1] 
data_neg = data[data.sentiment == 0] 

confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=2, edgecolor='black', label=r'$2\sigma$' )
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=2, edgecolor='orange')

confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=3, edgecolor='black', linestyle=':', label=r'$3\sigma$')
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=3, edgecolor='orange', linestyle=':')
ax.legend()
plt.show()