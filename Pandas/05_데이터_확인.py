### 데이터 확인

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

### DataFrame 확인 = 계산 가능한 데이터에 대해 column별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌
print(df.describe())
print(df.info())

# 처음 5개의 row를 가져옴
print(df.head())        #괄호안에 숫자를 넣으면 그 갯수만큼 가져옴

# 마지막 5개의 row를 가져옴
print(df.tail())        #괄호안에 숫자를 넣으면 그 갯수만큼 가져옴

# 어떤 값을 가지고 있는지 한눈에 볼 수 있음
print(df.values)

# index 를 볼 수 있음
print(df.index)

# column 확인
print(df.columns)

# row, column 갯수 보여줌
print(df.shape)

### Serise 확인
print(df['키'].describe())

# 순서대로 데이터
print(df['키'].nlargest(3))     #괄호 숫자 만큼 순서대로

# 데이터 갯수
print(df['SW특기'].count())     #비어있는 값은 세지않음

# 중복 제외한 데이터
print(df['학교'].unique())
print(df['학교'].nunique())     #중복를 제어한 데이터의 갯수