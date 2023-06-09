### 퀴즈

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)
print(df)

# 1) 영화 데이터를 활용하여 x 축은 영화, y 축은 평점인 막대 그래프를 만드시오.
plt.bar(df['영화'],df['평점'])
plt.show()

# 2) 앞에서 만든 막대 그래프에 제시된 세부 사항을 적용하시오.
plt.title('국내 Top 8 영화 평점 정보')
plt.xticks(rotation=90)
plt.xlabel('영화')
plt.ylabel('평점')
plt.show()

# 3) 개봉 연도별 평점 변화 추이를 꺾은선 그래프로 그리시오.
df_group = df.groupby('개봉 연도')['평점'].mean()
print(df_group)
plt.plot(df_group.index, df_group)
plt.show()

# 4) 앞에서 만든 그래프에 제시된 세부 사항을 적용하시오.
'''
- marker : 'o'
- x 축 눈금 : 5년 단위(2005, 2010, 2015, 2020)
- y 축 범위 : 최소7, 최대10
'''

plt.plot(df_group.index, df_group, marker='o')
plt.xticks([2005, 2010, 2015, 2020])
plt.ylim(7,10)
plt.show()

# 5) 평점이 9점 이상인 영화의 비율을 확인할 수 있는 원 그래프를 제시된 세부 사항을 적용하여 그리시오.
'''
- label : 9점 이상/ 9점 미만
- 퍼센트 : 소수점 첫째자리까지 표시
- 범례 : 그래프 우측에 표시
'''

filt=df['평점']>=9.0
values=[len(df[filt]), len(df[~filt])]
labels=['9점 이상', '9점 미만']

plt.pie(values,labels=labels, autopct='%.1f%%')
plt.legend(loc=(1,0.3))
plt.show()