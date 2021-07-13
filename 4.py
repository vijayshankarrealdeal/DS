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

class_code = {
    99:'physics',
    100:'chemistry',
    101:'english',
    111:'history',
    }

se = pd.Series(class_code)

grades = pd.Series([99,90,2,12,54,73,7])

grades = grades+2