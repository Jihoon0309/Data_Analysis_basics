### 막대 그래프 (심화)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

labels=['강백호', '서태웅', '정대만'] # 이름
values=[190, 187, 184] # 키

plt.barh(labels, values) #가로 막대그래프
plt.xlim(175, 195)

bar=plt.bar(labels, values)
bar[0].set_hatch('/') # 그래프 안을 /로 채움
bar[1].set_hatch('x') # 그래프 안을 x로 채움
bar[2].set_hatch('..') # 그래프 안을 ..으로 채움

bar=plt.bar(labels, values)
plt.ylim(175, 195)
for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height(), values[idx], ha='center', color='blue' )
plt.show()