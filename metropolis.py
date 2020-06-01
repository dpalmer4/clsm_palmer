# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:12:02 2020

@author: danpa
"""
import numpy as np
import matplotlib.pyplot as plt
import math
def linear_dist(x):
    if x<=1 and x>=0:
        return 2*x
    else:
        return 0

def gaussian(var,ave,y):
    """produces a gaussian curve over certain values of y, given variance, average"""
    gaussian=((1/(np.sqrt(var) * np.sqrt(2*math.pi))))*(np.exp(-((y - ave)**2)/(2*(var))))
    return gaussian 

def gaussian_dist(x):
    """two gaussian distrbution added together"""
    var1=1
    ave1=1
    var2=1.5
    ave2=5
    g1=gaussian(var1,ave1,x)
    g2=gaussian(var2,ave2,x)
    return g1+g2

def metropolis(steps,desired_dist,randoms):
    """metrolpolis algorithim in 1d given number of samples
    outputs markov chain, chain of average of x, chain of variance of x,acceptance fraction"""
    x=np.zeros(steps+1)
    x[0]=.5
    ave_x=np.zeros(steps)
    var_x=np.zeros(steps)
    accepted=0
    rands=np.random.rand(steps)
    for i in range(steps):
        x_next=x[i]+randoms[i]
        if (desired_dist(x_next)/desired_dist(x[i]))>=1:
            x[i+1]=x_next
            accepted+=1
        else:
            if rands[i]<=(desired_dist(x_next)/desired_dist(x[i])):
                x[i+1]=x_next
                accepted+=1
            else:
                x[i+1]=(x[i])
        ave_x[i]=np.mean(x[0:i]) 
        var_x[i]=np.var(x[0:i])
        acceptance_fraction=accepted/steps
    return [x,ave_x,var_x,acceptance_fraction]

#plotting histogram of metropolis output, average of x vs. step, variance of x vs. step, acceptance fraction
steps=20000 
####algorithim check
check_steps=100
xlowlim=0
xuplim=1
c=np.linspace(xlowlim,xuplim,check_steps)
cx=np.zeros(check_steps)
for i in range(check_steps): 
    cx[i]=linear_dist(c[i])
    
    
randoms=np.random.normal(size=steps)
[x,ave_x,var_x,acceptance_fraction]=metropolis(steps,linear_dist,randoms)
t=range(steps)
plt.hist(x,bins=100,density=1,label="metropolis distribution")
plt.plot(c,cx,label="predicted distribution")
plt.ylabel("probability")
plt.xlabel("x")
print("acceptance fraction= ",acceptance_fraction)
plt.legend()
plt.show()
plt.plot(t,ave_x)
plt.ylabel("average of x")
plt.xlabel("step")
plt.show()
plt.plot(t,var_x)
plt.ylabel("variance of x")
plt.xlabel("step")