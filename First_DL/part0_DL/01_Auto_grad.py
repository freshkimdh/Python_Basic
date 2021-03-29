import torch

x = torch.FloatTensor([[1,2],
                        [3,4]]).requires_grad_(True)

x1 = x + 2
x2 = x - 2
x3 = x1 * x2
y = x3.sum()

print(x1)
print(x2)
print(x3) # x3 = x1 * x2 = (x+2)(x-2) = x^2 - 4
print(y)

y.backward() # 미분 진행


#  y를 x로 미분 진행 한것
# y = x^2 + 4
# y' = 2x
print(x.grad)