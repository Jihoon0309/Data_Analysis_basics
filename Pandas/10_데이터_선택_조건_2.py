### 데이터 선택 (조건) = 조건에 해당하는 데이터 선택

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')

##str 함수
filt=df['이름'].str.startswith('송') # '송'씨 성을 가진 사람
print(df[filt])

filt=df['이름'].str.contains('태') # '태'가 이름에 들어간 모든 사람
print(df[filt])

print(df[~filt]) # ~는 제거

langs=['Python','Java']
filt=df['SW특기'].isin(langs) # SW특기가 langs인 사람
print(df[filt])

langs=['python','java']
filt=df['SW특기'].str.lower().isin(langs) # sw특기를 소문자로 변경후
print(df[filt])

filt=df['SW특기'].str.contains('Java', na=False) # NaN 있으면 오류나서 na속성으로 False로변경
print(df[filt])