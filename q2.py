

import pandas as pd
import matplotlib.pylab as plt
df = pd.read_excel("test.xlsx",index_col=0,
                   header=None)
print(df[2])
s=pd.to_numeric(df[1][2:])
p=pd.to_numeric(df[2][2:])
l=pd.to_numeric(df[3][2:])

plt.scatter(p,l, color='coral')
plt.savefig("NCLOC_DCP.jpg")