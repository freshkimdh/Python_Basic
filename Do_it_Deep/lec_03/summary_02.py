from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

# 1. x, y 데이터 셋팅
# 2. w, b 임의의 값 설정
# 3. w, b를 조정하면서 y_hat 구하기
# 4. 오차를 확인 후 w,b 업데이트
# 5. w,b 를 업데이트 하면서 학습
# 6. 그래프로 확인


# 1. x, y 데이터 셋팅
diabets = load_diabetes()

x = diabets.data[:,2]
y = diabets.target


class Neuron:

    # 2. w, b 임의의 값 설정
    def __init__(self):
        self.w = 1.0
        self.b = 1.0

    # 3. w, b를 조정하면서 y_hat 구하기
    def forpass(self, x):
        y_hat = x * self.w + self.b
        return y_hat

    # 4. 오차를 확인 후 w,b 업데이트
    # 역전파
    # w, b의 loss function을 최소화 하기 위해 미분 
    def backprop(self, x, err):
        w_grad = x * err # 가중치에 대한 미분 계산
        b_grad = 1 * err # 절편에 대한 미분 계산
        return w_grad, b_grad

    # 5. w,b 를 업데이트 하면서 학습
    # 학습 
    def fit(self, x, y, epochs=100):
        for i in range(epochs): # epochs 만큼 반복
            for x_i, y_i in zip(x, y): # 모든 샘플에 대해 반복
                y_hat = self.forpass(x_i) # 정방향 계산
                err = y_i - y_hat # 오차계산
                w_grad, b_grad = self.backprop(x_i, err) # 역방향 계산
                self.w = self.w + w_grad # 가중치 업데이트 (self.w += w_grad)
                self.b = self.b + b_grad # 절편 업데이트 (self.b += b_grad)


# 6. 그래프로 확인
# x : 입력 데이터
# y : 타깃 데이터
neuron = Neuron()
neuron.fit(x,y)

# 학습이 완료된 모델의 가중치와 절편 확인
plt.scatter(x,y)
pt1 = (-0.1, -0.1 * neuron.w + neuron.b)
pt2 = (0.15, 0.15 * neuron.w + neuron.b)
plt.plot([pt1[0], pt2[0]],[pt1[1], pt2[1]])
plt.xlabel('x')
plt.xlabel('y')
plt.show()








            