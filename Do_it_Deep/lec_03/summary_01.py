from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

# 1. x, y 데이터 셋팅
# 2. w, b 임의의 값 설정
# 3. w, b를 조정하면서 y_hat 구하기
# 4. 완성된 모델로 예측값 구하기
# 5. 그래프로 확인


# 1. x, y 데이터 셋팅
diabets = load_diabetes()

x = diabets.data[:,2]
y = diabets.target


# 2. w, b 임의의 값 설정
w = 1.0
b = 1.0


# 3. w, b를 조정하면서 y_hat 구하기 (epoch)
for i in range(1, 100):
    for x_i, y_i in zip(x,y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i 
        w = w + w_rate * err
        b = b + 1 * err

print(w,b)

# 4. 완성된 모델로 예측값 구하기
x_new = 0.18
y_perd = x_new * w + b
print(y_perd)


# 5. 그래프로 확인
plt.scatter(x,y) # 산점도 그래프
pt1 = (-0.1, -0.1 * w + b)
pt2 = (0.15, 0.15 * w + b)

plt.plot([pt1[0], pt2[0]], [pt1[1],pt2[1]])

plt.xlabel('x')
plt.ylabel('y')

plt.show()