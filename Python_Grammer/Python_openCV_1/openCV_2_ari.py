import cv2

image = cv2.imread('Python_openCV_1/cat.png')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 numpy 객체의 특정 픽셀을 가르킵니다.
px = image[100,100]

# B, G, R 순서로 출력 됩니다.
# (단, Gray Scale인 경우에는 B, G, R로 구분되지 않는다)
print(px)

# R 값만 출력하기
print(px[2])

