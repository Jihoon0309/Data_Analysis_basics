### 스타일

import matplotlib.pyplot as plt

## 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용시 마이너스 글자 깨지는 형상 해결

x=[1,2,3]
y=[2,4,8]

plt.plot(x, y, linewidth=10) # 선 굵기
plt.show()

# 마커(marker)
plt.plot(x, y, marker='o') # 데이터 있는 부분에 o로 표시
plt.plot(x, y, marker='o', linestyle='None') # 선표시 x
plt.plot(x, y, marker='v', markersize=10) # 화살표 표시, 마커사이즈 키우기
plt.plot(x, y, marker='X', markersize=10) # X 표시
plt.plot(x, y, marker='X', markersize=10, markeredgecolor='red') # 마커 테두리 색 변경
plt.plot(x, y, marker='X', markersize=10, markeredgecolor='red', markerfacecolor='yellow')  # 마커 색 변경
plt.show()

# 선 스타일
plt.plot(x, y, linestyle=':') # 점선
plt.plot(x, y, linestyle='--') # 조금더 두꺼운 점선
plt.plot(x, y, linestyle='-.') # -.
plt.plot(x, y, linestyle='-') # 실선
plt.show()

# 색깔
plt.plot(x, y, color='pink') # 분홍색
plt.plot(x, y, color='#ff0000') # 빨간색
plt.plot(x, y, color='b') # 파란색
plt.plot(x, y, color='g') # 초록색
plt.show()

# 포맷
plt.plot(x, y, 'ro--') # color, marker, linestyle
plt.plot(x, y, 'bv:')
plt.plot(x, y, 'go') # (x, y, color='g', marker='o', linestyle='None')랑 같음
plt.show()

# 축약어
plt.plot(x, y, marker='o', mfc='red', ms=10, mec='blue', ls=':')
# mfc=markerfacecolor, ms=markersize, mec=markeredgecolor, ls=linestyle
plt.show()

# 투명도
plt.plot(x, y, marker='o', mfc='red', ms=10, alpha=0.3) # alpha 투명도
plt.show()

# 그래프 크기
plt.figure(figsize=(10, 5)) # 가로 , 세로
plt.figure(figsize=(10,5), dpi=200) # dots per inch = 확대 축소
plt.plot(x, y)
plt.show()

# 배경색
plt.figure(facecolor='yellow') # 그래프 밖에 배경색 지정
plt.figure(facecolor='#a1c3ff')
plt.plot(x, y)
plt.show()