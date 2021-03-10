
import numpy as np

# MSE
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t=[0,0,1,0,0,0,0,0,0,0]
#정답은 2
y=[0.1,0.05,0.6,0.05,0.1,0,0.1,0,0,0]
#예 1: 정답이 2일 확률이 0.6으로 최대 (60%)
print(mean_squared_error(np.array(y),np.array(t)))

y=[0.1,0.05,0,0.05,0.1,0,0.1,0,0,0.6]
#예 1: 정답이 9일 확률이 0.6으로 최대 (60%)
print(mean_squared_error(np.array(y),np.array(t)))


# # CEE
# def cross_entropy_error(y, t):
#     delta=1e-6
#     return -np.sum(t*np.log(y+delta))

# t=[0,0,1,0,0,0,0,0,0,0]
# #정답은 2
# y=[0.1,0.05,0.6,0.05,0.1,0,0.1,0,0,0]
# #예 1: 정답이 2일 확률이 0.6으로 최대 (60%)
# print(cross_entropy_error(np.array(y),np.array(t)))

# y=[0.1,0.05,0,0.05,0.1,0,0.1,0,0,0.6]
# #예 1: 정답이 9일 확률이 0.6으로 최대 (60%)
# print(cross_entropy_error(np.array(y),np.array(t)))