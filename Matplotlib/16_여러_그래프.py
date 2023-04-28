### 산점도 그래프

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import pandas as pd
df=pd.read_excel('score.xlsx')

fig, axs = plt.subplots(2, 2, figsize=(15,10)) # 몇개의 plot를 만들것이가?(세로개수, 가로개수)
fig.suptitle('여러 그래프 넣기')

# 첫 번째 그래프
axs[0, 0].bar(df['이름'], df['국어'], label='국어점수')
axs[0, 0].set_title('첫 번째 그래프')
axs[0, 0].legend() # 범례
axs[0, 0].set(xlabel='이름', ylabel='점수') # x, y 축 label
axs[0, 0].set_facecolor('lightyellow') # 전경 색
axs[0, 0].grid(linestyle='--', linewidth=0.5)

# 두 번쨰 그래프
axs[0, 1].plot(df['이름'], df['수학'], label='수학')
axs[0, 1].plot(df['이름'], df['영어'], label='영어')
axs[0, 1].legend()

# 세 번쨰 그래프
axs[1, 0].barh(df['이름'], df['키'])

#네 번쨰 그래프
axs[1, 1].plot(df['이름'], df['사회'], color='g', alpha=0.5)

plt.show()