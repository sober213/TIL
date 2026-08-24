## 백지복습

### set{}의 교집합을 구할 때 
`set1 & set2` or `set1.intersection(set2)`

### set{}의 합집합을 구할 때 
`set1 | set2` `set1.union(set2)`
중복 x  순서x 

### 함수 작성
```
def func_1(arg):
  arg = 
  return

result = func_1(arg)
print(result)

```
### for 반복문 
`for i in range():`

### 반복문에서 enumerate
`for i, s in enumerate(list):`
인덱스와 값을 둘 다 구하고 싶을 때?


### class
함수와 메서드를 하나의 값으로 묶어서 쓰는 단위?
클래스 = 설계도

인스턴스 = 설계도로 만들어진 차 
가수 = class 아이유는 인스턴스다x 아이유는 가수 클래스의 인스턴스다. 

``` 

class Myth: #<-클래스 정의
  number_of_myth = 0 #<-클래스 변수   
  def __init__ (self, name): #<-인스턴스 변수 설정, 생성자 메서드
    self.name = name #<- self 뒤 name은 인스턴스 메서드, =뒤 name은 인스턴스 변수
    Myth.number_of_myth += 1 #<- 클래스 변수임을 표시? 클래스 메서드?
  @staticmethod #<-스태틱 메서드, 고정값 출력?
  def description():
    return('신화는 영웅이나 신들이 나오는 이야기다')
m1 = Myth('dangun') #<-인스턴스 생성? 클래스를 앞에 붙임 
m2 = Myth('greek & rome')

print(m1.name)#<-인스턴스 메서드 호출
print(m2.name)#
print(Myth.number_of_myth)
print(Myth.description())#<- 얘도 메서드다

```

### class, instance, static method
```

class Car:
  wheels = 4
  def __init__ (self, engine, driving_system, sound):
    self.engine = engine
    self.driving_system = driving_system
    self.sound = sound #<- 생성자 메서드는 인스턴스 변수만 설정
  @classmethod
  def increase_wheels(cls):
    cls.wheels += 1 #<= 클래스 메서드 정의  
    print('법이 개정되어 차 바퀴 수가 1증가했습니다.')
  def drive(self):
    print(self.sound)
    return self.engine #<=이게 인스턴스 메서드 정의, 인자 추가하기
  def introduce(self):
    print(...) 
  
  @staticmethod
  def description():
    return('자동차는 인간과 화물을 옮기는 기계다.') #<- 스태틱 메서드 정의

```

### 예외처리 
에러났을 때 일일이 원인을 찾아 고치기보다 일부 부분을 처음부터 예외상황을 상정하고 작성해 코드 전체가 작동할 수 있게끔 한다.

```
data = {'name' : '홍길동'}

try: #<-에러가 날 법한 코드 넣기
  age = data['age'] #<- 없는 키를 호출해 KeyError 발생
except KeyError: #<- 해당 에러가 발생했을 때 어떻게 작동(처리)할지 규정 
  print('data에 'age' 키가 존재하지 않습니다.')
  data['age'] = 30 
  print(data)

arr = ['안녕', '하세', '요']
try: 
  for i in range(4):
    print(arr.pop())
  print(arr) #<- 4번째 값은 존재하지 않아 IndexError 발생
except IndexError:
  print('더 이상 pop할 값이 존재하지 않습니다.')
  print(arr)

word = '3.15'
try :
  int(word) #<- 문자열을 벗겨도 정수 변환이 안 돼 ValueError 발생
except ValueError: 
  "정수로 변환할 수 있는 값을 입력해주세요."
```

### 상속 
```
class BaseModel:
  PK = 1
  TYPE = BASE MODEL
  def __init__(self, title, year):
    self.PK = BaseModel.PK
    self.title = title
    self.year = year
    BaseModel.PK += 1 
  def save(self):
    print('데이터를 저장합니다.')
class Novel(BaseModel): #<- 클래스 상속 
  def __init__(self, title, year, author):
    super().__init__(title, year) #<- 상속받은 Basemodel 생성자 한번 작동?
    self.author = author #<- 상속받은 class의 고유 요소 설정

```

