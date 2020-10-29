# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:23:52 2020

@author: Eslam
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path ='D:\\ex1data1.txt'
data = pd.read_csv(path, header=None, names=['X1', 'Y'])


data.insert(0, 'Xo', 1)
print('new data = \n' ,data.head(10) )
print('**************************************')


cols = data.shape[1]
X = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]

print('**************************************')
print('X data = \n' ,X.head(10) )
print('y data = \n' ,y.head(10) )
print('**************************************')



X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))

print('X \n',X)
print('X.shape = ' , X.shape)
print('theta \n',theta)
print('theta.shape = ' , theta.shape)
print('y \n',y)
print('y.shape = ' , y.shape)
print('**************************************')


def costfunction (X, y, theta):
    z = np.power(((X * theta.T) - y), 2)
#    print('z \n',z)
#    print('m ' ,len(X))
    return np.sum(z) / (2 * len(X))

print('the cost= ' , costfunction(X, y, theta))


def gradientDescent(X, y, theta, alpha, attempts):
    temp = np.matrix(np.zeros(theta.shape)) #[0,0]
    parameters = int(theta.ravel().shape[1]) #2
    cost = np.zeros(attempts)
    
    for i in range(attempts):
        error = (X * theta.T) - y
        
        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))
            
        attempts = temp
        cost[i] = costfunction(X, y, theta)
        
    return theta, cost



alpha = 0.01
attemps = 1000

g, cost = gradientDescent(X, y, theta, alpha, attemps)






# get best fit line

x = np.linspace(X.min(), X.max(), 100)

f = g[0, 0] + (g[0, 1] * x)





fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(X, y, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('input')
ax.set_ylabel('output')
ax.set_title('result')


