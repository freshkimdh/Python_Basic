import numpy as np

#넘파이 배열 생성
print("넘파이 배열 생성")
x = np.array([1.0, 2.0, 3.0])
print(x)

#넘파이 산술 연산
print("넘파이 연산")
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x*y)

#넘파이 N차원 배열
print("넘파이 N차원 배열")
a = np.array([[1,2], [3,4]])
b = np.array([[2,2], [5,5]])

print(a)
print(a.shape)

print(a*b)

#브로드캐스트
print("브로드캐스트")
c = np.array([[1,2], [3,4]])
d = np.array([1,2])

print(c*d)