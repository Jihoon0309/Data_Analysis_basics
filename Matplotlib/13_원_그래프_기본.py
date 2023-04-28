### 원 그래프(기본)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

values=[30, 25, 20, 13, 10, 2]
labels=['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']

# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False) # %보여줌, 시작위치, 시계방향

# explode=[0.2, 0.1, 0, 0, 0, 0] # 띄워서 보여줌
explode=[0.05]*6
plt.figure(figsize=(10,5))
plt.title('언어별 선호도')
plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2,0.3), title='언어')

plt.show()

