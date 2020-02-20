# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:35:36 2020

@author: danpa
"""

import numpy as np
import matplotlib.pyplot as plt

x1=np.random.rand(1000000)
y1=np.random.rand(1000000)

x2=(x1)**(1/2)
y2=(5/3)*(2*(y1))**(1/3)-1

mx=np.mean(x2)
my=np.mean(y2)
print("mean",mx,my)
print("var",np.var(x2),np.var(y2))
print("std", np.std(x2),np.std(y2))

z=x2+2*y2
print("mean z",np.mean(z))
print("var z", np.var(z))
print("std z", np.std(z))

plt.hist(z,100,density=1)