## 백지복습

### 2차원 배열

#### 1-1 행과 열
2차원 리스트 선언(N * M)을 위해 필요한 건 행개수(N)와 열개수(M)
i(r)는 행좌표 (행개수 순회) j(c)는 열좌표(열개수 순회) 
#### 1-2 열 방향 순회
```
for j in range(M):
  for i in range(N):
    print(arr[i][j])
```
#### 1-3 지그재그형 순회
```
for i in range(N):
  for j in range(M):
    print(arr[i][j + (M - 1 - 2 * j) * (i % 2)])
```
#### 1-4 행렬 배치
```
for i in range(N):
  for j in range(N):
    if i < j:
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
#### 1-5 벡터
하나를 기준점으로 상하좌우를 지정
```
for i in range(N):
  for j in range(M):
    s = arr[i][j]
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
      for c in range(1, k + 1)
        ni, nj = i + di * c, j + dj * c
        if 0 <= ni <= N and 0 <= nj <= M:
          s += arr[ni][nj]
    if s > max_v:
      max_v = s
      
```

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

### 선택 정렬, 셀렉트 알고리즘
```
def select(arr, k):
```
k번째로 작은 원소를 반환하는 함수
```
  for i in range(0, k):
    min_idx = i
    for j in range(j + 1, len(arr)):
      if arr[j] > arr[min_idx]
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr[k-1]
```

### 큐(Queue)

#### 1 FIFO
선입선출형 자료구조, 들어온 순서대로 나간다 ex-은행대기열, 프린터 대기열
#### 2 선형 큐
기본적 형태, front와 rear형태 front- 마지막으로 삭제한 원소의 위치
#### 2-1 큐 구조
rear - 마지막으로 추가한 원소의 위치 + 1 
만들 때는 둘 다 -1, .enque(item)로 원소 추가 시 rear한 칸 나가며 남은 자리에 추가 .dequeue(item)로 원소 삭제하며 삭제하고 남은 자리에 front들어옴 isempty(), isfull()
#### 2-2 원형 큐
선형 큐는 front가 한번 앞으로 나가버리면 다시 돌아가 재활용이 안 됨
한 번 포화되면 원소를 더 추가하기 힘들어 이를 보완하기 위한 형태
앞과 뒤를 붙여서 순환식
#### 3 연결 큐, 우선순위 큐?
연결 리스트를 이용해 연결한 큐? 구조?
#### 4 BFS
너비 우선 탐색- 큐를 사용, 마지막으로 들른 곳을 visited에 추가하며 인접점 우선탐색
들른 곳은 들렀다고 표시하며 큐에서 제거함  
#### 5 deque
덱, 양옆에서 넣고 뺄 수 있는 리스트 형태의 큐(유용하다)