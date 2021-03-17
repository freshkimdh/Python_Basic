import torch

x = torch.FloatTensor([[[1,2,],
                        [3,4]],
                        [[5,6],
                        [7,8]],
                        [[9,10],
                        [11,12]]])

# 12개의 벡터(1차원)을 만들고 싶다
print(x.reshape(12)) # 12 = 3 * 2 * 2 

# matrix(2차원)을 만들고 싶다.
print(x.reshape(3,4)) # 12개니깐 3*4=12 다른 숫자의 3*5 이런거는 안된다
print(x.reshape(3,-1)) # -1 은 컴터가 알아서 해줌 // 1개만 써야지 모호함이 없다

# tensor(3차원)을 만들고 싶다.
print(x.reshape(3,1,4)) # (k,n,m)
print(x.reshape(-1,1,4))

# 메모리를 다시 설정할때 필요하다?? 이런게 있다고 기억
# contiguous + view = reshape 



