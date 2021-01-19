import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Python_openCV_1/cat.png')

# Numpy Slicing: ROI 처리 가능
roi = image[200:350, 50:200] # 행(x,y) / 열(x,y)

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi # roi를 이미지 범위만큼 출력

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

