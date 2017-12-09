# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:01:30 2017

@author: SAMSUNG-pc
"""


import csv
import pandas as pd
csvFile = open("TRD_Week.csv", "r",encoding='UTF-8')
reader = csv.reader(csvFile)
#print(list(reader))
sss=list(reader)
#print(sss)
cols = ['股票代码', '股价']
df = pd.DataFrame(sss,columns=cols)

def combination(names):
    return ','.join(names)
    
abs=df.groupby('股票代码').aggregate(combination)
print(abs)
#abs.to_csv('wc.csv')