import numpy as np

x_i = [[1,2,3,4,5],[1,2,3]]
y_i = [[1,2,3,4,5],[1,2,4]]



# 4. w, b를 조정하면서 y_hat(z) 구하는 함수 생성
def forpass(self, x):
    z = np.sum(x * self.w) + self.b # 시그마 w * x
    return z


    # 6. activation() 메소드 생성
def activation(self, z):
    np.warnings.filterwarnings('ignore', 'overflow') # overflow 무시
    a = 1 / (1 + np.exp(-z)) # 시그모이드 계산
    return a

def predict(self, x):
    z = [self.forpass(x_i) for x_i in x]    # 선형 함수 적용
    a = self.activation(np.array(z))        # 활성화 함수 적용
    return a > 0.5  



test = np.mean(x_i == y_i)
# test = np.mean(neuron.predict(x_test) == y_test)

print(test)