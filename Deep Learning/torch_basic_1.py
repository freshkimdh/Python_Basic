import numpy as np
import torch

# gradient 기울기 (grad)
# requires_grad=False by default

x = torch.ones(2,2, requires_grad=True) # torch 연산에 기록하겠다
#print(x)

y = x + 2 # x가 grad=True 이기 때문에 같이 기록
print("y.grad_fn = ",y.grad_fn) # 연산의 결과로 생선된 y 이므로, grad_function 을 갖는다

# y에 다른 연산을 수행
z = y * y * 3 
out = z.mean() # z의 평균값

print('out = ', out)


#  벡터-야코비안 곱 후...
# out.backward()
# print(x.grad)

# print(x.requires_grad) # 기울기?
# print((x ** 2).requires_grad)

# with torch.no_grad():
#     print((x ** 2).requires_grad)