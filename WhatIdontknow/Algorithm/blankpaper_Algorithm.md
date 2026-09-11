## 백지복습

### 2차원 배열

#### 1-1 행과 열
row 와 col
#### 1-2 행렬 배치

#### 1-3 지그재그형 배열

#### 1-4 열 방향으로 순회?


### 카운팅 정렬
정수는 음수, 0형태 
자연수는 0 포함? 
정수로 표현되는 자료만 가능 
DATA의 특정 값이 등장하는 횟수를 COUNTS 리스트에 저장
TEMP 리스트에 n-1, -1, -1
```

def counting_sort(DATA, COUNTS, k):
  

  COUNTS = [0] * (k + 1)

  for i in range(len(DATA)):
    COUNTS[DATA[i]] += 1

  for i in range(1, k + 1):
    COUNTS[i] += COUNTS[i - 1]

  for i in range(n - 1, -1, -1):
    COUNTS[i] -= 1
    TEMP[COUNTS[DATA[i]]] = DATA[i]



```
지금 내가 뭘 모르는 거지?
낙타의 현 위치 인덱스가 오아시스 자리 목록을 벗어났을 때 나는 오류를 어떻게 고치는지 모른다.
낙타 위치 반복문이 break없이 끝났을 때 0을 반환하는 방법, 정확히는 맨 끝 오아시스에 낙타를 위치시킨 다음
  

### String

#### 1 코드체계
문자열 등을 코드로 표현하는 방식/ 인코딩 표준화 
#### 2 유니코드
문자열과 코드를 매치시켜 놓은 범용 인코딩 양식
ASCII(American Standard Code? Information Interchange) 미국 표준 utf-8 
글자 깨지는 건 us??-KOR?로 변환한 것을 utf-8로 읽어들여서 매칭이 안 됨 
#### 3 문자열 자료형과 연산, 메서드
문자열은 시퀀스 자료형(인덱스, 반복가능), 불변(임의 변경 불가)
list(input())? 리스트 형태로 받을 수 있음
+, * 등 연산자를 사용할 수 있음 txt.find()메서드, txt.strip(), "-".join(txt)
#### 4 고지식한 알고리즘 패턴 탐색 
brute force- 고지식하게 일일이 비교해보는 식의 문자열 일치패턴 탐색
p, ? len(p) = M 포인터 i, j 설정
```
def finding_brute_force(t, p, k?):
  len(t) = M # 주어진 문자열?
  len(p) = N # 찾으려는 패턴 
  i = 0
  j = 0
  while t[i] < M and p[i] < N:
    for i  _ in range()
      if t[i] != p[i]:
        i = i - j
        j = 0
      i + 1
      j + 1
  if j == M:
    return i - j???
```
할 줄은 알아야 됨
#### 4-1 KMP알고리즘
좀 더 나은 탐색방식? 보이어-무어는 실제 상용 프로그램에 사용
#### 5 암호화
시저의 암호문(한 칸씩), 단일치환- 문자 하나에 고정된 문자열 하나 지정해 무수한 키


### Stack 

#### 1 스택이란? 
데이터를 저장하는 대표적 선형 자료구조(선형: 자료의 원소가 1 : 1 매칭됨, 비선형: 1 : N)
후입선출-last in, first out <-겁쟁이 행동 (first in, last out) 
리스트 인덱스 사용, top을 설정, 하나씩 쌓아가는 형태
#### 2 스택 연산?
메서드 사용과 인덱스 사용
.append
#### 3 함수 스택?
함수도 스택에 맞춰 쓴다?
#### 3-2 시스템 스택? 
```



```