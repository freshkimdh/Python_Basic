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

# print('y_hat = ',y_hat) # 실제 예측값에서 너무 벗어남

#----------------------------------------------------#
# w 값 조절하여 예측값 바꾸기 

w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b


#----------------------------------------------------#
# w 값 조정한 후 예측값 증가 확인
w_rate = (y_hat_inc-y_hat) / (w_inc - w)


#----------------------------------------------------#
# 가중치 없데이트
w_new = w + w_rate


#----------------------------------------------------#
# 절편 업데이트 하기

b_inc = b + 0.1
y_hat_inc = x[0] * w_inc + b_inc

b_rate = (y_hat_inc-y_hat) / (b_inc - b)

b_new = b + 1


#----------------------------------------------------#
# epoch 진행
for i in range(1,100) :
    # 전체 샘플 반복하여, w, b 찾기
    for x_i, y_i in zip(x, y):

        # y = a*x + b
        y_hat = x_i * w + b

        err = y_i - y_hat # 오차

        w_rate = x_i # 

        w = w + w_rate * err # 임의로 정한 w에 값을 더해줌
        b = b + 1 * err  # 임의로 정한 b에 값을 더해줌

print(w,b) # 샘플로 오류를 줄여서 w, b 결과값을 찾음



#----------------------------------------------------#
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



#----------------------------------------------------#
# 내가 만든 모델로 예측값 구하기
x_new = 0.18
y_pred = x_new * w + b
print(y_pred)
