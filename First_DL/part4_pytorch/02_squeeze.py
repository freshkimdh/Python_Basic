import torch

# x = torch.FloatTensor([[[1,2,],
#                         [3,4]]])


# squeeze 쥐어짜는거!!
# print(x.size()) # (1,2,2)
# print(x.squeeze()) # 쥐어짜서 (2,2)가 되는 것이다.

# unsqueeze
x = torch.FloatTensor([[1,2,],
                        [3,4]])

print(x.size())
# print(x.unsqueeze(2))
print(x.unsqueeze(2).size()) # 차원이 늘어남 (2,2,1)




