### 데이터 선택(기본)

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)

# column 선택 (label)
# print(df[['키','이름']])

# column 선택 (정수 index) = column 이름을 모를때 유용함

# print(df.columns[0])
# print(df[df.columns[0]])

### 슬라이싱
print(df['영어'][0:5])
print(df[['이름','키']][:3])
# 전체 데이터
print(df[3:])