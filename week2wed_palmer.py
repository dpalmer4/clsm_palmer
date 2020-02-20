# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:20:48 2020

@author: danpa
"""

import numpy as np
import matplotlib.pyplot as plt
"""r1=np.random.rand(1000000)
r2=np.random.rand(1000000)
m1=np.mean(r1)
m2=np.mean(r2)
s1=r1+r2
print(np.mean(s1))
r1s=np.std(r1)
r2s=np.std(r2)
rss=np.std(s1)
print(r1s,r2s,rss)
print(r1s**(2)+r2s**(2))"""

N=20
rn=np.random.rand(1000000,N)
rn=rn**.5
sn=np.sum(rn,1)
plt.hist(sn,1000,density=1)
print(np.var(sn))