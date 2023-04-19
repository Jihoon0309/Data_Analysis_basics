### 결측치 = 비어있는 데이터

import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')

## 데이터 채우기 fillna
print(df.fillna('없음')) # NaN 데이터를 빈칸으로 채움

import numpy as np
df['학교']=np.NaN # 모든 학교 데이터를 NaN
print(df)
print(df.fillna('모름', inplace=True))
print(df)

df=pd.read_excel('score.xlsx', index_col='지원번호')
df['SW특기'].fillna('확인 중', inplace=True) # SW특기 데이터 중에서 NaN에서만 변경
print(df)

## 데이터 제외하기 dropna
df=pd.read_excel('score.xlsx', index_col='지원번호')
print(df.dropna()) # NaN 데이터가 있으면 삭제

# asxi : index(row(행) 삭제) or columns(column(열) 삭제)
# how : any(데이터 중에 하나라도 NaN 일때) or all(데이터 전체가 NaN 일때)
print(df.dropna(axis='index', how='any'))
print(df.dropna(axis='columns'))

df['학교']=np.NaN # 학교를 모두 NaN
print(df.dropna(axis='columns', how='all')) # 데이터 전체가 NaN인 경우 Column삭제
