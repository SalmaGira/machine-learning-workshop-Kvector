import numpy as np

def h(theta, X):
    n = X.size
    hy = 0
    for j in range(n):
        hy += theta[j]*X[j]
    return hy

def J(theta, X, Y):
    m = Y.size
    sigma = 0
    for i in range(m):
        sigma += (h(theta, X[i]) - Y[i])**2
    return sigma/(2*m)

def grad (theta, alpha, X, Y):
    m = Y.size # number of rows = number of data samples
    n = X[0].size # number of feautres
    new_theta = np.empty(n)
    for j in range(n):
        sigma = 0
        for i in range(m):
            sigma += (h(theta, X[i]) - Y[i]) * X[i,j]
        new_theta[j] = theta[j] - (alpha/m) * sigma
    return new_theta

if __name__ == "__main__":
    
    file_name = input('file_name = ') # getting file name
    kc = np.genfromtxt('./data/'+file_name, delimiter = ',') # loading the file into a numpy 2D array
    kc = np.delete(kc, 0, axis = 0) # deleting the labels row
    
    features = kc[:,0:-1] # unscaled features
    values = kc[:,-1] # true output
    
    features = (features-features.mean(axis=0))/(features.max(axis=0)-features.min(axis=0))  #features scaled
    features = np.insert(features, 0, 1, axis=1) # for xo
    
    theta = np.zeros(features[0].size) # array of thetas

    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))

    print('iteration #{}: J = {} , theta = {}'.format(0, J(theta, features, values), theta)) # error of the intial theta

    # iterating over updates
    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta)) # error per every update