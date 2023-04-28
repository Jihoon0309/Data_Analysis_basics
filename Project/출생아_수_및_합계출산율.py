# 합계 출산율 = 가임기간(15~49세)에 낳을 것으로 기대되는 평균 출생아 수

import pandas as pd
df = pd.read_excel('142801_20230428194253024_excel.xlsx', skiprows=2, nrows=2 ,index_col=0)
# 두번째행까지 스캡, 2번쨰 행까지 불러오기, 인덱스는 0행
# print(df.index.values) # ['출생아\xa0수' '합계\xa0출산율'] 이렇게 들어가있음
df.rename(index={'출생아\xa0수':'출생아 수','합계\xa0출산율':'합계 출산율'}, inplace=True)
# print(df.loc['출생아 수']) # df.iloc[0]
df=df.T # 행과열의 위치를 바꿔줌

# 데이터 시각화
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

# plt.plot(df.index, df['출생아 수'])
# plt.plot(df.index, df['합계 출산율'])

fig, ax1 = plt.subplots(figsize=(13, 5))
fig.suptitle('출생아 수 및 합계출산율')

ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250,700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d') # 주황색
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val+12, val, ha='center')



ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color='#ffd100', marker='o', ms=15, lw=5, mec='w', mew=3) # 노란색
for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val+0.08, val, ha='center')
plt.show()