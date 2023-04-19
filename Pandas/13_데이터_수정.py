### 데이터 수정

import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')

## Column 수정
print(df['학교'].replace({'북산고':'상북고'}, inplace=True))
print(df)

df['SW특기']=df['SW특기'].str.lower() # SW특기 모두 소문자로
print(df)
df['SW특기']=df['SW특기'].str.upper() # 대문자로 변경
print(df)

df['학교']=df['학교']+'등학교' # 학교 데이터 + 등학교
print(df)

## Column 추가
df['총합'] = df['국어'] + df['영어']+ df['수학']+ df['과학']+ df['사회']
print(df)

df['결과']='Fail' # 결과 Column 추가하고 전체 데이터를 Fail
print(df)

df.loc[df['총합']>400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터에 대해 결과 값을 pass로 변경 앞이 if문 이라고 보면됨
print(df)

## Column 삭제
print(df.drop(columns=['총합'])) # 총합 Column 삭제
print(df.drop(columns=['국어','영어','수학'])) # 총합 Column 삭제

## row 삭제
print(df.drop(index='4번')) # index 해당하는 row 삭제
filt=df['수학']<80
print(df.drop(index=df[filt].index))# filt에 해당하는 index들 삭제

## row 추가
df.loc['9번'] = ['이정환','해남고등학교',184,90,90,90,90,90,'Kotlin',450,'Pass']
print(df)

## Cell 수정
df.loc['4번', 'SW특기'] = 'Python'
print(df)
df.loc['5번', ['학교','SW특기']] = ['능남고등학교','C']
print(df)

## Column 순서 변경
cols=list(df.columns)
print(cols)
df=df[[cols[-1]]+cols[0:-1]] # 맨 뒤 결과 column을 앞으로 가져오고 나머지 데이터를 합쳐서 뒤로 가져옴
print(df)

## Column 이름 변경
df=df[['결과','이름','학교']]
print(df)
df.columns = ['Result', 'Name', 'School']
print(df)