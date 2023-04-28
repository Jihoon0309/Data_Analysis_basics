### DataFrame 활용

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import pandas as pd
df=pd.read_excel('score.xlsx')
print(df)

# plt.plot(df['지원번호'],df['키'])
plt.plot(df['지원번호'],df['영어'])
plt.plot(df['지원번호'],df['수학'])
plt.grid(color='purple', alpha=0.5, linestyle='--', linewidth=2) # 격자생성 axis='x' 하면 x선만 생성 y하면 y선만 생성
plt.show()