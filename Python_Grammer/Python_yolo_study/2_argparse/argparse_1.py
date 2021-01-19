
from __future__ import print_function
import argparse

# def detect():
#     X,Y


def main():
    parser = argparse.ArgumentParser() # argparse.ArgumentParser() 함수를 통해 parser를 생성
    parser.add_argument('X', type=int, help="What is the first number?") # add_argument 이용하여 입력받고자 하는 인자의 조건을 설정한다.
    parser.add_argument('Y', type=int, help="What is the second number?")
    args = parser.parse_args() # parse_args 함수를 통해 인자들을 파싱하여 args에 저장한다.
    print("args = ", args) # args =  Namespace(X=1, Y=2) // 1,2 를 주었을 때

    X = args.X
    Y = args.Y
    print("%d + %d = %d" % (X, Y, X+Y))

if __name__=="__main__":
    main()
