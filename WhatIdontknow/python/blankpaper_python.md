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