

import scipy
import numpy as np 
import pandas as pd
import matplotlib.pylab as plt

df = pd.read_excel("test0.xlsx",index_col=0,
                   header=None)

s=pd.to_numeric(df[1][2:])
p=pd.to_numeric(df[2][2:])
l=pd.to_numeric(df[3][2:])
r, p = scipy.stats.pearsonr(p, l)
print(r)
