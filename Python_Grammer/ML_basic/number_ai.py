from PIL import Image
import matplotlib.pyplot as plt

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

import tensorflow as tf
import keras

print(train_images.shape) # 60000, 28, 28 => (갯수, 가로, 세로)
print(train_labels)

# print(train_images[0]) # 이미지 구성

# 학습 시킬 데이터 확인
digit = train_images[0]
plt.imshow(digit, cmap = plt.cm.binary)
plt.show()

# test 진행
origin_my_image = test_images[0]

# keras 딥러닝 기술 활용
from keras import models
from keras import layers

model = models.Sequential()

# 머신러닝 모델에 784개를 넣었고, 512개의 신호로 내보내겠다
# activation // 의미없는 데이터는 제거하고 0보다 큰것만 넘기겠다.
# 바로 다음 층으로 가서 256개로 출력
model.add(layers.Dense(512, activation='relu', input_shape=(28*28, ))) # 28*28=784 
model.add(layers.Dense(256, activatin='relu', ))
model.add(layers.Dense(128, activatin='relu', ))
model.add(layers.Dense(64, activatin='relu', ))

# 마지막에서 10개까지 줄인 이유는 숫자는 0~10 까지 있다.
# 그래서 0부터 9까지 줄여버린것이다.
model.add(layers.Dense(10, activation='softmax'))

# optimizer는 학습방법이며, 보통 adam 을 많이 쓴다
# lose 선생님이 채점해주는 것 ex) 선생님 이거 5에요 땡 4 에요 
# accuracy(정확도)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# (60000, 28, 28) 3차원 => 정육면체 60000, 28, 28
# (60000, 28*28) 2차원 => 사각형 784, 60000
train_images = train_images.reshape((60000, 28*28))


# 데이터 형태를 int로 되어 있었는데, float 형태로 바꿔준다.
# RGB 값(0~255) 되어있고, 255로 나누면 0,1 형태로 된다
train_images = train_images.astype('float32')/255
train_images.shape

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255

# 행렬의 연산을 위해 바꿔주는 것
from keras.utils import to_categorical
print(train_labels)

train_labels = to_categorical(train_labels)
print(train_labels)

test_labels = to_categorical(test_labels)
