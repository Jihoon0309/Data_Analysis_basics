### 원 그래프(심화)

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결


def custom_autopct(pct):
    # return ('%.1f%%' % pct) if pct>=10 else '' # %가 10이상인 것들만 보여줌
    return '{:.1f}%'.format(pct) if pct >= 10 else ''
values=[30, 25, 20, 13, 10, 2]
labels=['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff'] # 색지정
explode=[0.05]*6 # 칸을 띄움
wedgeprops={'width':0.7, 'edgecolor':'w', 'linewidth':2} # 도넛 모양으로 만듦 ,선 두께지정,테두리색 지정, 색 굵기 지정
plt.pie(values, labels=labels, autopct=custom_autopct,
colors=colors,  wedgeprops=wedgeprops, pctdistance=0.7) #(글자를 중심지로 띄움))

# DataFrame 활용
import pandas as pd
df=pd.read_excel('score.xlsx')
print(df)

grp=df.groupby('학교')
values=[grp.size()['북산고'], grp.size()['능남고']]

labels=['북산고', '능남고']
plt.pie(values, labels=labels)
plt.title('소속학교')
plt.show()