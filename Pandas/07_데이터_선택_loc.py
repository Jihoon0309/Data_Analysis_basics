### 데이터 선택 (loc) = 이름을 이용하여 원하는 row에서 원하는 col 선택

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')
print(df)
# index에 해당하는 전체데이터
print(df.loc['1번'])

# 일부 column
print(df.loc['1번','국어'])     # index 1번에 해당하는 국어 데이터
print(df.loc[['1번','2번'],'국어'])
print(df.loc[['1번','2번'],['이름','국어','영어']])

print(df.loc['1번':'5번', '국어':'사회'])       #슬라이싱 이용 이때는 뒤에 값 포함