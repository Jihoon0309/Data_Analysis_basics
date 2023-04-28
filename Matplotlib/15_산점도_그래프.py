### 산점도 그래프

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import pandas as pd
import numpy as np
df=pd.read_excel('score.xlsx')

df['학년']=[3, 3, 2, 1, 1, 3, 2, 2]
print(df)

sizes = df['학년']*500 # 학년별로 크기에 따라 달라짐

plt.figure(figsize=(7,7))
plt.scatter(df['영어'],df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3) #학년별로 색을 지정해줌
plt.xlabel('영어점수')
plt.ylabel('수학점수')
plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.5, orientation='horizontal') # 크기지정, 가로지정 
plt.show()

