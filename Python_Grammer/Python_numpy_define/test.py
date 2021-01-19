import numpy as np

# 배열 나누기
# split(데이터, 인덱스, axis)
# axis = 0 는 x축
# axis = 1 은 y축
# axis = 2 는 z축??
array1 = np.arange(8).reshape(2,4)
left, right = np.split(array1, [1], axis=0)

#기본 인덱스는 '열' 을 기준으로 한다.
print(array1)
print(left)


# print(left.shape)
# print(right.shape)
# print(array1)
# print(left)




