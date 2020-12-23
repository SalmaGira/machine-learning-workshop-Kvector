import numpy as np

def h(theta, X):
    n = X.size + 1
    hy = 0
    for i in range(n):
        hy += theta[i]*X[i]
    return hy

def J(theta, X, Y):
    m = Y.size
    sigma = 0
    for i in range(m):
        sigma += (h(theta, X[i]) - Y[i])**2
    return sigma/(2*m)

def grad (theta, alpha, X, Y):
    m = Y.size # number of rows = number of data samples
    n = X[0].size + 1 # number of feautres + 1 // 1 => theta(zero)
    new_theta = np.empty(n)
    for j in range(n):
        sigma = 0
        for i in range(m):
            sigma += (h(theta, X[i]) - Y[i]) * X[i,j]
        new_theta[j] = theta[j] - (alpha/m) * sigma
    return new_theta

if __name__ == "__main__":
    
    file_name = input('file_name = ')
    kc = np.genfromtxt('./data/'+file_name+'.csv', delimiter = ',')
    kc = np.delete(kc, 0, axis = 0)
    
    features = kc[:,0:-1]  #unscaled features
    values = kc[:,-1]
    
    features = np.insert(features, 0, 1, axis=1)
    
    theta = np.ones(features[0].size + 1)

    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))

    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta))
    
    
    
    
    
    
    
    #features = (kc[:,0:-1]-kc[:,0:-1].mean(axis=0))/(kc[:,0:-1].max(axis=0)-kc[:,0:-1].min(axis=0))  #features scaled