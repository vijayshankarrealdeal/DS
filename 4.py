import pandas as pd
import numpy as np
student = ["jack", 'opera', 'minni']

sd = pd.Series(student)

stu_score = {
    'Alice':'Physics',
    'jack':'maths',
    'ur':'chemistry'
}
st = pd.Series(stu_score)

x = np.random.randn(20)
y = x**2

import matplotlib.pyplot  as plt
plt.plot(x,y)