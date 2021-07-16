import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import math
import random
import pandas as pd


n = 1
x = np.random.uniform(1,2,1000)
y = x.copy()

#mean
x = x - np.mean(x)
y = y - np.mean(y)

data = pd.DataFrame({'x':x,'y':y})

plt.scatter(data.x,data.y)

pca = PCA(n_components=2)

pcaTr = pca.fit(data)

rotatedData = pcaTr.transform(data)

dataPCA = pd.DataFrame(data = rotatedData, columns = ['PC1', 'PC2']) 
plt.scatter(dataPCA.PC1, dataPCA.PC2)
plt.show()

import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

random.seed(100)

std1 = 1    
std2 = 0.333 

x = np.random.normal(0, std1, 1000) 
y = np.random.normal(0, std2, 1000)  

x = x - np.mean(x) 
y = y - np.mean(y)

n = 1 
angle = np.arctan(1 / n) 
print('angle: ',  angle * 180 / math.pi)
rotationMatrix = np.array([[np.cos(angle), np.sin(angle)],
                 [-np.sin(angle), np.cos(angle)]])
print('rotationMatrix')
print(rotationMatrix)

xy = np.concatenate(([x] , [y]), axis=0).T 

data = np.dot(xy, rotationMatrix) 
plt.scatter(data[:,0], data[:,1])
plt.show()


plt.scatter(data[:,0], data[:,1]) 
pca = PCA(n_components=2)  

pcaTr = pca.fit(data)

dataPCA = pcaTr.transform(data)

print('Eigenvectors or principal component: First row must be in the direction of [1, n]')
print(pcaTr.components_)

print()
print('Eigenvalues or explained variance')
print(pcaTr.explained_variance_)

plt.scatter(dataPCA[:,0], dataPCA[:,1])
plt.plot([0, rotationMatrix[0][0] * std1 * 3], [0, rotationMatrix[0][1] * std1 * 3], 'k-', color='red')
plt.plot([0, rotationMatrix[1][0] * std2 * 3], [0, rotationMatrix[1][1] * std2 * 3], 'k-', color='green')

plt.show()


