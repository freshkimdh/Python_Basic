# Linear Layer

import torch

W = torch.FloatTensor([[1,2],
                        [3,4],
                        [5,6]])

b = torch.FloatTensor([2,2])

print(W.size())
print(b.size())

# Linear 함수
def linear(x, W, b):
    y = torch.matmul(x, W) + b # matmul 행렬곱
    
    return y

x = torch.FloatTensor([[1,1,1],
                        [2,2,2],
                        [3,3,3],
                        [4,4,4]])

print(x.size())

y = linear(x, W, b)          

print(y.size())
# print(torch.matmul(x, W))
# print(y)







