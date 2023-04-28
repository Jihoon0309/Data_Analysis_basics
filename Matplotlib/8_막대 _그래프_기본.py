### 막대 그래프 (기본)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

labels=['강백호', '서태웅', '정대만'] # 이름
values=[190, 187, 184] # 키
colors=['r','g','b'] # 막대그래프 색상지정

plt.bar(labels, values, color=colors, alpha=0.5)


labels=['강백호', '서태웅', '정대만'] # 이름
values=[190, 187, 184] # 키
plt.bar(labels, values, width=0.5) # 막대 두께설정
plt.ylim(175, 195) # y축 범위 지정
plt.xticks(rotation=45) # x 축의 데이터 각도를 45도로 설정
plt.yticks(rotation=45) # y 축의 데이터 각도를 45도로 설정


labels=['강백호', '서태웅', '정대만'] # 이름
values=[190, 187, 184] # 키
ticks=['1번', '2번', '3번']

plt.bar(labels, values)
plt.xticks(labels, ticks, rotation=90) # 이름을 ticks로 바꿈, 90도로 설정
plt.show()