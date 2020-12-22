import numpy as np
import matplotlib.pyplot as plt


def h(theta, X):
    return np.sum(theta * X, axis=1)

def J(theta, X, Y):
    sigma = np.sum((h(theta, X) - Y)**2)
    return sigma/(2*Y.size)

def grad (theta, alpha, X, Y):
    new_theta = np.empty(X[0].size)
    for j in range(X[0].size):
        sigma = np.sum((h(theta, X) - Y) * X[:,j], axis=0)
        new_theta[j] = theta[j] - (alpha/Y.size) * sigma
    return new_theta

if __name__ == "__main__":
    
    file_name = input('file_name = ')
    kc = np.genfromtxt('./data/'+file_name+'.csv', delimiter = ',')
    kc = np.delete(kc, 0, axis = 0)
    
    features = kc[:,0:-1]
    values = kc[:,-1]
    
    features = (features-features.mean())/(features.max()-features.min())
    
    ##mods
    plt.scatter(features,values)
    ##end
    features = np.insert(features, 0, 1, axis=1)
    theta = np.zeros(features[0].size)

    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))

    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta))
        ##mods
        plt.plot(features[:,1],features[:,1]*theta[1]+theta[0])
        plt.pause(0.05)
        ##end
    plt.show()