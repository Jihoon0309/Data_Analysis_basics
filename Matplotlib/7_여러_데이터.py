### 여러 데이터

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]

# COVID-19 백신 종류별 접종 인구
days=[1, 2, 3]
az=[2,4, 8] # (단위 : 만명) 1~3일까지 az 접종인구
pfizer=[5, 1, 3]
moderna=[1, 2, 5]


plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', ls='--')
plt.plot(days, moderna, label='moderna', marker='s', ls='-.')
plt.legend(ncol=3) # 아래로 말고 옆으로 보여줌
plt.show()










