### 데이터 선택 (iloc) = 위치(인덱스) 이용해서 원하는 row에서 원하는 col 선택

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')


print(df.iloc[0])       # df.loc['1번']와 값은 값
print(df.iloc[0:5])

# 원하는 col
print(df.iloc[0,1])     # 0번째 행에 1번째 열을 가져옴
print(df.iloc[[0,1],2])     # 여러 학생의 2번쨰 열 정보
print(df.iloc[[0,1],[3,4]])     # 여러 학생의 여러개의 열 정보
print(df.iloc[0:5, 3:8])        #슬라이싱경우 괄호 추가 안해도됨

