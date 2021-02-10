from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

diabets = load_diabetes()

# print(diabets.data[:,2])
# print(diabets.data[:2])

# plt.scatter(diabets.data[:, 2], diabets.target)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

b = a[:2]


# print(b)
# print(a.shape) 

#print(diabets.data[:, 2])
# print(a)
print(a[0,:])
# b = a[:2]
# print(b)

# c = a[:,1]
# print(c)
