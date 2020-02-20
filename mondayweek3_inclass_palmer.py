# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:49:44 2020

@author: danpa
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(1000000)
K=1
T=1
A=1
m=1
z=1

#probability distribution of Energy
E=(-K*T*np.log(K*T*x/A))
plt.hist(E,100,density=1)
plt.xlabel("Energy")
plt.ylabel("probability")
plt.show()


#probability distribution of velocity
vp=np.sqrt(np.log(2/(E*z))*2*K*T/m)-1  #positive velocities
vn=-np.sqrt(np.log(2/(E*z))*2*K*T/m)+1 #negative velocities
v=np.concatenate((vp,vn))
plt.hist(v,100,density=1)
plt.show()