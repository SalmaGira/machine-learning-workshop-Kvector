import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def h(theta, X):
    #return np.sum(theta * X, axis=1) # hypothesis function used for linear regression
    return 1 / ( 1 + np.e**(-1 * np.sum(theta * X,axis=1))) # hypothesis function used for logistic regression

def J(theta, X, Y):
    HX = h(theta, X)
    #sigma = np.sum((HX-Y)**2) # error for a linear regressor
    sigma = np.nansum(Y*np.log(HX)+(1-Y)*np.log(1-HX)) # error for the logistic regressor
    #if you encounter nan values; use np.nansum() (considers nan=zero) or add 1e-20 (small value) inside the log
    #nan + anynumber = nan
    return -sigma/(2*Y.size)

def grad (theta, alpha, X, Y, lam):
    HX = h(theta, X)
    sigma = np.sum(X.transpose()*(HX - Y), axis=1)
    return (alpha/Y.size)*(sigma + lam*theta)

def main():
    
    file_name = 'modified.csv'#input('file_name = ')
    
    # loading the csv into a dataframe
    df = pd.read_csv('./data/'+file_name)
    poss = df.loc[df['admission']==1]
    neg = df.loc[df['admission']==0]
    # converting to a numpy matrix
    kc = np.array(df)
    
    # features = X
    features = kc[:,0:-1]
    # values = Y
    values = kc[:,-1]
    
    plt.scatter(poss.iloc[:,0],poss.iloc[:,1],color='red')
    plt.scatter(neg.iloc[:,0],neg.iloc[:,1],color='blue')
    #plt.show()
    
    # applying feature scaling
    maxmin = features.max(axis=0)-features.min(axis=0)
    mean = features.mean(axis=0)
    features = (features-mean)/(maxmin)
    # inserting 1s for Xo
    features = np.insert(features, 0, 1, axis=1)

    # initialzing theta
    theta = np.ones(features[0].size)
    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))
    lam = float(input("lambda = "))
    
    # iterating to change theta
    for i in range(iterations):
        try:
            print('iteration #{}: J = {} , theta = {}'.format(i, J(theta, features, values), theta))
            theta -= grad(theta, alpha, features, values, lam)
        except:
            break
        

main()