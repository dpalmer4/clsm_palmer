# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt
"""if np.random.rand()<.5:
    print("heads")
else:
    print("tails")
    
r1=np.random.rand(1000000)
r2=r1**(1/2)
h1=plt.hist(r1,100,density=1)
plt.show()
h2=plt.hist(r2,100,density=1)
plt.show()"""

"""

#1
plothist=[[],[],[],[],[],[] ]
for j in range(100000):
    num=np.random.rand()
    for i in range(6):
        if num>=(1.0/6.0)*(i) and num<=(1.0/6.0)*(i+1):
            plothist[i].append(i+1)
plt.hist(plothist)"""


#2

n1=np.random.rand(1000000)
n2=5-n1**(1/2)
h=plt.hist(n2,100,density=1)


#3
"""
x=np.random.rand(100000)
y=np.random.rand(100000)
z=2*x
h=plt.hist(z,100,density=1)
plt.show()
z2=x+y
h2=plt.hist(z2,100,density=1)
plt.show()"""

