import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import warnings

#------------------------------------------------------------------------------------------#
# 문제1. mnist 데이터 살펴보기
mnist = keras.datasets.mnist

# x = mnist.load_data()
# print(x)

((train_images, train_labels), (test_images, test_labels)) = mnist.load_data()


#------------------------------------------------------------------------------------------#
# 문제2. 데이터의 shape을 출력해보세요.
print("train_images : ", train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)


#------------------------------------------------------------------------------------------#
# 문제3. (28,28) 형태의 이미지를 plt을 이용하여 출력해보세요.

# print(train_images[6000].shape)
plt.figure()
plt.imshow(train_images[0]) # 이미지 정답 = 5
plt.colorbar() # 칼라를 통해서 대략적인 값을 알 수 있다.
plt.grid(True)
plt.show()
print(train_labels[0]) # 레이블 정답 = 5


#------------------------------------------------------------------------------------------#
# 문제4. 하나의 이미지에 대한 모든 0이 아닌 값을 출력하는 코드를 작성하세요.

# print(train_images[0]) 2차원 
change = train_images[0].reshape(-1) # reshape(-1) 1차원으로 변경
f = filter(lambda x : x != 0, change) # 0이 아닌 값을 출력
list_f = list(f) # list 형태로 변경

# print(sorted(list_f)[:10]) # 정렬, [:10] 10개까지만 출력


#------------------------------------------------------------------------------------------#
# 문제5. train_images의 dtype을 출력해보세요.

# uint8 
# u = unsigned 음수가 없다 즉, 양수만 있다
# int 정수 데이터
# 8 은 데이터 크기

print(train_images.dtype)
print(train_labels.dtype)
print(test_images.dtype)
print(test_labels.dtype)