### 다중상속
```
class BaseModel:
  PK = 1
  TYPE = Base Model
  def __init__(self, title, year):
    self.PK = BaseModel.PK
    self.title = title
    self.year = year 
    

class Novel(BaseModel):
  def __init__(self, title, year, author):
  super().__init__(title, year)
  self.author = author

class Other(BaseModel):
  def __init__(self, title, year, **kwargs):
  super().__init__(title, year, **kwargs)
  

class ExtendedModel(Novel, Other):
  def __init__(self, *args, extended_type, **kwargs):
  super().__init__(*args, **kwargs)
  extended_type.self = extended_type

def display_info(self):
  cls = type.self
  print(f'PK: {cls.PK}, TYPE: {cls.TYPE}, Extended Type: {self.extended_type})

def save(self):
  print('데이터를 저장합니다.')


extended_instance = ExtendedModel(title, year, author, extended_type)

extended_instance.display_info()
extended_save()



```



### 골격 4종

1. 누적
total = 0
for x in data:
total += x
return total

2. 카운팅
cnt = 0
for x in data:
if 조건:
cnt += 1
return cnt

3. 탐색
best = data[0]
best_idx = 0
for i, x in enumerate(data):
if x > best:
best = x
best_idx = i
return best_idx

4. 필터링
result = []
for x in data:
if 조건:
result.append(x)
return result




#### 보충1회차 0814
```
total = 0 
for x in data:
  total += x
return total

cnt = 0
for x in data:
  if조건:
    cnt += 1
return cnt

best = data[0]
for x in data:
  if x > best
    best = x
return best     #<-탐색 틀림

max_score = data[0]
max_idx = 0
for i, x in enumerate(list[]):
  if score < max_score:
    max_score = score  
  if list[idx] = max_score: 
    max_idx.append(idx)
return max_idx, max_score #<- 필터링 틀림

best = data[0]
best_idx = i
for i, x in enumerate(data):
  if x > best
    best = x
    best_idx = i
return best_idx

result = []
for x in data:
  if 조건문:
    data_1.append(x)
return result

total = x
for x in data:
total += x
return total

cnt = 0
for x in data:
if 조건:
cnt += 1
return cnt

best = data[0]
best_idx = 0
for i, x in enumerate(data):
if x > best
best = x
best_idx = i
return best_idx

result = []
for x in data:
if 조건문:
result.append(x)
return result

```
**1주차 피드백 역질문 답변**
1. 2번에서 cnt = 0을 for문 안쪽에 쓰면 어떻게 될까요?
   *A.* 0. B자리에 둔 이상 반복문이 돌 때마다 초기화되어 C자리로 갈 마지막 순회에서 'present'만 반영된 cnt = 0이 반환될 것이다.
2. 그럼 "1차원 리스트에서 과락 인원 수와 최고점을 동시에 구하라" 는 문제라면 반복문이 몇 겹일까요? 그리고 "3차원 리스트(학교 > 반 > 학생)에서 과락 인원 수만 구하라" 는 몇 겹일까요?
   *A.* 한 겹. 리스트를 한 번만 벗겨도 된다. 세 겹. 조건과 비교할 학생 데이터에 접근하려면 세 번을 써야 된다. 
3. 지문의 "점수는 0 이상 100 이하" 가 "점수는 -100 이상 100 이하" 로 바뀌면, max_score = 0 버전은 어떤 입력에서 틀릴까요?
직접 그 입력을 하나 만들어서 두 버전을 돌려보고 결과를 적어보세요.
   *A.* analyze_scores([[-1, -30]])를 설정했을 때 max_score = 0은 (2, 0)을 출력,
   max_score = classes[0][0]은 (2, -1)을 출력했다. 
   


### 보충 2주차 

problem1. 리스트로 주어진 값에서 메뉴별 매출합계를 딕셔너리 형태로 반환할 때
내가 모르는 것: 시작값을 설정할 때 매출합계를 각 메뉴마다 매칭시키는 법과 매출 합계를
딕셔너리 형태로 묶을 때 기존 반복문을 어떻게 변형하는지
딕셔너리에 값 추가: sum_category[coffee] = category_total 
key = category? value = sum_

total = 0 #total을 여러 개로 설정하면 안 됨(예시마다 변형x)
for x in data:
if x ==
total +=  
elif x == 
elif x == 
return total

**2주차 피드백 역질문 답변**

```

```

### 보충 3주차
튜플/ 리스트/ 딕셔너리 다루기


