from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

diabets = load_diabetes()

x = diabets.data[:,2]
y = diabets.target


# 예측값 찾기
# y = ax + b 일차 방정식
# y_hat = wx + b 

# y_hat = 예측값
# w = 가중치
# b = 절편

# 우리가 알고 싶은 것은 예측값(y_hat) 이다

# 임의로 값을 설정
w = 1.0 
b = 1.0

# x[0] = 0.06
# y[0] = 151.0 우리가 알고 싶은 값
y_hat = x[0]*w + b

print('y_hat = ',y_hat) # 실제 예측값에서 너무 벗어남

#----------------------------------------------------#
# w 값 조절하여 예측값 바꾸기 

w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b

print('y_hat_inc = ',y_hat_inc)

#----------------------------------------------------#
# w 값 조정한 후 예측값 증가 확인
w_rate = (y_hat_inc-y_hat) / (w_inc - w)
print('w_rate = ',w_rate)

#----------------------------------------------------#
# 가중치 없데이트
w_new = w + w_rate
print('w_new = ',w_new)

#----------------------------------------------------#
# 절편 업데이트 하기

b_inc = b + 0.1
y_hat_inc = x[0] * w_inc + b_inc
print('y_hat_inc = ',y_hat_inc)

b_rate = (y_hat_inc-y_hat) / (b_inc - b)
print('b_rate = ', b_rate)

b_new = b + 1
print('b_new = ',b_new)



