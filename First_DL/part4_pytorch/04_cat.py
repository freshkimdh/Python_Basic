import torch

# cat: Concatenation

x = torch.FloatTensor([[1,2,3],
                        [4,5,6],
                        [7,8,9]])

y = torch.FloatTensor([[10,11,12],
                        [13,14,15],
                        [16,17,18]])
print(x.size(), y.size())


# 붙이고 싶은것들끼리 합쳐주는 거 [x,3] [y,3] x,y 합쳐주는 것
# (6,3)
z = torch.cat([x,y], dim=0) # dim 0 첫번째 // dim -1 마지막
print(z)
print(z.size())

# (3,6)
z = torch.cat([x,y], dim=-1)
print(z)
print(z.size())







