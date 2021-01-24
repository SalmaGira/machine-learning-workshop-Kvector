import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def h(theta, X):
    #return np.sum(theta * X, axis=1) # hypothesis function used for linear regression
    return 1 / ( 1 + np.e**(-1 * np.sum(theta * X,axis=1))) # hypothesis function used for logistic regression

def J(theta, X, Y):
    HX = h(theta, X)
    #sigma = np.sum((HX-Y)**2) # error for a linear regressor
    sigma = np.sum(Y*np.log(HX)+(1-Y)*np.log(1-HX)) # error for the logistic regressor
    return -sigma/(2*Y.size)

def grad (theta, alpha, X, Y):
    HX = h(theta, X)
    sigma = np.sum(X.transpose()*(HX - Y), axis=1)
    return (alpha/Y.size)*sigma

def main():
    
    file_name = 'class.csv'#input('file_name = ')
    
    # loading the csv into a dataframe
    df = pd.read_csv('./data/'+file_name)
    pos = df.loc[df['admission']==1]
    neg = df.loc[df['admission']==0]
    # converting to a numpy matrix
    kc = np.array(df)
    
    # features = X
    features = kc[:,0:-1]
    # values = Y
    values = kc[:,-1]
    
    plt.scatter(pos.iloc[:,0],pos.iloc[:,1],color='red',label='positive')
    plt.scatter(neg.iloc[:,0],neg.iloc[:,1],color='blue',label='negative')
    plt.legend()
    plt.show()
    
    # applying feature scaling
    maxmin = features.max(axis=0)-features.min(axis=0)
    mean = features.mean(axis=0)
    features = (features-mean)/(maxmin)
    # inserting 1s for Xo
    features = np.insert(features, 0, 1, axis=1)
    
    trainingF = features[:80]
    trainingV = values[:80]
    testingF = features[80:]
    testingV = values[80:]
    
    # initialzing theta
    theta = np.ones(features[0].size)
    
    iterations = int(input("num_of_iterations = "))
    alpha = float(input("alpha = "))
    
    # iterating to change theta
    for i in range(iterations):
        try:
            print('iteration #{}: J = {} , theta = {}'.format(i, J(theta, trainingF, trainingV), theta))
            theta -= grad(theta, alpha, trainingF, trainingV)
        except:
            break
        
    original = [
                theta[0]-theta[1]*mean[0]/maxmin[0]-theta[2]*mean[1]/maxmin[1]
                 ,theta[1]/maxmin[0]
                 ,theta[2]/maxmin[1]
                 ]
    
    print(original)
    Xintercept = [0,-original[0]/original[1]]
    Yintercept = [-original[0]/original[2],0]
    
    plt.scatter(pos.iloc[:,0],pos.iloc[:,1],color='red',label='positive')
    plt.scatter(neg.iloc[:,0],neg.iloc[:,1],color='blue',label='negative')
    plt.plot(Xintercept,Yintercept,color='black',label='h(x)=0')
    
    #plt.legend(['h(x)=0','positive','negative'])
    plt.legend()
    
    plt.show()
    
    print('Tesing Error : ',J(theta,testingF,testingV))

main()