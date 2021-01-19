from __future__ import print_function
import pickle
import os.path # 경로 설정
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import io
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000

import numpy as np
import time

import cv2 # openCV
import numpy as np
import datetime

from googleapiclient.http import MediaIoBaseDownload


# None 값이 들어있지 않는 변수
def imwrite(filename, img, params=None):
    try:
        # os.path.splitext(name)
        #  확장자만 따로 떨어뜨린다.
        # name = "c:\temp\test\python\hello.exe"
        # print(name) => .exe
        # os.path.splitext(filename)[0] # 인덱스 위치 0
        # os.path.splitext(filename)[1] # 인덱스 위치 1

        ext = os.path.splitext(filename)[1] # [1] 확장자만 가져옴 

        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else :
            return False
        
    except Exception as e:
        print(e)
        return False

SCOPES = ['https://www.googleapis.com/auth/drive']
creds = None

# imwrite("C:\\Users\\AIMEDIA_01\\Desktop\\test\\result1.png","result1.png")






# 1. with open(파일경로, 모드) as 파일 객체:
# with...as 파일을 열고 해당 구문이 끝나면 자동으로 닫히게 되는 문법
# with open("C:\\Users\\AIMEDIA_01\\Desktop\\test.txt", "w") as file:
#     file.write("test oh~~~")

# 2. readline() 함수 
# 파일 내용을 한줄씩 읽는 것
# r - 읽기모드, w - 쓰기모드, a - 추가모드
# f = open("C:\\Users\\AIMEDIA_01\\Desktop\\test.txt")
# line = f.readline()
# print(line)

# 3. for ... in enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때
t = ['aaa!aa','bbb!bb','ccc!cc','ddd!dd','eee!ee']
# for i,j in enumerate(t):
#   print(i,j)
# for i,j in enumerate(t):
#   print("i",i)
#   print("j",j)

for num,data in enumerate(t):
    data = data.strip() # 양끝 공백과 \n을 제거
    index = data.index("!") # "!" 몇번째 index 인지 위치 찾기

    # [0:4] 0 이상 4 미만
    # [:7] 리스트 처음부터 7 미만
    # [7:] 리스트 7이상 부터 끝까지
    file_name = data[:index] # 위치 찾은 인덱스까지 출력    
    file_id = data[index + 1 :] # index + 1 부터 끝까지 출력


# f ("김대환 {} 입니다.".format()) format을 줄인것이다.
with open(f'C:\\Users\\AIMEDIA_01\\Desktop\\test.txt', 'r' , encoding='utf-8') as flist:
    datas = flist.readlines()
    data_len = len(datas) 
    print('Download {} images'.format(data_len))


    for num ,data in enumerate(datas):
        data = data.strip() 
        index = data.index("!")
        file_name = data[:index]
        file_id = data[index + 1 :]

        date_index = file_name.index(".") # '.' 이 몇번째 index 인지 위치 찾기
        date = file_name[date_index - 15:date_index]
        # folder_name = "D://SR_Data_v1.0/"  + date[:8] + "/"
        folder_name = "C:\Users\AIMEDIA_01\Desktop"  + date[:8] + "/"
        file_name = folder_name + file_name



#         imwrite(file_name, image)