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

#summing N boltzmann distributions
N=20 # number of distributions
r=1000000 # number of random numbers in distribution
n=np.random.rand(r,N)
En=(-K*T*np.log(K*T*n/A))
total_dist=[]
for i in range(r):
    total_dist.append(np.sum(En[i,:]))
plt.hist(np.array(total_dist),100,density=1)
plt.show()
    

#probability distribution of velocity
vp=np.sqrt(np.log(2/(E*z))*2*K*T/m)-1  #positive velocities
vn=-np.sqrt(np.log(2/(E*z))*2*K*T/m)+1 #negative velocities
v=np.concatenate((vp,vn))
plt.hist(v,100,density=1)
plt.show()