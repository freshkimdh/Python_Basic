# 1. 리스트 삭제
# nums = [100, 200, 300, 400, 500] 에서 400, 500 삭제 코드


# 2. 리스트의 내장 함수
# a = [200, 100, 300] 를 a = [200, 100, 1000, 300] 변경


# 5. for 문
# 1부터 10까지 2의 배수만 더하는 함수


# 10. 트리 


# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

x = 6

for i in range(1, x+1):
    for j in range(x+1-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
    
