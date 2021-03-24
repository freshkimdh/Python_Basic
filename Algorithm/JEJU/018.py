# 18. 국어, 수학, 영어 시험 보았습니다. 평균 점수를 구하시오
# 공백으로 구분하여 세 과목의 점수가 주어지면
# 전체 평균 점수를 구하는 프로그램을 작성하세요. 단, 소숫점 자리는 모두 버립니다.


# def avg_score(kor, math, eng):
#     avg = (kor + math + eng) / 3
#     return round(avg,3)

# a = avg_score(90,80,90)
# print(a)

# data = list(map(int, input().split()))

# print(int(sum(data)/3))

# ================================================= # 

# 참고사이트
# https://dojang.io/mod/page/view.php?id=2286

# 리스트, map
# 아래 리스트의 모든 요소를 정수로 변환

a = [1.2, 2.5, 3.7, 4.6]

for i in range(len(a)):
    a[i] = int(a[i])

print(a)

# 이때 map을 사용하면 편하다
# list(map(함수, 리스트))

a = list(map(int, a))
b = list(map(int, range(10)))

print(a)
print(b)

