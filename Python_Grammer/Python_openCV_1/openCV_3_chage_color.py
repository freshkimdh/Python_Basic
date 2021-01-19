import cv2
import time
import matplotlib.pyplot as plt

image = cv2.imread('Python_openCV_1/cat.png')

start_time = time.time()

# 첫 번째 방법 - for 문으로 돌려서 변경
# start_time = time.time()
# for i in range(0, 100):
#     for j in range(0, 100):
#         image[i, j] = [255, 255, 255] # 모든 값들을 255로 변경 
# print("--- %s seconds ---" % (time.time() - start_time))

# 두 번째 방법 - 해당 픽셀 값을 설정 후 변경
start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

