import numpy as np
import matplotlib.pyplot as plt

# 얕은 신경망을 이용한 다중 분류 문제

# 함수 구현

# sigmoid 함수
# 값이 작아질수록 0, 커질 수록 1dp tnfua
# sigmoid(x) = 1/(1+e^-x)
def sigmoid(x):
    return 1/(1+np.exp(-x))


# softmax 함수
# softmax(x) = e^x / sigma e^x
def softmax(x):
    e_x = np.exp(x)
    return e_x / np.sum(e_x)


# 네트워크 구조 정의
class ShallowNN:
    # num_input : input layer 뉴런 갯수
    # num_hidden : hidden layer 뉴런 갯수
    # num_output : output layer 뉴런 갯수

    # W_h 히든레이어 weigt 행렬 = (n x m)(m x 1) = n x 1 
    # b_h 히든레이어의 bias 행렬 = 출력에서 더하기 때문에 출력이랑 길이가 같은
    # W_o 아웃풋 weight 행렬
    # b_o 아웃풋 bias 행렬

    def __init__(self, num_input, num_hidden, num_output):
        self.W_h = np.zeros((num_hidden, num_input), dtype=np.float32)
        self.b_h = np.zeros((num_hidden,), dtype=np.float32)
        self.W_o = np.zeros((num_output, num_hidden), dtype=np.float32)
        self.b_o = np.zeros((num_output,), dtype=np.float32)


    # 뉴런 네트워크 계산
    # 1. hidden layer 계산
    # 2. matmul 행렬의 곱 (2x3)(3x4) = 2x4 
    # 3. y = wx + b 계산
    # 4. 다중 클래스 분류이므로, softmax 로 반환

    def __call__(self, x):
        h = sigmoid(np.matmul(self.W_h, x) + self.b_h) # y = wx + b
        return softmax(np.matmul(self.W_o, h) + self.b_o) # y = wx + b
 

# !!학습하는 방법을 배우지 않아서 사전에 만든것!!
# 데이터셋 가져오기, 정리하기
dataset = np.load('C:/Users/AIMEDIA_01/Desktop/DH/c_git/Python_Basic/dataset/ch2_dataset.npz')
inputs = dataset['inputs']
labels = dataset['labels'] # classfication 에서 정답이 되는것


# 모델 만들기
# 데이터셋에 들어가 있고 선생님이 알고 있는 데이터 넣는다
# (input, hidden, output)
model = ShallowNN(2, 128, 10)


# !!학습하는 방법을 배우지 않아서 사전에 만든것!!
# 사전에 학습된 파라미터 불러오기
weights = np.load('C:/Users/AIMEDIA_01/Desktop/DH/c_git/Python_Basic/dataset/ch2_parameters.npz')
model.W_h = weights['W_h']
model.b_h = weights['b_h']
model.W_o = weights['W_o']
model.b_o = weights['b_o']


# 모델 구동 및 결과 프린트
outputs = list()
for pt, label in zip(inputs, labels):
    output = model(pt) # 입력값으로 출력값을 얻는다.
    outputs.append(np.argmax(output)) # argmax 가장 높은 index 가 추가된다.
    print("실제 추정치", np.argmax(output), "정답", label) 

outputs = np.stack(outputs, axis=0) #outputs에 리스트 넣어준다


# 정답 클래스 스캐터 플랏
plt.figure()
for idx in range(10): # 10개의 class 
    mask = labels == idx
    plt.scatter(inputs[mask, 0], inputs[mask, 1])

plt.title('true_label')
plt.show()


# 모델 출력 클래스 스캐터 플랏
plt.figure()
for idx in range(10):
    mask = outputs == idx
    plt.scatter(inputs[mask, 0], inputs[mask, 1])

plt.title('model_output')
plt.show()