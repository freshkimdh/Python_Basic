# nn.Module

import torch.nn as nn
import torch

W = torch.FloatTensor([[1,2],
                        [3,4],
                        [5,6]])

b = torch.FloatTensor([2,2])

# print(W.size())
# print(b.size())

# Linear 함수
def linear(x, W, b):
    y = torch.matmul(x, W) + b # matmul 행렬곱
    
    return y

x = torch.FloatTensor([[1,1,1],
                        [2,2,2],
                        [3,3,3],
                        [4,4,4]])

# print(x.size())

y = linear(x, W, b)          

print(y.size())
# print(torch.matmul(x, W))
# print(y)



# 딥러닝 뉴럴 네트워크를 상속 받아서, nn.Module 를 상속받아서 구현한다
# class 생성, nn.Module 상속
class MyLinear(nn.Module): 

    def __init__(self, input_dim=3, output_dim=2): # input = n, output = m 
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        super().__init__()
        
        self.W = torch.FloatTensor(input_dim, output_dim) # 3x2 
        self.b = torch.FloatTensor(output_dim) # 2차원의 벡터

    # You should override 'forward' method to implement detail.
    # The input arguments and outputs can be designed as you wish.
    def forward(self, x):
        # |x| = (batch_size, input_dim)
        y = torch.matmul(x, self.W) + self.b
        # |y| = (batch_size, input_dim) * (input_dim, output_dim)
        #     = (batch_size, output_dim)
        
        return y

linear = MyLinear(3, 2)

y = linear(x)

print(y.size())

# nn.Module 에 등록을 해줘야 한다.
# 아무것도 안나온다.
for p in linear.parameters():
    print(p)





