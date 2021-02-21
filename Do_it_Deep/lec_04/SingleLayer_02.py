from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# 1. x, y 데이터 셋팅
# 2. 클래스 생성
# 3. w, b 변수 선언
# 4. w, b를 조정하면서 y_hat 구하는 함수 생성
# 5. 오차를 확인 후 w,b 업데이트
# 6. activation() 메소드 생성
# 7. w,b 를 업데이트 하면서 학습
# 8. 예측하는 메소드 구현
# 9. 모델 훈련하기
# 10. 테스트 세트 사용해 모델의 정확도 평가 


# 1. x, y 데이터 셋팅
cancer = load_breast_cancer()

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)

# print(x_train.shape, x_test.shape) # (455, 30) (114, 30)
# print(y_train.shape, y_test.shape) # (455,) (114,)

# 2. 클래스 생성
class LogisticNeuron:
    
    # 3. w, b 변수 선언 + losses 변수 선언
    def __init__(self):
        self.w = None
        self.b = None
        self.losses = []

    # 4. w, b를 조정하면서 y_hat(z) 구하는 함수 생성
    def forpass(self, x):
        z = np.sum(x * self.w) + self.b # 시그마 w * x
        return z

    # 5. 오차를 확인 후 w,b 업데이트
    def backprop(self, x, err):
        w_grad = x * err
        b_grad = 1 * err
        return w_grad, b_grad

    # 6. activation() 메소드 생성
    def activation(self, z):
        np.warnings.filterwarnings('ignore', 'overflow') # overflow 무시
        a = 1 / (1 + np.exp(-z)) # 시그모이드 계산
        return a

    # 7. w,b 를 업데이트 하면서 학습
    # 가중치 초기화
    # 절편 초기화
    def fit(self, x, y, epochs=100):
        self.w = np.ones(x.shape[1])    # (445, 30) 1번째 인덱스 30 # 가중치 초기화
        self.b = 0                      # 절편 초기화
        for i in range(epochs):
            for x_i, y_i in zip(x, y):
                z = self.forpass(x_i)   # 정방향 계산
                a = self.activation(z)  # 활성화 함수
                err = -(y_i - a)        # 오차 계산
                w_grad, b_grad = self.backprop(x_i, err) # 역방향 계산
                self.w -= w_grad        # 가중치 업데이트
                self.b -= b_grad        # 절편 업데이트

    # 8. 예측하는 메소드 구현
    def predict(self, x):
        z = [self.forpass(x_i) for x_i in x]    # 선형 함수 적용
        a = self.activation(np.array(z))        # 활성화 함수 적용
        return a > 0.5                          # 계단 함수 적용 (부등호가 있으니 True or False 반환)

# 9. 모델 훈련하기
neuron = LogisticNeuron()
neuron.fit(x_train, y_train)

# 10. 테스트 세트 사용해 모델의 정확도 평가 
test = np.mean(neuron.predict(x_test) == y_test) # 정확도(accuracy)
print(test)

# -------------------------------------------------------------#
# test = np.mean(neuron.predict(x_test) == y_test) 코딩 이해

# a == b 같으면 1, 다르면 0  
# np.mean(a == b) 0,1,1,1,0 .... 의 모든 합의 평균
# neuron.predict(x_test) 는 Ture, False 나오는 배열
# y_test 는 0,1 로 이루어진 배열
# => x, y 같으면 1, 다르면 0 합쳐서 평균 => accuracy(정확도)


# print('x = ', x_test)

# a = [neuron.forpass(x_i) for x_i in x_test]
# print('a = ' , a)

# b = neuron.activation(np.array(a))
# print('b = ', b)

# result = neuron.predict(x_test)
# print('result = ', result)