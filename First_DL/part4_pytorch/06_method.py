import torch

# stack
# 말 그대로 쌓는것

x = torch.FloatTensor([[[1,2]],
                        [[3,4]]])
print(x.size())                

# expand
# 차원이 맞지 않지만 boardcast(퍼뜨리다) 해서 합쳐지도록 하는 것

y = x.expand(*[2,3,2])

print(y)
print(y.size())

# randperm : random permutation
# 안에 숫자들을 셔플링 막 섞어서 결고를 준다
x = torch.randperm(10)

print("randperm = ", x)
print(x.size())


# argmax
x = torch.randperm(3 ** 3).reshape(3,3,-1) # 랜덤

print(x)
print(x.size())

y = x.argmax(dim=-1)

# 결과값에 가장 큰 인덱스값을 구하는것 
# 각각의 3차원 그림에서 해당하는 큰값을 가져오는 것이다.
print(y)
print(y.size())

