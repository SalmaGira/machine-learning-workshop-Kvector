import numpy as np
import matplotlib.pyplot as plt


def get_X(X, i, j):
    return 1 if j == 0 else X[i][j-1]

def h(theta, X_i):
    return np.sum(theta[0] + theta[1:X_i.size+1] * X_i)

def J(theta, X, Y):
    sigma = 0
    for i in range(Y.size):
        sigma += (h(theta, X[i]) - Y[i])**2
    return sigma/(2*Y.size)

def grad (theta, alpha, X, Y):
    new_theta = np.empty(X[0].size+1)
    for j in range(X[0].size+1):
        sigma = 0
        for i in range(Y.size):
            sigma += (h(theta, X[i]) - Y[i]) * get_X(X ,i, j)
        new_theta[j] = theta[j] - (alpha/Y.size) * sigma
    return new_theta

if __name__ == "__main__":
    
    file_name = input('file_name = ')
    kc = np.genfromtxt('./data/'+file_name+'.csv', delimiter = ',')
    kc = np.delete(kc, 0, axis = 0)
    
    #features = kc[:,0:-1]  #unscaled features
    features = (kc[:,0:-1]-kc[:,0:-1].mean(axis=0))/(kc[:,0:-1].max(axis=0)-kc[:,0:-1].min(axis=0))  #features scaled
    values = kc[:,-1]
    
    ##mods
    plt.scatter(features,values)
    ##end

    theta = np.zeros(features[0].size + 1)

    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))

    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta))
        ##mods
        plt.plot(features,features[:,0]*theta[1]+theta[0])
        plt.pause(0.1)
        ##end
    plt.show()