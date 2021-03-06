import numpy as np
import matplotlib.pyplot as plt

#Reading data
datafile = 'data/ex1data1.txt'
cols = np.loadtxt(datafile,delimiter=',',usecols=(0,1),unpack=True)
# X-->inputs Y-->outputs
X = np.transpose(np.array(cols[:-1]))
y = np.transpose(np.array(cols[-1:]))
#Insert the usual column of 1's into the "X" matrix
X = np.insert(X,0,1,axis=1)

#plot data
plt.figure(figsize=(10,6))
plt.plot(X[:,1],y[:,0],'rx',markersize=10)
plt.grid(True) #Always plot.grid true!
plt.ylabel('Profit in $10,000s')
plt.xlabel('Population of City in 10,000s')
plt.show()

#hypothesis function without victorization
def h2(theta,X):
    arr = np.zeros((X.shape[0],1))
    for i in range (X.shape[0]):
        arr[i][0] = theta[0][0]*X[i][0] + theta[1][0]*X[i][1]
    print(arr)

#hypothesis function victorized
def h(theta,X):
    return np.dot(X,theta)

#Cost function
def computeCost(theta, X, y):
    m = y.size # number of training examples
    squareSum = np.dot ((h(theta,X)-y).T , (h(theta,X)-y) )
    J = float( (1/(2*m)) * squareSum ) 
    return J

#testing
initial_theta = np.zeros((X.shape[1],1))
print( computeCost(initial_theta,X,y) )

#Gradiant Descent
iterations = 1500   #number of iterations
alpha = 0.01
def Gradiantdescent(X, initial_theta):
    m = y.size
    theta = initial_theta
    jvec = []               #all cost functions
    thetahistory = []       #theta history
    for _ in range(iterations):
        tmptheta = theta
        jvec.append(computeCost(theta,X,y))

        thetahistory.append(list(theta[:,0]))
        #Simultaneously updating theta values
        for j in range(len(tmptheta)):
            tmptheta[j] = theta[j] - (alpha/m) * np.sum( (h(theta,X) - y)*np.array(X[:,j]).reshape(m,1) )
        theta = tmptheta
    return theta, thetahistory, jvec

#testing
initial_theta = np.zeros((X.shape[1],1))
theta, thetahistory, jvec = Gradiantdescent(X,initial_theta)

#plot convergence of cost function
def plotConvergence(jvec):
    plt.figure(figsize=(10,6))
    plt.plot( range(len(jvec)) ,jvec,'bo')
    plt.grid(True)
    plt.title("Convergence of Cost Function")
    plt.xlabel("Iteration number")
    plt.ylabel("Cost function")
    dummy = plt.xlim([-0.05*iterations,1.05*iterations])
    #dummy = plt.ylim([4,8])


plotConvergence(jvec)
dummy = plt.ylim([4,7])
plt.show()

#Plot the line on top of the data to ensure it looks correct
def myfit(xval):
    return theta[0] + theta[1]*xval
plt.figure(figsize=(10,6))
plt.plot(X[:,1],y[:,0],'rx',markersize=10,label='Training Data')
plt.plot(X[:,1],myfit(X[:,1]),'b-',label = 'Hypothesis: h(x) = %0.2f + %0.2fx'%(theta[0],theta[1]))
plt.grid(True) #Always plot.grid true!
plt.ylabel('Profit in $10,000s')
plt.xlabel('Population of City in 10,000s')
plt.legend()
plt.show()

#--------------------------------------------------------
#plotting 3D
#Import necessary matplotlib tools for 3d plots
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
import itertools

fig = plt.figure(figsize=(12,12))
ax = fig.gca(projection='3d')

xvals = np.arange(-10,10,.5)
yvals = np.arange(-1,4,.1)
myxs, myys, myzs = [], [], []
for a in xvals:
    for b in yvals:
        myxs.append(a)
        myys.append(b)
        myzs.append( computeCost(np.array([[a], [b]]),X,y) )

scat = ax.scatter(myxs,myys,myzs,c=np.abs(myzs),cmap=plt.get_cmap('YlOrRd'))

plt.xlabel(r'$\theta_0$',fontsize=30)
plt.ylabel(r'$\theta_1$',fontsize=30)
plt.title('Cost (Minimization Path Shown in Blue)',fontsize=30)
plt.plot( [x[0] for x in thetahistory] , [x[1] for x in thetahistory] , jvec , 'bo-' )
plt.show()
#--------------------------------------------------------