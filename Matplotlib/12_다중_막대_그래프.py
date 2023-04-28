### 다중 막대 그래프 (그래프를 여러개를 옆으로 보여줌)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import pandas as pd
df=pd.read_excel('score.xlsx')
print(df)

import numpy as np
N=df.shape[0]
index=np.arange(N)
plt.figure(figsize=(10,5))
plt.title('학생별 성적')

w=0.25
plt.bar(index-w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index+w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=60)
plt.show()