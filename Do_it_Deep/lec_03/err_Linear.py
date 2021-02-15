from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

diabets = load_diabetes()

x = diabets.data[:,2]
y = diabets.target


# 임의로 값을 설정
w = 1.0 
b = 1.0

# x[0] = 0.06
# y[0] = 151.0 우리가 알고 싶은 값
y_hat = x[0]*w + b

# print('y_hat = ',y_hat) # 실제 예측값에서 너무 벗어남

#----------------------------------------------------#
# w 값 조절하여 예측값 바꾸기 

w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b


#----------------------------------------------------#
# w 값 조정한 후 예측값 증가 확인 (증가값)
w_rate = (y_hat_inc-y_hat) / (w_inc - w) # x[0]과 동일


#----------------------------------------------------#
# 가중치 없데이트
# w_new = w + w_rate

#----------------------------------------------------#

# 첫번째
err = y[0] - y_hat # 오차값
w_new = w + w_rate * err # 새로운 가중치
b_new = b + 1 * err # 새로운 절편
print(w_new, b_new)

# 두번째
y_hat = x[1] * w_new + b_new
err = y[1] - y_hat
w_rate = x[1]
w_new = w_new + w_rate * err # 계산 후 다시 w_new 대입
b_new = b_new + 1 * err 
print(w_new, b_new)

# 세번째
y_hat = x[2] * w_new + b_new
err = y[2] - y_hat
w_rat = x[2]
w_new = w_new + w_rate * err
b_new = b_new + 1 * err
print(w_new, b_new)

# 세번째
y_hat = x[3] * w_new + b_new
err = y[3] - y_hat
w_rat = x[3]
w_new = w_new + w_rate * err
b_new = b_new + 1 * err
print(w_new, b_new)


# 반복문 사용
for x_i, y_i in zip(x,y):
    y_hat = x_i * w + b
    err = y_i - y_hat
    w_rate = x_i
    w = w + w_rate * err
    b = b + 1 * err

print(w, b)

# 반복문 epoch
# 원하는 모델를 만들기 위해 epoch 진행
for i in range(1,100):
    for x_i, y_i in zip(x,y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i
        w = w + w_rate * err
        b = b + 1 * err
print(w, b)

# 모델 완성
# y_hat = 913.6 * x + 123.4

# 완성된 모델로 y_hat(예측값) 구하기
x_new = 0.18
y_pred = x_new * w + b
print(y_pred)


#----------------------------------------------------#
# 구한 값 w, b 를 이용해서 직선 표현
# 산점도 그래프로 모델 확인

# x = diabets.data[:,2]
# y = diabets.target

plt.scatter(x,y) # 산점도 그래프
pt1 = (-0.1, -0.1 * w + b)
pt2 = (0.15, 0.15 * w + b)

# ex) x가 1 이면, y는 110 1차 방정식 그래프 
# plt.plot([1,2,3], [110,130,120]) 
plt.plot([pt1[0], pt2[0]], [pt1[1],pt2[1]])

plt.xlabel('x') # 그림에 표시
plt.ylabel('y') # 그림에 표시

plt.show()