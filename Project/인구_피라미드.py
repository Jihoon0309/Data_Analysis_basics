import pandas as pd

# 남자 데이터
df_m=pd.read_excel('202303_202303_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,E:Y') 
# 3행 스킵, 인덱스=(행정기관), B,E~Y까지 가져옴

# 전국 데이터를 숫자로 변경
df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int) # ','를 ''로 변경하고 숫자를 int형으로 변경
print(df_m.iloc[0]) # 0번째 행

# 여자 데이터
df_w=pd.read_excel('202303_202303_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,AB:AV') 
# 3행 스킵, 인덱스=(행정기관), B,Z~AV까지 가져옴
# print(df_w) # 0~4세.1 로 나오는데 이유은 같은 이름이 있기때문

df_w.columns = df_m.columns # 컬럼명 통일
# print(df_w)

df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int) # ','를 ''로 변경하고 숫자를 int형으로 변경
# print(df_w)


# 데이터 시각화
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

plt.figure(figsize=(10, 7))
plt.barh(df_m.columns, -df_m.iloc[0]//1000) # 단위 : 천 명 ,-df_m.iloc[0] 반대로 그림 그래프를 대칭으로 보여줌
plt.barh(df_w.columns, df_w.iloc[0]//1000) # 단위 : 천 명
plt.title('2023년 대한민국 인구 피라미드')
plt.savefig('2023_인구피라미드.png',dpi=100)
plt.show()