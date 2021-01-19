# 3. 텍스트 안에 단어에 id를 부여하고 각 단어의 빈도수를 세어
# 각각의 텍스트에 해당하는 id를 저장하는 딕셔너리와 (o)

# 각각의 단어 id에 해당하는 빈도수를 저장하는 딕셔너리 리턴

# 텍스트 안에 특수 기호는 제거해야한다 (o)
# 모든 단어는 소문자 형태로 관리한다 (o)

# id_dict  = { Apple : 0 , is : 1,} 
# count_dict = { 0 : 1 , 1 : 3 }

import re

def word_index_count(text):

    #소문자 변환
    lower_text = text.lower()

    #특수문자 제거
    re_lower_text = re.sub('[.?]', '',lower_text)

    #단어 split
    split_text = re_lower_text.split(' ')
    set_item = set(split_text)

    id_dict = {}
    count_dict = {}

    for index , item in enumerate(set_item):
        id_dict[item] = index
    
    print("my_dict :", id_dict)

    #id 부여
    word_id = {
    'apple' : 0, 'is' : 1, 'fruit' : 2, 
    'orage' : 3, 'alos' : 4, 'tomato' : 5
    }

    id_frequency = {}

    #단어 count
    for i in split_text :
        id_frequency[i] = id_frequency.get(i, 0) + 1

    return word_id, id_frequency

text = "Apple is fruit. Orange is also fruit. Tomato is fruit?"
a = "Apple" in text
print(a)
print(word_index_count(text))
