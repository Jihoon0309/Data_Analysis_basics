### 그룹화 = 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')

print(df.groupby('학교').get_group('북산고'))
print(df.groupby('학교').get_group('능남고'))

# print(df.groupby('학교').mean()) # 계산 가능한 데이터들의 평균값 (왜 오류 나는지 모르겠음)
print(df.groupby('학교').size()) # 각 그룹의 크기
print(df.groupby('학교').size()['능남고'])

print(df.groupby('학교')['국어'].mean()) # 원하는 데이터 중에서 평균값

print(df.groupby('학교')[['국어','영어','수학']].mean())

df['학년']=[3,3,2,1,1,3,2,2] # 학년 column 추가
print(df)

print(df.groupby(['학교','학년'])['키'].mean())

print(df.groupby(['학교','학년']).sum())

print(df.groupby('학교')[['이름','SW특기']].count())

school=df.groupby('학교')
print(school['학년'].value_counts()) # 학교로 그룹화 한 뒤 학년별 학생 수 가져옴

print(school['학년'].value_counts().loc['북산고']) # 북산고 학년별 학생 수
print(school['학년'].value_counts(normalize=True).loc['북산고']) # 학생들의 수 데이터를 퍼센트로 비교