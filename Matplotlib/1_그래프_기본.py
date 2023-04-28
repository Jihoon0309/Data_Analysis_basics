### Matplotlib = 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리
### 그래프 기본
import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

import matplotlib.font_manager as fm
# print(fm.fontManager.ttflist) # 사용 가능한 폰트 확인
# [f.name for f in fm.fontManager.ttflist]


x=[1,2,3]
y=[2,4,8]
plt.plot(x,y)
# plt.show()

## Title 설정
plt.title('꺾은선 그래프')
# plt.show()

plt.plot([-1, 0, 1],[-5, -1, 2])
plt.show()