### Pandas = 파이썬에서 사용하는 데이터 분석 라이브러리
### Series = 1차원 데이터
import pandas as pd

### Series 객체 생성
#1월~4뤌까지 평균온도 데이터
temp=pd.Series([-20,-10,10,20])
print(temp)

### Series 객체 생성(Index 지정)
temp=pd.Series([-20,-10,10,20], index=['Jan','Feb','Mar','Apr'])
#Index 'Jan' 데이터값 출력
print(temp['Jan'])