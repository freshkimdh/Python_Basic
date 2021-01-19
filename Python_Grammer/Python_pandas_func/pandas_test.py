import pandas as pd

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
}

w = pd.Series(word_dict)
f = pd.Series(frequency_dict)
i = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word' : w,
    'frequency' : f,
    'impotance' : i
})

score = summary['frequency'] * summary['impotance']
summary['score'] = score


print(summary)
