### 누적 막대 그래프 (막대 그래프 하나 위에 계속 쌓음)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import pandas as pd
df=pd.read_excel('score.xlsx')
print(df)

plt.bar(df['이름'],df['국어'], label='국어')
plt.bar(df['이름'],df['영어'], bottom=df['국어'], label='영어') # 국어점수 위에 영어점수를 쌓음
plt.bar(df['이름'],df['수학'], bottom=df['국어']+df['영어'], label='수학')

plt.xticks(rotation=60)
plt.legend()
plt.show()