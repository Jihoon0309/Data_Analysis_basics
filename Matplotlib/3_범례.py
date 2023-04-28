### 범례(legned)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]

plt.plot(x, y, label='무슨 데이터')
plt.legend(loc='upper right') # loc=위치조정 정의안하면 알아서 지정함
# plt.show()

plt.plot(x, y, label='범례')
plt.legend(loc=(0.5, 0.5)) # 세부적으로 지정가능
plt.show()