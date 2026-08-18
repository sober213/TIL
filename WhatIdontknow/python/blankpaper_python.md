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
**피드백 역질문 답변**
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
```
지문에서 찾은 신호어 : "가장 높은 ~ 인덱스", "모두 모아 리스트로 반환"
# 선택한 골격         : (이 문제는 골격이 2개입니다. 모두 쓰세요) 탐색, 필터링
# 그렇게 판단한 이유   : 주어진 리스트 내 가장 높은 온도값을 우선 찾아내야 하기에 탐색.
#                     탐색 조건을 만족하는 날의 인덱스를 리스트에 모아 내려 필터링 사용. 
#                     
# 반환 형태 (지문에서 그대로 옮겨 적기) : "모두 모아 리스트로 반환하는"
#
# 추가 질문: 1주차 03번은 '가장 먼저 나온 날'의 인덱스 하나만 반환했습니다.
#            이 문제는 무엇이 달라졌고, 그래서 어떤 골격이 하나 더 필요한가요?
# 답 : 이 문제는 가장 높은 온도를 가진 날이 여럿일 시 모두 반환함을 요구한다. 
#      조건을 만족하는 날의 인덱스를 모두 한 리스트에 더하려면 필터링이 필요하다.

변수 이름 | 담기는 것 | 시작값 | 그 시작값이어야 하는 이유
# hst_temp | 최고 기온값 |temps[0] | 영하, 영상과 비교할 시 조건을 타지 않기 때문
# hst_idx_result  | 최고 기온 기록날의 인덱스 목록| [] | 조건을 만족하는 인덱스를
#                                                    리스트에 추가하려 빈 리스트

# 0. [시작값을 무엇으로 둘 것인가] (변수 2개 모두)
#     hst_temp = temps[0], hst_idx_result = []으로 둔다.
#    [왜]
#     영하 기온까지 비교해 최고기온을 탐색해야 하니 0이 아닌 리스트의 첫값으로 
#     설정, 탐색으로 찾은 인덱스를 리스트에 추가하기 위해 빈 리스트로 둔다.  
# 1. [지금까지의 최고 기온보다 '더 높은' 값을 만났을 때 무엇을 하는가]
#     hst_idx_result를 반복문 내에서 초기화한다.
#    [왜]
#     초기화시키지 않으면 순회하며 추가했던 리스트에 갱신 전 최대기온 날짜 인덱스까지
#     들어간 채 반환된다. [0, 1, 2] 첫날 21도가 최고기온 조건을 만족해 인덱스에 
#     추가된 값이 그대로 출력된다.
# 2. [지금까지의 최고 기온과 '같은' 값을 만났을 때 무엇을 하는가]
#     최고 기온을 갱신하지 않고 해당 값의 인덱스만 리스트에 추가한다.
#    [왜]
#     최고 기온을 기록한 "모든"날을 기록하니 동일값이 나온 경우의 조건을 추가해 
#     인덱스를 추가해야 모든 날짜의 인덱스를 기록할 수 있다. 
# 3. [두 경우를 부등호로 각각 어떻게 쓸 것인가]
#     >, == 로 쓴다.
#    [왜]
#     >=를 쓰면 동일값 상황에서도 최고기온 갱신과 함께 지금까지의 리스트가 초기화되는 
#     경우를 방지하기 힘들다. 분리해서 ==로 완전히 같은 값일 때 조건을 만족하도록 한다.
def find_all_hottest_days(temps):
    hst_temp = temps[0]
    hst_idx = 0
    hst_idx_result = []
    for i, temp in enumerate(temps):
        if temp > hst_temp:
            hst_temp = temp
            hst_idx = i
            hst_idx_result = []
            hst_idx_result.append(i)
        elif temp == hst_temp:
            hst_idx = i
            hst_idx_result.append(i)
    return hst_idx_result
# 회차 | 인덱스 | 꺼낸 값 | 처리 | 최고 기온 | 인덱스 목록
# 시작 |   -   |   -    |  -  |    21    |     [] 
# 1   |   0   |    21  | True|    21    |     [0] 
# 2   |   1   |    25  | True|    25    |     [1]  
# 3   |   2   |    25  | True|    25    |     [1, 2]  
# 4   |   3   |    19  | False|   25    |     [1, 2]  

# [-238, 10, 10]| 영하의 경우에도 코드가 정상작동하는지 궁금해서|[1, 2]|예상과 동일
# [-2, 3, -1, 3]| 간격이 있어도 인덱스가 순서대로 리스트에 입력되나 궁금해서|[1, 3]|예상과 동일

print(find_all_hottest_days([-238, 10, 10]))
print(find_all_hottest_days([-2, 3, -1, 3]))
# 막힌 지점            : 반복문 내에서 조건 만족 인덱스 리스트를 초기화하는 부분을
#                       즉시 떠올리지 못해 출력내용을 보며 찾아냈다.
# 문제 소요 시간       : 26분.
# 예측과 실제가 달랐던 곳 : 인덱스를 급하게 읽다 직관적으로 2번째 인덱스라 생각한 게 
#                        인덱스로는 3으로 표기되어 혼동이 있었다.
# 지문에서 찾은 신호어 : "역대 최고 갱신", "인덱스를 모두 모아"
# 선택한 골격         : (이 문제는 골격이 2개입니다. 모두 쓰세요)탐색, 필터링
# 그렇게 판단한 이유   : 리스트 내 모든 요소를 돌며 역대 순이익을 갱신할 때마다 
#                      찾아야 하니 탐색 적용. 조건을 만족하는 값의 인덱스를 리스트
#                      내 모아 반환해야 하니 필터링을 쓴다.
# 반환 형태 (지문에서 그대로 옮겨 적기) : 역대 최고 순이익을 새로 갱신한 주의 인덱스
#                                    (0부터 시작)을 모두 모아 리스트로 반환하는
# 추가 질문: 03번은 '전체에서 가장 높은 값'을 기준으로 골라냈고,
#            이 문제는 '그 시점까지 가장 높은 값'을 기준으로 골라냅니다.
#            이 차이 때문에 03번에는 있었지만 여기에는 없어도 되는 동작이
#            하나 있습니다. 무엇일까요?
# 답 : 인덱스를 모은 리스트를 초기화하는 동작이 불필요하다.
# 변수 이름 | 담기는 것 | 시작값 | 그 시작값이어야 하는 이유
# r_week   | 역대 최고 순이익 경신 주| profits[0]|순이익이 음수인 주도 존재하니 비교
#                                              시 첫값이 아닌 값으로 경신되지 않도록 한다.
# r_idx_result|경신 주의 인덱스| [] | 빈 리스트로 설정해 조건을 만족한 인덱스를 차례대로
#                                   담을 수 있게 했다.
# 0. [시작값을 무엇으로 둘 것인가] (변수 2개 모두)
#     r_week = profits[0], r_idx_result = []로 둔다.
#    [왜]
#     profits[0]을 최고 기록 변수로 설정하면 인덱스 0에서 꺼낸 값과 비교 시
#     동일해진다. 원래의 '더 큰'조건에 걸려 경신되는 경우는 방지하나 해당 문제의
#     경우 첫 주가 경신된, 즉 조건을 만족함을 요구한다. 실제 예시01을 넣었을 때
#     [1, 4]로 첫 인덱스가 조건을 만족하지 못해 추가되지 않았음을 확인했다.
#     이를 해결하기 위해 조건문에 i == 0라는 조건을 달아 일괄 추가되도록 했다.
# 1. [반복을 몇 번 인덱스부터 시작할 것인가]
#     0번 인덱스부터 시작한다.
#    [왜]
#     첫 주는 비교할 이전 값이 없으니 늘 기록을 경신한 주로 간주한다. 
#     첫 주의 인덱스 0번도 조건을 만족한 리스트에 추가해야 하니 반복 범위 안에 둔다.
# 2. [경신했을 때 무엇을 해야 하는가] (해야 할 일이 2개입니다)
#     경신한 주 변수 r_week를 조건 만족 반복변수로 교체한다. 그 다음 
#     그 반복변수의 인덱스를 r_idx_result에 추가한다.
#    [왜]
#     리스트 내 요소들을 순회하며 비교, 탐색을 진행하나 경신한 주의 인덱스를  
#     모두 추가해야 하니 다음 경신을 위해 최고 기록을 갱신하되 인덱스를 추가하고
#     넘어가야 조건을 만족한 인덱스 리스트를 완성할 수 있다.
# 3. [동점을 경신에서 제외하려면 부등호를 무엇으로 쓸 것인가]
#     >=를 사용하지 않고 >를 쓴다.
#    [왜]
#     동점의 경우는 경신되지 않아야 하니 >(초과)부등호를 쓴다. 동점이 조건을 만족하는
#     유일한 경우(첫 주)는 조건문을 하나 추가해 ==를 쓴다. 

def find_record_weeks(profits):
    r_idx_result = []
    r_week_idx = 0
    r_week = profits[0]
    for i, profit in enumerate(profits):
        if profit > r_week:
            r_week = profit
            r_week_idx = i
            r_idx_result.append(i)
        if i == 0:
            r_idx_result.append(i)
    return r_idx_result
    # 회차 | 인덱스 | 순이익 | 경신?(True/False) | 최고 기록 | 결과 리스트
# 시작 |   -   |   -   |         -        |    10    | []
# 1   |   0    |  10  |        True       |   10    | [0]
# 2   |   1    |  30  |        True       |   30    | [0, 1]
# 3   |   2    |  20  |        False      |   30    | [0, 1]
# 4   |   3    |  30  |        False      |   30    | [0, 1]
# 5   |   4    |  45  |        True       |   45    | [0, 1, 4]
# [2, 2, 3, 3] |같은 값이 연달아 나올 때 어떻게 작동하나 궁금해서|[0, 2]|[0, 2]
# [-1, 0, 100] |0, 음수 등의 값을 둬도 작동하나 궁금해서|[0, 1, 2]|[0, 1, 2]
print(find_record_weeks([2, 2, 3, 3]))
print(find_record_weeks([-1, 0, 100]))
# 막힌 지점            : 첫 인덱스를 조건 만족 리스트에 추가할 때 
#                       시작값 설정과 조건문 설정 시 순서와 형식을 혼동했다.
# 문제 소요 시간       : 17분
# 예측과 실제가 달랐던 곳 : 예측과 실제 결과가 일치했다.
# 지문에서 찾은 신호어 : "2차원 리스트", "평균 순이익이 가장 높은", "지점의 번호
#                     (인덱스, 0부터 시작)"
# 선택한 골격         : (이 문제는 골격이 3개 이상입니다. 모두 쓰세요) 누적, 
#                      중첩 반복문, 탐색, 필터링
# 그렇게 판단한 이유   : 지점마다의 평균을 구하려면 리스트 내 총합을 구해야 하니 누적 사용.
#                     리스트 내 리스트에서 값을 꺼내 돌려야 하니 중첩 반복문을 쓴다.
#                     평균들을 리스트에 추가해야 하니         
# 반환 형태 (지문에서 그대로 옮겨 적기) : "평균 순이익이 가장 높은 지점의 번호(인덱스,..
#                                     정수의 형태로 반환"
# 추가 질문 1: 반복문이 몇 겹 필요한가요? 그렇게 판단한 근거는?
#             (골격을 몇 개 쓰는지와는 상관이 없습니다)
# 답 : 2겹. 리스트 내 요소가 리스트 형태고 이 안의 값에 접근해야 하니  
#      데이터의 깊이는 2라 판단했다. 
# 추가 질문 2: 이 문제는 앞의 01~04번 중 어떤 문제들의 조합인가요?
#             '새로운 유형'이 아니라는 걸 확인하는 질문입니다.
# 답 : 01, 03번의 조합이다.
```

