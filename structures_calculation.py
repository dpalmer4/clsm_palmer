# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:36:00 2020

@author: danpa
"""

import numpy as np
import math

hkl=np.array([[1,1,1],[2,0,0],[2,2,0],[3,1,1],[2,2,2],[4,0,0],[3,3,1],[4,2,0],[4,2,2],[3,3,3]])

theta=np.array([36.93, 42.91, 62.30, 74.64, 78.64, 94.06, 105.75, 109.78, 127.29, 143.77])/2
a=0
lambdaa=.1542*10**(-9)
i=0
for t in theta:
    alpha=((hkl[i,0]**2+hkl[i,1]**2+hkl[i,2]**2)/4/(math.sin(t))**2)*lambdaa**2
    a+=np.sqrt(alpha)/len(theta)
    i+=1
print((a))