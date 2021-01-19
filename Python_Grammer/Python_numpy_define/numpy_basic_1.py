import numpy as np
import cv2

image = cv2.imread("C://Users/AIMEDIA_01/Desktop/test/Python_openCV/cat.png")
image = image[0:100, 0:100]
print(image.shape)
cv2.imshow('image', image)
cv2.waitKey(0)
list_data = [1,2,3]
list_data = [[1,2,3],[4,5,6],[7,8,9]]

# 1. list를 넘파이 자료형으로 변경

array = np.array(list_data)
print(array[0][1:])
print(array[2][:])
# print(type(array))

# print(array.size)
# print(array.dtype)

# # 2. 0부터 3까지의 배열 만들기
# #   arange는 크기
# array1 = np.arange(4)
# print(array1)

# # 3. 행렬 형태로 만들기
# # 실수 타입
# array2 = np.zeros((4,4), dtype=float)
# print(array2)

# # 1의 값을 가지는 문자 타입
# array3 = np.ones((4,4), dtype=str)
# print(array3)