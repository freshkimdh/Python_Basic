# nn.Module

import torch.nn as nn
import torch

W = torch.FloatTensor([[1,2],
                        [3,4],
                        [5,6]])

b = torch.FloatTensor([2,2])


# Linear 함수
def linear(x, W, b):
    y = torch.matmul(x, W) + b # matmul 행렬곱
    
    return y

x = torch.FloatTensor([[1,1,1],
                        [2,2,2],
                        [3,3,3],
                        [4,4,4]])

y = linear(x, W, b)          
print("수동 = ", y.size())


class MyLinear(nn.Module): 

    def __init__(self, input_dim=3, output_dim=2): # input = n, output = m 
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        super().__init__()

        # nn.Parameter 를 해줘야 등록(register)이 되는 것이다.
        self.W = nn.Parameter(torch.FloatTensor(input_dim, output_dim)) # 3x2 
        self.b = nn.Parameter(torch.FloatTensor(output_dim)) # 2차원의 벡터


    def forward(self, x):
        y = torch.matmul(x, self.W) + self.b
        
        return y

linear = MyLinear(3, 2)
 
# y = linear.forward(x) 동일한 표현이며, 나중에 더 심화과정에 배운다.
y = linear(x)

print("함수사용 = ", y.size())




# 위에 있는것이 정석이지만,
# 위에 있는것을 매번 하기에는 벅차고, 반복작업이기 때문에,
# nn.Linear 를 활용한다.

linear = nn.Linear(3,2)

y = linear(x)

print("한방짜리 = ", y.size())

for p in linear.parameters():
    print(p)
