### 데이터 정렬

import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')

print(df.sort_values('키')) # 오름차순 정렬
print(df.sort_values('키', ascending=False)) # 내림차순 정렬

print(df.sort_values(['수학','영어'])) # 수학 기준으로 오름차순 수학 점수가 같으면 영어 성적 기준으로 오름차순
print(df.sort_values(['수학','영어'], ascending=False)) # 수학 기준으로 내림차순 수학 점수가 같으면 영어 성적 기준으로 내림차순

print(df.sort_values(['수학','영어'], ascending=[True,False])) # 수학은 오름차순 영어는 내림차순

print(df['키'].sort_values(ascending=False)) # 키 만 내림차순으로 보고싶을때

print(df.sort_index(ascending=False)) # index기준 내림차순