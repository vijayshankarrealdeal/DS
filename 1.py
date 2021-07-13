from PIL import Image
import numpy as np
from IPython.display import  display
import math
import matplotlib.pyplot as plt

fer = np.array([0, -19, 10, 20])    
cel = (fer - 32)*5/9

A = np.array([[1, 2], [2, 3]])
B = np.array([[3.0, 4], [5, 8]])


C = A + B

q = np.array([i for i in range(1, 16)]).reshape(3, 5)


im = Image.open("1.jpg")

image_array = np.array(im)
plt.imshow(image_array)

mask = np.full(image_array.shape,255)
modified_array = image_array - mask
modified_array = modified_array*-1
modified_array = modified_array.astype(np.uint8)

plt.imshow(modified_array)


