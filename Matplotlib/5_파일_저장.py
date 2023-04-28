### 파일 저장

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]

# plt.plot(x, y)
# plt.savefig('graph.png', dpi=100)

plt.figure(dpi=200)
plt.plot(x, y)
plt.savefig('graph_200.png', dpi=100) # dpi=200으로 그리고 dpi=100으로 저장