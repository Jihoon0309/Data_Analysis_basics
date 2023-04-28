### 축

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]
plt.plot(x,y)
plt.title('꺾은선 그래프', size=10)
# plt.show()

plt.xlabel('X축', color='red' , loc='right') #loc=left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top') #loc=top, center, bottom
# plt.show()

plt.xticks([1,2,3]) # x축 나타내는 숫자
plt.yticks([3,6,9,12]) # y축 나타내는 숫자
plt.show()