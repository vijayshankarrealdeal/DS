#DataFrames 

import pandas as pd

record1 = pd.Series({
    'name':'jack',
    'class':'Physics',
    'score':85,
    })

record2 = pd.Series({
    'name':'Kate',
    'class':'Chemistry',
    'score':15,
    })

record3 = pd.Series({
    'name':'martha',
    'class':'Math',
    'score':95,
    })

df = pd.DataFrame([record1,record2,record3],index = ['school1','school2','school3'])
#drop data

df.drop('name',inplace = True,axis = 1)

df1 = pd.read_csv()