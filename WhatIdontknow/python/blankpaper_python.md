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




```
### Python Basic Syntax 1

#### 1 프로그래밍이란 무엇인가
프로그램- 컴퓨터에 내릴 명령이나 지시 뭉치, 프로그래밍- 지시를 만드는 작업
#### 2 변수(Variable)
변수는 저장이 아닌 주소를 참조하는 주소록 같은 것
Assignment(할당), = 할당자 
순서: 표현식을 확인, 변수 형식이 적절한가 - 그 값을 변수에 할당
#### 3 DataType
데이터에는 여러 타입이 있고, 다루는 방법이 달라 구분할 필요
#### 3-1 nummeric type
int, float 등 숫자형 데이터
#### 3-2 sequence type
순서를 가지고 나열된 데이터 형식 list, tuple, str, range 
인덱스, 슬라이싱, len, 반복 사용가능 but tuple, str은 불변형이라 값 임의변경x
#### 3-2 non-sequence type
순서가 없는 데이터 set, dict

#### 4 표현식과 문장
표현식: 값 Value(가장 작은 데이터 조각)을 돌려주는 식, 변수에 할당 가능
문장: 명령과 지시(레시피)
표현식을 재료 삼아 문장을 조합해 프로그램을 만든다

### Python Basic Syntax 2

#### 1 시퀀스형 자료
순서가 존재하는 데이터
#### 1-2 List
리스트- 존나 만만한 자료형, 순서 존재하고 변경 가능
슬라이싱은 [start : stop : step] start값은 포함, stop값 포함x step은 간격
#### 1-3 Tuple
, ()없어도 만들어짐, 순서가 존재하나 한 번 만들어지면 절대 변경 못함 
백트레일 콤마(가독성을 위해) 끝마다 하나씩- 마지막 한 칸을 내려 괄호닫기
#### 1-4 Str
문자열: 순서가 존재, 역시 immutable
#### 1-5 Range
순서대로 정수를 나열하는 자료형 매개변수 세 개까지 가질 수 있음
range(start, stop, step) 기본적으로 stop앞에서 멈춤, 0부터 시작, step은 1로 설정됨
#### 2 변경/불변 자료형

#### 2-1 Dict
{"key": value, ..}로 표현, 불변 자료형만 넣는 key와 다 되는 value로 구성 
순서와 중복(key)없는 자료형, 임의로 변경 가능한 자료형 조회와 추가 가능
#### 2-2 Set
수학의 집합을 옮겨놓은 듯한 자료형. 순서와 중복 없는 자료형
빈 세트는 set()로 시작해야, set1 | set2 합집합/ set1 & set2 교집합
#### 3 Collection
값들이나 데이터를 모아놓을 수 있는 타입
list, tuple, Set, Dict
#### 4 연산자
자료들끼리 적극적 동작? ()-> [] -> ** -> - 순 
#### 4-2 복합 연산자
a = a + b == a += b
#### 4-3 멤버십 연산자
어떤 값이 옆의 collection에 포함되어 있나 확인하는 용도
a in [] 
#### 4-4 논리 연산자 
True나 False값을 반환하는 boolean
==, !=, and, or 조건 없을 시 and- 거짓이 나오면 통과, 참이면 반환 없으면 마지막
단축 연산
#### 5 형변환
암시적- 파이썬이 개판나기전에 몰래 고쳐주는것 3.0 + 2 
명시적- 이렇게 바꾸라 직접 명령하는 것 int("2")

### Python Functions

#### 1 함수(Functions)
특정 행동을 정해놓은 코드뭉치? 
한 번 만들어놓으면 계속 쓸 수 있음
def calculate_store_sale(): (동사_형용사_명사 순으로 직관적 정의)
#### 1-2 내장함수(built-in functions)
파이썬에 기본적으로 있는 유용한 함수 
max, min, sum, sorted, len등
#### 2 매개변수와 인자
parameter: 함수가 받을 값-어떻게 둬도 상관없으나 알아보기 쉽게끔 작성
위치 변수/ 기본값 변수(Value Default Parameter)- name = "홍길동" 처럼
.get()등으로 호출했을 때 기본적으로 나오는 변수/ *args/ **kwargs
#### 2-1 위치인자, 키워드 인자, 가변 인자
인자 - 실제로 함수에 전달되는 값 
위치인자는 기본적으로 정해진..
#### 3 재귀함수(Recursion)
스스로 자기 자신을 불러오는 함수
함수 내 종료 조건을 정해야 함
#### 4 스코프
변수의 위치 참조 순위? local -> enclsoed -> global -> built_in
global 변수로 안쪽에서 함수 전역에 변수를 적용할 수 있음
#### 5 패킹
*를 앞에 둬서 여러 값을 튜플로 묶음/ **를 앞에 둬서 키워드 변수들을 딕셔너리 형태로 묶는 게 패킹
#### 5-2 언패킹
각각의 변수에 다시 풀어내는 언패킹
기본 - 변수 수를 일치시켜서/ *함수 호출할 때/ **매개변수명
#### 6 람다 함수
lambda 매개변수 : 표현식 ->임시함수
#### 7  지연함수(map, zip, range)
map - 게으른 요리사 
바로 음식을 만드는 게 아니라 레시피 형태로
저장해놓았다가 요청하면 만들어 주는 느낌 