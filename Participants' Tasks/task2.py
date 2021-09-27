import numpy as np

def scaler(features):
    # feature scaling to be applied
    return features

def J(theta, X, Y):
    # error function to be implemented
    return 0

def grad (theta, alpha, X, Y):
    # gradient descent to be implemented
    return theta


if __name__ == "__main__":
    
    file_name = input('Enter the filename : ') # getting filename
    kc = np.genfromtxt(file_name, delimiter = ',') # loading the file into a numpy 2D array
    kc = np.delete(kc, 0, axis = 0) # deleting the labels row
    
    features = kc[:,0:-1] # unscaled features
    values = kc[:,-1] # true output
    
    features = scaler(features) # scaling features

    features = np.insert(features, 0, 1, axis=1) # for xo

    theta = np.zeros(features[0].size) # array of thetas

    iterations = int(input("Number of iterations = "))
    alpha = float(input("Alpha = "))
    
    print('iteration #{}: J = {} , theta = {}'.format(0, J(theta, features, values), theta)) # error for intial theta
    
    for i in range(iterations):
        theta = grad(theta, alpha, features, values)
        print('iteration #{}: J = {} , theta = {}'.format(i+1, J(theta, features, values), theta)) # error after each update
        
# IT IS ALSO REQUIRED TO COMPLETE THE TASK WITH A MINIAML NUMBER OF LOOPS ,YOU CAN USE NUMPY'S FEATURES TO IMPLEMENT YOUR SOLUTION