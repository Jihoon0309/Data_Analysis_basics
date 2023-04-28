### 텍스트

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]

plt.plot(x, y, marker='o')
for idx, txt in enumerate(y): 
    plt.text(x[idx], y[idx]+0.3, txt, ha='center', color='blue') # ha=수평 맞춤
plt.show()

