### 함수 적용

import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')

df['학교']+='등학교'
print(df)


#df['키']+='cm' # 키=int 'cm'=str 그래서 안됨
## 데이터에 함수 적용(apply)
def add_cm(height):
    return str(height)+'cm'

df['키']=df['키'].apply(add_cm) # add_cm 함수 사용
print(df)


def def_capitalize(lang):
    if pd.notnull(lang): # NaN이 아닌지 확인
        return lang.capitalize() # 첫글자는 대문자로, 나머지는 소문자로
    return lang

df['SW특기']=df['SW특기'].apply(def_capitalize)
print(df)