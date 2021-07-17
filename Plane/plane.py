import numpy as np
from utils_nb import plot_vectors
#here we will 
#scale , Translate, Rotate

R = np.array([[2,0],
              [0,-2]])

x = np.array([[1,2]])

y = np.dot(x,R)
plot_vectors([x,y],axes = [10,10],fname ='transform_x.svg')
#scale
x = x*4
plot_vectors([x,y],axes = [10,10],fname ='transform_x.svg')

#translate
x = x + 2
plot_vectors([x,y],axes = [10,10],fname ='transform_x.svg')

#Rotate
angle = 100 * (np.pi / 180) 
Ro = np.array([[np.cos(angle), -np.sin(angle)],
              [np.sin(angle), np.cos(angle)]])

x2 = np.array([2,2]).reshape(1,-1)
y2 = np.dot(x2,Ro)
#change angle to rotate the blue vector
plot_vectors([x2,y2],axes =[10,10],fname= 'transform_x.svg')

#FNORM
A = np.array([[2,2],[2,2]])
sq = np.square(A)
F_norm = np.sqrt(np.sum(sq))