```
# 지문에서 찾은 신호어 : 'target물품이 놓인', '모든 칸의 위치를'
# 선택한 골격         : (이 문제는 골격이 2개 이상입니다. 모두 쓰세요) 조건문, 필터링
# 그렇게 판단한 이유   : 특정 조건을 만족하는지 확인해야 하니 조건문 사용.
#                     조건을 만족한 물품 위치를 리스트에 모아 반환해야 하니 필터링
#
# 반환 형태 (지문에서 그대로 옮겨 적기) : '(층, 칸)형태의 튜플로 만들어 리스트에 모아
#                                     반환하는'
# 추가 질문 1: 2주차 03번에서는 조건에 맞는 위치를 '인덱스 하나'로 모았습니다.
#             이 문제에서 위치를 표현하려면 숫자가 몇 개 필요한가요? 왜 그런가요?
# 답 : 두 개 필요하다. 층 위치 역시 표시해야 하니 기존 인덱스에 하나가 더해진다. 
#
# 추가 질문 2: 지문의 '위쪽 층부터, 같은 층 안에서는 왼쪽 칸부터'는
#             바깥 반복문과 안쪽 반복문 중 무엇이 층을 돌아야 한다는 뜻인가요?
# 답 : 바깥 반복문

# 변수 이름 | 담기는 것 | 시작값 | 도는 범위 | 어느 반복문 안/밖에서 만드는가
# r        | 선반 층 리스트| shelf[0] | shelf[0]부터 shelf길이까지 | 안쪽 반복문 밖/ 바깥 반복문 안 
# t_loc_lst| target물품의 위치 튜플 |  []  | 0번부터 층 수-1까지|바깥 반복문 밖
# c        | 칸별 물품 번호 |  0  |  0부터 r길이까지 | 안쪽 반복문 안
# 0. [결과를 담는 변수 - 시작값]
#     t_loc_lst = []로 한다.
#    [왜]
#     안쪽 반복문에서 조건을 만족한 값을 모은 튜플을 추가해야 하니 빈 리스트로 둔다.
#      
# 1. [바깥 반복문은 무엇을 도는가]
#     선반의 층을 돈다.
#    [왜]
#     조건을 따지기 전 맨 위층부터 차례로 나열하라는 요구사항을 충족하려면
#     층을 우선 정하고 해당 층의 물품칸을 순회하는 식으로 배치해야 값이 자연스러운
#     순서로 추가된다.
# 2. [안쪽 반복문은 무엇을 도는가]
#     물품 칸
#    [왜]
#     바깥 반복문에서 층이 정해진 후 해당 층의 물품을 왼쪽부터 확인한다 했으니
#     리스트를 정방향으로 순회하면서 각각 조건문을 통과시키는 식으로 접근한다.    
# 3. [조건을 만족했을 때 결과에 무엇을 넣는가]
#     (f, i)형태의 튜플을 추가한다.
#    [왜](확인함)
#     조건을 만족하면 해당 물품의 위치를 나타내는 바깥, 안쪽 반복문 인덱스를 
#     튜플 형태로 만든다. 조건을 만족한다면 모두 넣기에 매 반복문마다 
#     초기화되는 변수를 설정할 것 없이 내부 반복문이 끝날 때마다 바로 추가한다.
#     예시_01을 넣었을 때 결과는 [(0, 0), (2, 0), (1, 1)]이 나왔다.
#     인덱스를 바로 튜플에 넣는 식으로 해 모든 숫자가 정답과 동일하진 않았으나
#     (0, 0), (1, 1)은 정답과 같아 보임에도 오답이다. 겉보기에는 같으나 
#     가리키는 값이 다르다. 정답이 (첫 층, 첫 물품칸)이라면 이건 (첫 물품칸, 첫 층)
#     인데 우연히 대응값이 같았을 뿐이다.  
# 4. [결과를 반환하는 자리는 어디인가]
#     바깥 반복문 밖
#    [왜]
#     바깥 반복문까지 모두 돌며 결과 리스트에 물품 칸 위치 튜플을 추가한 뒤에 
#     리스트를 반환해야 중간에 누락된 값이 없다. 
def find_positions(shelf, target):
    t_loc_lst = []
    for f, r in enumerate(shelf):
        for i, c in enumerate(r):
            if c == target:
                t_loc = (f, i)
                t_loc_lst.append(t_loc)
    return t_loc_lst
# 1   | r = shelf[0] | c = shelf[0][0]|  1   |   True       | [(0, 0)]
# 2   | r = shelf[0] | c = shelf[0][1]|  2   |   False      | [(0, 0)]
# 3   | r = shelf[0] | c = shelf[0][2]|  1   |   True       | [(0, 0), (0, 2)]
# 4   | r = shelf[1] | c = shelf[1][0]|  3   |   False      | [(0, 0), (0, 2)]
# 5   | r = shelf[1] | c = shelf[1][1]|  1   |   True       | [(0, 0), (0, 2), (1, 1)]
# 6   | r = shelf[1] | c = shelf[1][2]|  2   |   False      | [(0, 0), (0, 2), (1, 1)] 
# 내가 만든 입력 | 그렇게 만든 이유 | 예상 결과 | 실제 결과
# [[4, 3, 1], [0, 2, 3]], 3|위치가 순서대로 나오나 궁금|[(0, 1), (1, 2)]|[(0, 1), (1, 2)]
# [[0, 0, 1], [0, 1, 1], [1, 1, 1]], 1| 같은 개수의 칸을 가진 층수가 높아질 때 결과가 궁금|
# [(0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]| 예상과 동일
print(find_positions([[4, 3, 1], [0, 2, 3]], 3))
print(find_positions([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 1))
# 막힌 지점            : 무작위로 임계값이나 튜플 등의 개념 등을 얕게 머릿속으로 적용
#                       하는 걸 구조가 나올 때까지 반복하는 접근방식을 고수하다 30분을
#                       썼다. 최근 손으로 쳐서 간단하게나마 정리가 되는 정보만
#                       머릿속에서 박스 테두리를 치는 이미지화 작업을 반복 중이었다.
#                       박스 테두리가 쳐진 정보만 써서 다시 접근하자 6분 만에 
#                       코드가 완성되었다. 다음 문제부터는 이 방식을 쓸 생각이다.
# 문제 소요 시간       : 36분 소요
# 예측과 실제가 달랐던 곳 : 예측과 실제 사이 차이는 없었다.

# 지문에서 찾은 신호어 : '규칙을 몇 번 적용해야'
# 선택한 골격         : 조건문, 카운팅
# 그렇게 판단한 이유   : 조건을 만족할 때까지 조건을 몇 번 적용하는지 그 개수를
#                     세니 카운팅을 써야 한다 판단했다.
# 반환 형태 (지문에서 그대로 옮겨 적기) : '그 횟수를 정수로 변환하는'
#
# 추가 질문 1: 반복을 몇 번 해야 하는지, 코드를 짜기 전에 알 수 있나요?
#             예시_01(6)은 8번, 예시_04(7)는 16번입니다.
#             6과 7 사이의 관계에서 8과 16을 미리 계산할 수 있나요?
# 답 : 시간을 들이면 미리 계산할 수도 있겠지만 제한적이다.
#
# 추가 질문 2: 지금까지 쓴 반복문은 리스트를 끝까지 돌면 알아서 멈췄습니다.
#             이 문제에는 돌 리스트가 없습니다. 그럼 반복은 언제 멈춰야 하나요?
# 답 : n == 1이 False 값을 반환할 때

# 변수 이름 | 담기는 것 | 시작값 | 시작값의 이유 | 반복이 끝나려면 무엇이 바뀌어야 하나
# n        | 입력된 정수|  n   | 이 값으로 시작해 조건을 적용하니 변경은 없다.| n==1이 거짓이 되어야 한다.
# steps_cnt| 조건문이 적용된 횟수|   0  | 문제는 한 번도 조건이 적용되지 않았을 때 0이라 규정했다.|이 변수에 마지막으로 1이 더해진 후 
 0-1. [횟수를 세는 변수 - 시작값]
#       steps_cnt = 0으로 둔다
#      [왜]
#       조건이 적용된 횟수를 세는 게 목적이니 한 번도 적용되지 않으면 0부터 시작해야 한다.
# 0-2. [반복을 언제까지 계속할 것인가]
#       while n == 1: 이 False값을 반환할 때까지
#      [왜]
#       정해진 literable요소가 없어 종료조건을 설정하지 않으면 무한루프가 발생한다.
#       n을 바꾸는 줄을 주석처리하자 프로그램이 멈춰 강제로 빠져나와야 했다.
#       계속해서 n값이 입력되니 터미널이 표시하기 어렵다.
# 1. [짝수인지 홀수인지 어떻게 판정하는가]
#     2로 나눈 나머지가 0이면 짝수, 아니면 홀수로 하는 조건문을 설정한다. 
#    [왜]
#     짝수는 2로 나눴을 때 나누어떨어지는 정수를 말한다. 나머지가 남지 않을 테니 
#     해당 조건을 만족하면 짝수, 아니면 홀수로 본다. 
def count_steps_to_one(n):
    steps_cnt = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            steps_cnt += 1
        elif n % 2 != 0:
            n = n * 3 + 1
            steps_cnt += 1
    return steps_cnt
    # 막힌 지점            : while 조건문 정지 조건을 혼동했다.
# 문제 소요 시간       : 26분 소요
```
