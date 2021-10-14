import numpy as np

np.set_printoptions(precision=3, threshold = 2) 

iris = np.genfromtxt(r'C:\Users\ASUS\Downloads\iris.data', delimiter=',', dtype = 'object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

print(np.argwhere(iris[:, 3].astype('float')>1)[0])