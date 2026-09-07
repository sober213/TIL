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
### 문자열

#### 1 코드체계
문자열 등을 코드로 표현하는 방식
#### 2 유니코드
문자열과 코드를 매치시켜 놓은 범용 
ASCII(American S?? Code I?? I??) 미국 표준 utf-8 
#### 3 문자열 자료형과 연산, 메서드
문자열은 시퀀스 자료형(인덱스, 반복가능), 불변(임의 변경 불가)
+, * 등 연산자를 사용할 수 있음 txt.find()메서드, txt.strip(), "-".join(txt)
#### 4 고지식한 알고리즘
brute force- 고지식하게 일일이 비교해보는 식의 문자열 일치패턴 탐색
할 줄은 알아야 됨
#### 4-1 KMP알고리즘
좀 더 나은 탐색방식? ???-무어는 실제 상용
#### 5 암호화
시저의 암호문(한 칸씩), 완전일치- 하나에 대응
___

```


```