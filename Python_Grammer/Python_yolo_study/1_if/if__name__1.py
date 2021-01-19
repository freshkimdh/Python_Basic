# if __name__ == '__main__':
# 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라는 명령

def func():
    print("fuction working")


if __name__ == '__main__':
    print("직접실행")
    print(__name__)
else:
    print("임포트되어 사용됨")
    print(__name__)
