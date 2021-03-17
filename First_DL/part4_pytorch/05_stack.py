import torch

# stack
# 말 그대로 쌓는것

x = torch.FloatTensor([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

y = torch.FloatTensor([[10,11,12],
                        [13,14,15],
                        [16,17,18]])
print(x.size(), y.size())


# 두개를 쌓으니깐 차원이 더 생기는거
# 사격형 블록에 하나 더 얹혀서 
# (2,3,3)
z = torch.stack([x,y]) 
print(z)
print(z.size())

# cat - 실제 존재하는 dimation 에 붙힌다
# stack - 내가 원하는 dimation에 unsqueeze 해서 붙이는 것

# (3,3,2)
z = torch.stack([x,y], dim=-1) 
print(z)
print(z.size())








