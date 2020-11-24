
#사전 : 키와 값 한 쌍을 원소로 가지는 자료형
#사전은 중괄호를 이용
dict = {}
dict['안녕'] = 'hello'
dict['기적'] = 'miracle'
dict['노력'] = 'effort'

#print(dict)

#삭제
#del dict['안녕']

#i는 인덱스, k는 key 값
for i, k in enumerate(dict) :
    print(i, k, dict[k])





