import numpy as np
import pandas as pd


def h(theta, X):
    #return np.sum(theta * X, axis=1) # hypothesis function used for linear regression
    return 1 / ( 1 + np.e**(-1 * np.sum(theta * features,axis=1))) # hypothesis function used for logistic regression

def J(theta, X, Y):
    HX = h(theta, X)
    #sigma = np.sum((HX-Y)**2) # error for a linear regressor
    sigma = np.sum(Y*np.log(HX)+(1-Y)*(np.log(1-HX))) # error for the logistic regressor
    return -sigma/(2*Y.size)

def grad (theta, alpha, X, Y):
    HX = h(theta, X)
    sigma = np.sum(X.transpose()*(HX - Y), axis=1)
    return (alpha/Y.size) * sigma

if __name__ == "__main__":
    
    file_name = input('file_name = ')
    
    #loading the csv into a dataframe
    df = pd.read_csv('./data/'+file_name)
    
    #converting to a numpy matrix
    kc = np.array(df)
    
    #features = X
    features = kc[:,0:-1]
    #values = Y
    values = kc[:,-1]
    
    #applying feature scaling
    features = (features-features.mean(axis=0))/(features.max(axis=0)-features.min(axis=0))
    
    #inserting 1s for Xo
    features = np.insert(features, 0, 1, axis=1)

    #initialzing theta
    theta = np.ones(features[0].size)
    
    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))
    
    print('iteration #{}: J = {} , theta = {}'.format(0, J(theta, features, values), theta))
    #iterating to change theta
    for i in range(iterations):
        theta -= grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta))