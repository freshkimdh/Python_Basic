
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오

A,B = map(int,input().split())

if A < B :
    print("<")
elif A > B :
    print(">")
elif A == B :
    print("==")

# 'cc'로 2개의 변수로 구분
# a, b = input("나이를 입력해주세요").split('cc')
# print(a, b)