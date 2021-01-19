from PIL import Image
im = Image.open('result1.png')

res_im = im.transpose(Image.FLIP_LEFT_RIGHT) # 좌 우를 바꾼다. 
res_im.save('result1.png')#좌 우가 바뀐 Lenna 를 출력한다.

show.Image(im)