import numpy as np

arr1 = np.arange(30,dtype=int)
arr2 = arr1*5 +7

np.savetxt('./data/test.csv',np.array([arr1,arr2]).transpose(),delimiter=',')
