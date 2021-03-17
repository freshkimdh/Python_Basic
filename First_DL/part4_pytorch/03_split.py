import torch

# Pytorch의 sliceing 

x = torch.FloatTensor([[[1,2,],
                        [3,4]],
                        [[5,6],
                        [7,8]],
                        [[9,10],
                        [11,12]]])

print(x.size()) # (3,2,2)
 
print(x[0]) # 0 번의 인덱스
print(x[0, :]) # 0번 인덱스 가져오고 나머지 다 가져와

print(x[-1]) # 뒤에서 첫번째 인덱스
print(x[-1, :]) # 뒤에서 첫번째 인덱스 가져오고 나머지 다 가져와


y = torch.FloatTensor(10,4) # 2차원의 (10,4)

splits = y.split(4, dim=0) # dim 0 첫번째 // dim -1 마지막

# 10개를 4번 4번 나머지 출력
for s in splits:
    print(s.size())




