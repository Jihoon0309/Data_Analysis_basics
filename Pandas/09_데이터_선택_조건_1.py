### 데이터 선택 (조건) = 조건에 해당하는 데이터 선택

import pandas as pd

df=pd.read_excel('score.xlsx', index_col='지원번호')


print(df['키']>=185) # True,False로 나옴

filt = (df['키']>=185)
print(df[filt]) # 저 조건에 맞는 데이터들만 가져옴
print(df[~filt]) # 저 조건에 맞지 않는 데이터들만 가져옴

print(df.loc[df['키']>=185,['수학','이름']])

## 다양한 조건
# & (and)
print(df.loc[(df['키']>=185) & (df['학교']=='북산고')])

# | (or)
print(df.loc[(df['키']<170) | (df['키']>200)])