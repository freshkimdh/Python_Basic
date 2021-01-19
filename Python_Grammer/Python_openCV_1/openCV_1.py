import cv2

# img_basic = cv2.imread('cat1.jpg', cv2.IMREAD_COLOR)
# img = 'Python_openCV/cat.png'
# img_basic = cv2.imread(img, imread_greyscale)

# # print('shape:',img_basic.shape)
# cv2.imshow('image Basic', img_basic)
# cv2.waitKey(0)
# cv2.release()
# cv2.destroyAllWindows()

img_basic = cv2.imread("Python_openCV_1/cat.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image Basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png',img_basic)
