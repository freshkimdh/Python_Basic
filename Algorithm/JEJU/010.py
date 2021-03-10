
# 10. 트리 만들기
# 입력 5 
# 1, 3, 5, 7, 9 트리 만들기
 
# for i in range(1,5): # 1 이상 5 미만 
#     for j in range(i):
#         print("*",end="") # "end=" 는 줄바꿈 방지
#     print() # 개행

# print("abc",end="")
# print("123")


x = int(input("줄 수를 입력하세요 "))


# for i in range(1, x+1):
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(1, x+1):
#     for j in range(x+1-i):
#         print("*", end="")
#     print()

# 트리 
for i in range(1, x+1):
    for j in range(x+1 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
