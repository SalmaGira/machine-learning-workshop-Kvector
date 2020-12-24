import numpy as np
import matplotlib.pyplot as plt


def h(theta, X):
    return np.sum(theta * X, axis=1)

def J(theta, X, Y):
    HX = h(theta, X)
    sigma = np.sum((HX - Y)**2)
    return sigma/(2*Y.size)

def grad (theta, alpha, X, Y):
    HX = h(theta, X)
    sigma = np.sum(X.transpose()*(HX - Y), axis=1)
    return theta - (alpha/Y.size) * sigma

if __name__ == "__main__":
    
    file_name = input('file_name = ')
    kc = np.genfromtxt('./data/'+file_name,delimiter = ',')
    kc = np.delete(kc, 0, axis = 0)
    
    features = kc[:,0:-1]
    values = kc[:,-1]
    
    features = (features-features.mean(axis=0))/(features.max(axis=0)-features.min(axis=0))
    
    #plot
    plt.scatter(features,values)
    plt.show()
    plt.scatter(features,values)
    #endplot

    features = np.insert(features, 0, 1, axis=1)
    theta = np.zeros(features[0].size)

    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))
    
    temp = plt.plot(features[:,1],features[:,1]*theta[1]+theta[0])
    print('iteration #{}: J = {} , theta = {}'.format(0, J(theta, features, values), theta)) # error for intial theta
    
    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta))
        #temp.pop(0).remove() # to remove the past line
        temp = plt.plot(features[:,1],features[:,1]*theta[1]+theta[0]) # fitting the line
        #plt.scatter(theta[0],J(theta, features, values)) # J versus theta0
        #plt.scatter(theta[1],J(theta, features, values)) # J versus theta1
        plt.pause(0.05)
        
    plt.show() # to keep the window open